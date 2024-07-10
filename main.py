from flask import Flask, render_template

app = Flask("Website")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/v1/<station>/<date>")
def about(station, date):
    df = pandas.read_csv("")
    temperature = df.station(date)
    return render_template("about.html")

app.run(debug=True)





