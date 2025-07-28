from pydantic import BaseModel, Field
from pathlib import Path
from spectromobi import AppConfig
import joblib

class ClassificationModel(BaseModel):
    name: str = Field(description="Name of the classification model")
    version: str = Field(description="Version of the classification model")
    path: Path = Field(description="Path to the classification model")

    def load(self):
        """
        Load the classification model from the specified path.
        """
        return joblib.load(self.path)

class RegressionModel(BaseModel):
    name: str = Field(description="Name of the regression model")
    version: str = Field(description="Version of the regression model")
    path: Path = Field(description="Path to the classification model")
    def load(self):
        """
        Load the regression model from the specified path.
        """
        return joblib.load(self.path)


class ClassificationScalars(BaseModel):
    name: str = Field(description="Name of the classification scalers")
    version: str = Field(description="Version of the classification scalers")
    path: Path = Field(description="Path to the classification model")
    def load(self):
        """
        Load the classification scalers from the specified path.
        """
        return joblib.load(self.path)


class StandardScalars(BaseModel):
    name: str = Field(description="Name of the standard scalers")
    version: str = Field(description="Version of the standard scalers")
    path: Path = Field(description="Path to the classification model")

class LabelDecoder(BaseModel):
    decode_table: dict[int, str] = Field(
        default=AppConfig.LABEL_DECODE_TABLE,
        description="Dictionary mapping integar labels to oil types"
    )

    def decoder(self, label: int) -> str:
        """
        Decodes the label to the corresponding oil type.
        """
        return self.decode_table[label]

class PredictionRequest(BaseModel):
    classification_model: ClassificationModel = Field(
        description="Classification model to use for prediction"
    )

    regression_model: RegressionModel = Field(
        description="Regression model to use for prediction"
    )

    classification_scaler: ClassificationScalars = Field(
        description="Classification scaler to use for prediction"
    )

    standard_scalar: StandardScalars = Field(
        description="Standard scaler to use for prediction"
    )


class PredictionResponse(BaseModel):
    oil_type: str = Field(
        description="Predicted oil type based on the input image and classification model"
    )
    purity_value: float = Field(
        description="Predicted EVO value based on the input image and models"
    )
    contamination: float = Field(
        description="Predicted contamination level based on the input image and models"
    )