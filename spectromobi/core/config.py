from pydantic_settings import BaseSettings
from pathlib import Path


class Settings(BaseSettings):
    app_name: str = "Spectro Mobi"
    project_root: Path = Path(__file__).parent.parent.parent
    app_root: Path = Path(__file__).parent.parent

    CLASSIFIER_MODEL_PATH: Path = project_root / "ml/models/oil_classification_model.pkl"
    CLASSIFIER_SCALER_PATH: Path = project_root / "ml/models/oil_classification_scaler.pkl"

    PREDICTION_MODEL_PATHS: dict[int, Path] = {
        0: project_root / "ml/models/olive_prediction_model.pkl",
        1: project_root / "ml/models/palm_prediction_model.pkl",
        2: project_root / "ml/models/soya_prediction_model.pkl",
    }

    STANDARD_SCALER_PATHS: dict[int, Path] = {
        0: project_root / "ml/models/olive_scaler.pkl",
        1: project_root / "ml/models/palm_scaler.pkl",
        2: project_root / "ml/models/soya_scaler.pkl",
    }

    LABEL_DECODE_TABLE: dict[int, str] = {
        0: "Olive",
        1: "Palm",
        2: "Soya"
    }

AppConfig = Settings()