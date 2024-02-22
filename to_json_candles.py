import csv
from datetime import datetime, timedelta
import pandas as pd
import json

def parse_csv_to_json(csv_file, start_day, start_time):
    start_datetime = datetime.strptime(start_day + ' ' + start_time, '%Y-%m-%d %H:%M:%S')

    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        data = list(reader)

    df = pd.read_csv(csv_file)
    df['DateTime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'])

    start_datetime = datetime.strptime(start_day + ' ' + start_time, '%Y-%m-%d %H:%M:%S')
    df = df[df['DateTime'] >= start_datetime]

    # Extract the last fifteen candles
    last_fifteen_candles = df.tail(15)

    json_data = {
        "last_fifteen_candles": [
            {
                "date-time": row['DateTime'].strftime('%Y-%m-%d %H:%M:%S'),
                "open": row['Open_2m'],
                "high": row['High_2m'],
                "low": row['Low_2m'],
                "close": row['Close_2m'],
                "timeframe": "2m"
            }
            for index, row in last_fifteen_candles.iterrows()
        ]
    }

    return json_data

if __name__ == "__main__":
    csv_file = 'NQF.csv'
    start_day = '2023-11-20'
    start_time = '13:00:00'
    json_data = parse_csv_to_json(csv_file, start_day, start_time)
    
    with open("sample_candle_series.json", 'w') as out:
        json.dump(json_data, out, indent=2)