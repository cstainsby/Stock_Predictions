import torchvision.models as models
from torchvision.models import densenet121
from torchvision import transforms
import plotly.graph_objects as go
import torch
import torch.nn.functional as F
from torch.utils.data import DataLoader, Dataset
import os
import io
from enum import Enum
from PIL import Image

class TrendClassification(Enum):
    BULL = 0
    BEAR = 1
    NEUTRAL = 2

class DenseNetModel():
    def __init__(self) -> None:
        """Constructor"""
        model = densenet121(pretrained=False)
        num_ftrs = model.classifier.in_features
        model.classifier = torch.nn.Linear(num_ftrs, 3)

        # load weights if availible
        model_weights_path = "model_weights/weights.pt"
        if os.path.exists(model_weights_path):
            loaded_weights = torch.load(model_weights_path)
            model.load_state_dict(loaded_weights)

        # model.to(device)
        self.model = model

    def __tensorfy_candlestick_image(self, candle_figure: go.Figure) -> torch.Tensor:
        """
        Converts a plotly figure into a pytorch tensor which can be understood by the DenseNet Model.
        
            Parameters:
                candle_figure (go.Figure): A plotly image figure containing sequenced candlestick information.
            
            Returns:
                image_tensor (Pytorch Tensor): The candle figure transformed into a pytorch tensor.
        """
        image_tensor = None

        fig_bytes = candle_figure.to_image("jpg")
        buf = io.BytesIO(fig_bytes)
        img = Image.open(buf)
        img = img.convert("RGB")

        transform_function = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
        ])
        image_tensor = transform_function(img)
        return image_tensor

    def make_prediction(self, candle_figure: go.Figure) -> TrendClassification:
        """
        Makes a Above/Below/Neutral classification on data using a candlestick image figure.

            Parameters:
                candle_figure (go.Figure): A plotly image figure containing sequenced candlestick information.

            Returns:
                prediction (TrendClassification): An enum value for representing a forecasted result of Bull/Bear/Neutral 

        """
        prediction: TrendClassification = None

        figure_tensor = self.__tensorfy_candlestick_image(candle_figure)
        figure_tensor = torch.unsqueeze(figure_tensor, 0)


        model_outputs = self.model(figure_tensor)
        output_probabilities = F.softmax(model_outputs, dim=1)
        print("Output Probabilities: " + str(output_probabilities))
        _, raw_prediction = output_probabilities.max(1)

        # map prediction tensor to Enum
        #   0 -> 
        #
        #
        print("Prediction Made: " + str(raw_prediction))
        predicted_class_num = raw_prediction.tolist()[0]
        if raw_prediction == TrendClassification.BEAR.value:
            prediction = TrendClassification.BEAR
        elif raw_prediction == TrendClassification.BULL.value:
            prediction = TrendClassification.BULL
        elif raw_prediction == TrendClassification.NEUTRAL.value:
            prediction = TrendClassification.NEUTRAL
        return prediction