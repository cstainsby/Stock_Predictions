# Stock_Predictions

## High Level Project Overview

Create a model that takes in OHLC price data, creates an image, creates a prediction, then trades based off of said prediction

## Training, Backtesting Workflow

### Step 1: Data collection
1. Historical data is collected using YahooFinance on various futures contracts including Forex, Indeces, Commodities, and Interest Rates
2. Data is cleaned and put into a format that can be used to create images/is friendly for testing. This includes 1m, 2m, 5m, 1h, 1d time frames. Found 2m works best, others are now irrelavent
3. Labels are created for returns over 6m, 8m, and 10m time frames. 6m works best and will be the only one used for the foreseeable future
4. Other feature engineering is performed for future models, but not used in the current model which uses images only
5. S&P Futures (Ticker/Representation: ESF and ES=F) are used for the training and validation sets, validation set was manually selected to ensure representation of training set
6. Training and Validation set uses step size of 5 to avoid overlap, this lowers dataset size but ensures more variation in images
7. Test sets are step size of 1, so all possible trades/times are represented to be tested on 
8. Images are saved to a google drive folder

### Step 2: Image Classification Model Training
1. Utilizes PyTorch to create custom models and import pretrained models for finetuning
2. Load and preprocess images
3. Gridsearch over hyperparameters for custom models
4. Gridsearch over hyperparameters for pretrained models
5. Select models best for certain aspects to create ensemble later

### Step 3: Model Testing/Backtesting
1. Test best models over various out of sample observations including various contract types and out of sample time frames
2. Judge based off win/loss ratios, class accuracies, and F1 scores
3. Create backtesting code to guage returns on various portfolio sizes (Currently Working On: Travis)
4. Create popular voting and averaging ensembles, repeat parts 1-3 (Currently Working On: Travis)
5. Create ANN and LSTM ensemble using Image Classification outputs and pricing data, repeat parts 1-3

## Live Data Testing (Currently Working On: Cole):
1. Identify API to collect required data for simple, singular model (no ensembling, only best image classification model)
2. Data Requirements for API:
    - Time
    - Date
    - 2 minute OHLC prices
    - Last 15 candlesticks 
4. Clean and engineer data as needed
5. Pass data through image creator
6. Pass image through model
7. Save important info for future analysis:
  a. Close price of final candle stick
  b. Probabilities of each class (bull, bear, neutral)
  c. Predicted movement (max of probabilities)
8. Calculate trade returns (use close price of the candle 6 minutes/3 candles from prediction candle)

## Future Goals
1. Create live data portfolio simulation
2. Live data using ensemble methods
3. Define more rigorous trading conditions
4. Create SQL database
5. Use with real money

