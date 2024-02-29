
from typing import List

import plotly.graph_objects as go



# Function 1: Labeling
# This func takes in price data, calculates the future change in price, then creates a label. This may not be needed for live data, easier to explain over a call on caveats of how this works. More documentation in code

def label_price_data():
    pass

# Function 2: Momentum Indicator Creation
# This func will not be used in the current model, used when ensembling with an LSTM or ANN but creates moving averages and other momentum indicators.

# Function 3: Data Cleaning
# When training/testing model I pulled historical data from yahoo finance and needed to do some data cleaning. See code for documentation of each line, only 5 lines



# Function 4: Candlestick Creation
# This is the function that takes in the OHLC data and transforms it to a candlestick chart. This will most likely benefit from some augmentation for live data
#   Arguements:
#     Data: this is the dataframe that contains all of the OHLC data, dates, etc.
#     image_folder_base: This is the google drive folder path where the images are stored
#     candles: this is the number of candles per image, set this to 15
#     step: step size is how I skipped candles for training purposes so there was minimal overlap. For test data this is set to 1 so that there are no skips, this arguement will most likely not be used in live data

#   In depth explanation:
#     line 1: get all unique dates
#     line 2: for loop so it performs iterates through each date
#     line 3: day_df data frame is filtered on the current iteration date
#     line 4&5: start candle is set to the first row in day_df data frame, end candle is set to candles arguement, 15 in this case
#     line 6: While loop, this way it does not try to create charts if there are not enough data points
#     line 7: This uses start candle and end candle as the index values to create a sequence of data points 15 rows in length
#     line 8: This uses a library to create the candlestick charts, the reason it is labeled things like 'Open_2m' is that in the test/train data I also had 1m, 5m, etc. data OHLC data points, this naming convention will not be super relevant on live data as we only need 2m most likely
#     line 9: This takes the label (bull, bear, neutral) from the SixMinLabel column. Will not have labels for live data as we do not have the future 6 minute returns info obviously
#     line 10: Indicates the output folder path, for training purposes the label needed to be included in the folder name
#     line 11: creates a file name for each image, pretty self explanatory
#     line 12: writes the file to said folder w/ said file name
#     line 13&14: Moves to next rows, i.e. goes from row 0 and 15 to 1 and 16


def create_candle_stick_jpeg_figure(ohlc_data: List[dict]) -> go.Figure:
    """
    Creates a candlestick jpeg figure object from ohlc_data
    
        Parameters:
            ohlc_data (list): a list of json formated candlestick datapoints in sequence.

        Returns:
            candle_stick_chart (go.Figure): A Plotly figure representing the ohcl data
    """
    candle_stick_chart = None

    date_times = [candlestick_datapoint["date-time"] for candlestick_datapoint in ohlc_data]
    open_prices = [candlestick_datapoint["open"] for candlestick_datapoint in ohlc_data]
    high_prices = [candlestick_datapoint["high"] for candlestick_datapoint in ohlc_data]
    low_prices = [candlestick_datapoint["low"] for candlestick_datapoint in ohlc_data]
    close_prices = [candlestick_datapoint["close"] for candlestick_datapoint in ohlc_data]
    
    candle_stick_chart = go.Figure(data=[go.Candlestick(
        x=date_times,
        open=open_prices,
        high=high_prices,
        low=low_prices,
        close=close_prices
    )])
    
    return candle_stick_chart
