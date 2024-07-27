from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def clean_csv(input_file, output_file):
    if not os.path.exists(input_file):
        print(f"Error: The file {input_file} does not exist.")
        return
    df = pd.read_csv(input_file)

    # Attempt to read the file with utf-8 encoding, fallback to other encodings if it fails
    encodings = ['utf-8', 'latin1', 'iso-8859-1', 'cp1252']
    for encoding in encodings:
        try:
            df = pd.read_csv(input_file, encoding=encoding)
            break

        except UnicodeDecodeError as e:
            print(f"Error reading {input_file} with encoding {encoding}: {e}")
            if encoding == encodings[-1]:
                return

    for column in df.columns:
        if df[column].dtype in ['int64', 'float64']:
            median_value = df[column].median()
            df[column].fillna(median_value, inplace=True)
        else:
            mode_value = df[column].mode()[0]
            df[column].fillna(mode_value, inplace=True)
    
    df_cleaned = df.drop_duplicates()
    df_cleaned.to_csv(output_file, index=False)
    print(f"Cleaned data saved to {output_file}")

@app.route('/', methods=['GET', 'POST'])
def index():
    msg = None
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file:
            input_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            output_path = os.path.join(app.config['UPLOAD_FOLDER'], f"cleaned_{file.filename}")
            file.save(input_path)
            clean_csv(input_path, output_path)
            msg = f"File has been uploaded and cleaned successfully!"
            print(msg)
    return render_template('index.html', msg=msg)

@app.route('/uploads/<filename>')
def download_file(filename):
    return redirect(url_for('static', filename=f"uploads/{filename}"))

if __name__ == "__main__":
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)
