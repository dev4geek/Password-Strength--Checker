from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check():

    password = request.form['password']

    score = 0

    if len(password) >= 8:
        score += 1

    if re.search(r'[A-Z]', password):
        score += 1

    if re.search(r'[a-z]', password):
        score += 1

    if re.search(r'\d', password):
        score += 1

    if re.search(r'[@$!%*?&]', password):
        score += 1

    if score <= 2:
        strength = "Weak"

    elif score <= 4:
        strength = "Medium"

    else:
        strength = "Strong"

    return render_template(
        'index.html',
        strength=strength,
        password=password
    )

if __name__ == "__main__":
    app.run(debug=True)