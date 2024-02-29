from flask import Flask, request, render_template, redirect
import json 

from stock_data_helper_functions import create_candle_stick_jpeg_figure
from dense_net_model import DenseNetModel

app = Flask(__name__)
model = DenseNetModel()

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
        try:
            json_form_data = json.loads(data)
        except Exception as e:
            return render_template(
                "error.html", 
                error_description="Error decoding JSON input value.", 
                user_input_value=data,
                returned_error_message=repr(e))

        if len(json_form_data) < 15:
            return render_template(
                "error.html", 
                error_description="Missing " + str(15 - len(json_form_data)) + " candles (too few, Fifteen Required)", 
                user_input_value=data) 
        # for now, not allowing going over required data input count.
        if len(json_form_data) > 15: 
            return render_template(
                "error.html", 
                error_description="Found " + str(len(json_form_data)) + " candles (too many, Fifteen Required)", 
                user_input_value=data)  

        last_fifteen_candles = json_form_data
        candlestick_figure = create_candle_stick_jpeg_figure(last_fifteen_candles)
        predicted_direction_of_stock = model.make_prediction(candlestick_figure)

        return "Predicted Direction: " + predicted_direction_of_stock.name + """<a href="/">Back</a>"""

if __name__ == '__main__':
    app.run(debug=True)
