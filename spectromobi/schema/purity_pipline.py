from pydantic import BaseModel, Field
from typing import Any
from spectromobi.schema.prediction import (
    PredictionRequest, 
    ClassificationModel, 
    RegressionModel,
    ClassificationScalars,
    StandardScalars,
    LabelDecoder
    )

class OilPurity_Input(BaseModel):
    img: bytes = Field(description="Image bytes for prediction")
    params: PredictionRequest = Field(description="Prediction parameters")

class ModelsLoaderFunctionInput(BaseModel):
    """
    Pydantic model for the input of the model loader function.
    """
    classification_model: ClassificationModel = Field(description="The classification model")
    regression_model: RegressionModel = Field(description="The regression model")
    classification_scaler: ClassificationScalars = Field(description="The classification scaler")
    standard_scaler: StandardScalars = Field(description="The standard scaler")

class ModelLoaderFunctionOutput(BaseModel):
    """
    Pydantic model for the output of the model loader function.
    """
    classification_model: Any = Field(description="The classification model")
    classification_scaler: Any = Field(description="The classification scaler")
    prediction_models: dict[int,Any] = Field(description="The prediction models")
    standard_scalers: dict[int,Any] = Field(description="The standard scalers")

class RGBParams(BaseModel):
    r: float = Field(description="The average of the red RGB value")
    g: float = Field(description="The average of the green RGB value")
    b: float = Field(description="The average of the blue RGB value")

class PredictorFucntionInput(BaseModel):
    """
    Pydantic model for the input of the predictor function.
    """
    rgb_average: RGBParams = Field(description="The average of the RGB values")
    classification_model: Any = Field(description="The classification model")
    classification_scaler: Any = Field(description="The classification scaler")
    prediction_models: dict[int, Any] = Field(description="The prediction models")
    standard_scalers: dict[int, Any] = Field(description="The standard scalers")
    label_decoder: LabelDecoder = Field(description="The label decoder")


class PredictorFunctionOutput(BaseModel):
    """
    Pydantic model for the output of the predictor function.
    """
    contaminant: str = Field(description="The contaminant in the ")
    purity: float = Field(description="The percent composition of Extra Virgin Olive oil in the given sample (purity)")
    contamination: float = Field(description="The percent contamination of the given sample")

