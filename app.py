from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def rootpage():
    weight = ''
    height = ''
    bmi = ''
    format_bmi = ''
    health = ''
    if request.method == 'POST' and 'weight' in request.form and 'height' in request.form:
        weight = int(request.form.get('weight'))
        height = float(request.form.get('height'))
        bmi = weight / (height * height);
        format_bmi = float("{:.2f}".format(bmi))

        if (format_bmi < 18.5):
            health = 'underweight'
        elif (format_bmi >= 18.5 and format_bmi <= 24.9):
            health = 'normal weight'
        elif (format_bmi >= 25 and format_bmi <= 29.9):
            health = 'overweight'
        else:
            health = 'obese'
    
    return render_template('index.html', format_bmi = format_bmi, health = health)

app.run(port = 7777)