from flask import Flask, render_template
import music

app = Flask(__name__)

'''
PERIOD_OVERALL = "overall"
PERIOD_7DAYS = "7day"
PERIOD_1MONTH = "1month"
PERIOD_3MONTHS = "3month"
PERIOD_6MONTHS = "6month"
PERIOD_12MONTHS = "12month"
'''

@app.route("/")
def index():
    try:
        music.generate_report('7day')
        return render_template("index.html",report=music.report)
    except Exception as e:
        return render_template("error.html",message=e)    

@app.route("/30")
def month():
    try:
        music.generate_report('1month')
        return render_template("index.html",report=music.report)
    except Exception as e:
        return render_template("error.html",message=e)

@app.route("/90")
def month3():
    try:
        music.generate_report('3month')
        return render_template("index.html",report=music.report)
    except Exception as e:
        return render_template("error.html",message=e)

@app.route("/180")
def month6():
    try:
        music.generate_report('6month')
        return render_template("index.html",report=music.report)
    except Exception as e:
        return render_template("error.html",message=e)

@app.route("/365")
def year():
    try:
        music.generate_report('12month')
        return render_template("index.html",report=music.report)
    except Exception as e:
        return render_template("error.html",message=e)


if __name__ == '__main__':
   app.run(debug=True,port=3000)

