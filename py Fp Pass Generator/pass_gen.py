import random
import string
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# List to store generated passwords
generated_passwords = []

def generate_password(name, birthdate, length=12):
    # Use the name and birthdate to create a personalized password
    personal_info = name.lower() + birthdate.replace("-", "")

    # Characters for the rest of the password, including special characters
    rest_characters = string.ascii_letters + string.digits + string.punctuation + '@#$%^&*'

    # Calculate the minimum length needed for personal_info
    min_personal_info_length = min(length, 6)

    # Generate the rest of the password
    rest_password = ''.join(random.choice(rest_characters) for _ in range(length - min_personal_info_length))

    # Combine personal info and the rest of the password
    password = personal_info[:min_personal_info_length] + rest_password
    
    # Shuffle the password characters to make it more random
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    # Store the generated password
    generated_passwords.append(password)

    return password

@app.route('/')
def index():
    return render_template('pass.html', passwords=generated_passwords)

@app.route('/generate_password', methods=['POST'])
def generate_password_route():
    name = request.form.get('name')
    birthdate = request.form.get('birthdate')
    length = request.form.get('length')

    if not name or not birthdate or not length:
        return jsonify({'error': 'Name, birthdate, and length are required'})

    try:
        length = int(length)
        if length < 6:
            raise ValueError("Length must be at least 6")
    except ValueError as e:
        return jsonify({'error': str(e)})

    password = generate_password(name, birthdate, length)
    return render_template('pass.html', password=password, passwords=generated_passwords)

if __name__ == '__main__':
    app.run(debug=True)
