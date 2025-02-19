# CodeAlpha_CSV_Cleaner

CSV Cleaner is a web-based tool to clean your CSV files by removing duplicates and `None` values. This tool helps ensure your data is clean and ready for analysis, enhancing the quality of your decisions based on that data.



<img width="1440" alt="Screenshot 2024-07-27 at 6 05 13 PM" src="https://github.com/user-attachments/assets/46794a13-809b-4c5f-a4f6-c26472109aee">
<img width="1440" alt="Screenshot 2024-07-27 at 6 05 25 PM" src="https://github.com/user-attachments/assets/2dc7976e-5127-4534-ac77-456bc58d19e1">

## Features

- Upload CSV files through a simple web interface.
- Clean data by removing duplicate rows and rows with `None` values.
- Receive feedback through the web interface upon successful cleaning.

## Installation

To set up the CSV Cleaner on your local machine, follow these steps:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/omarrrefaatt/CSV_Cleaner.git
    cd CSV_Cleaner
    ```

2. **Create a virtual environment and activate it:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the application:**
    ```bash
    python app.py
    ```

2. **Open your web browser and go to:**
    ```
    http://127.0.0.1:5000/
    ```

3. **Upload your CSV file and let the tool clean it.**

## File Overview

- **`app.py`**: The main Flask application that handles file uploads, cleaning, and rendering HTML templates.
- **`index.html`**: The HTML template for the main page, allowing users to upload their CSV files.
- **`static/style.css`**: The CSS file for styling the web page.
- **`static/images/`**: Directory containing images used in the web interface.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.


## Acknowledgments

- Special thanks to the Flask community for their comprehensive documentation .
- Gratitude to the maintainers of Pandas for their invaluable tool in data manipulation and cleaning.
- Appreciation to the open-source community for their contributions and shared knowledge.


## Contact

If you have any questions or suggestions, feel free to open an issue or contact me directly at [omarref3at2031@gmail.com].

---

By Omar Ahmed Mohamed
