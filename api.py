from flask import Flask, request, render_template, redirect
import json 

app = Flask(__name__)

@app.route('/')
def index():
    return redirect("/basic-prediction/")

@app.route("/basic-prediction/", methods=["GET", "POST"])
def make_basic_prediction(): 
    if request.method == "GET":
        return render_template("basic_prediction.html")
    if request.method == "POST":
        data = request.form.get('last-fifteen-candles')

        json_form_data = {}
        print("data " +  str(data))
        try:
            json_form_data = json.loads(data)
        except:
            return """Error decoding json form <a href="/">Back</a>"""
        
        last_fifteen_candles = json_form_data["last_fifteen_candles"]

        #TODO: handle model interactions here

        return "Data received: " + json.dumps(json_form_data, indent=2) + """<a href="/">Back</a>"""

if __name__ == '__main__':
    app.run(debug=True)
