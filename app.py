from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def rootpage():
    weight = ''
    height = ''
    bmi = ''
    health = ''
    if request.method == 'POST' and 'weight' in request.form and 'height' in request.form:
        weight = int(request.form.get('weight'))
        height = float(request.form.get('height'))
        bmi = float("{:.2f}".format(weight / (height * height)));

        if (bmi < 18.5):
            health = 'underweight'
        elif (bmi >= 18.5 and bmi <= 24.9):
            health = 'normal weight'
        elif (bmi >= 25 and bmi <= 29.9):
            health = 'overweight'
        else:
            health = 'obese'
    
    return render_template('index.html', format_bmi = bmi, health = health)

app.run(port = 7777)