from flask import Flask, request, jsonify, render_template, redirect, url_for
from health_utils import calculate_bmi, calculate_bmr

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/bmi-page')
def bmi_page():
    return render_template('bmi.html')

@app.route('/bmr-page')
def bmr_page():
    return render_template('bmr.html')

@app.route('/bmi', methods=['POST'])
def bmi():
    height = float(request.form['height'])
    weight = float(request.form['weight'])
    result = calculate_bmi(height, weight)
    return render_template('bmi.html', bmi=result)


@app.route('/bmr', methods=['POST'])
def bmr():
    height = float(request.form['height'])
    weight = float(request.form['weight'])
    age = int(request.form['age'])
    gender = request.form['gender']
    result = calculate_bmr(height, weight, age, gender)
    return render_template('bmr.html', bmr=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
