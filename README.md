# PASSWORD-GENERATOR

## Description  
This is a Flask-based web application that generates strong and personalized passwords based on user input, including name and birthdate. The generated passwords are stored and displayed on the webpage.  

## Features  
- Generates a password using the user's name and birthdate.  
- Adds random characters to enhance security.  
- Ensures a minimum password length of 6 characters.  
- Displays previously generated passwords.  
- Simple and interactive web interface using Flask.  

## Requirements  
- Python 3.x  
- Flask  
- HTML template (`pass.html`)  

## Installation & Setup  
1. Clone the repository or copy the script files.  
2. Install Flask using pip:  
   ```bash
   pip install flask
   ```  
3. Run the Flask application:  
   ```bash
   python app.py
   ```  
4. Open your browser and go to `http://127.0.0.1:5000/` to access the web app.  

## Endpoints  
- **`/`** : Displays the homepage with generated passwords.  
- **`/generate_password`** (POST): Accepts user details and generates a password.  

## Usage  
1. Enter your name and birthdate.  
2. Set the desired password length (minimum 6 characters).  
3. Click the generate button to receive a secure password.  

## Technologies Used  
- Flask (Python)  
- HTML & Jinja2 Templates  
- Random & String Libraries  

## Notes  
- Passwords are stored temporarily for display but are not saved permanently.  
- Ensure you keep your generated password safe.  

## License  
This project is for educational purposes. Modify and use it as needed!  

---

Let me know if you need any modifications! 🚀
