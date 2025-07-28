import joblib
from spectromobi.schema.purity_pipline import ModelLoaderFunctionOutput
from spectromobi import AppConfig

def load_models() -> ModelLoaderFunctionOutput:
    classification_model = joblib.load(AppConfig.CLASSIFIER_MODEL_PATH)
    classification_scaler = joblib.load(AppConfig.CLASSIFIER_SCALER_PATH)

    prediction_models = {
        k: joblib.load(v) for k, v in AppConfig.PREDICTION_MODEL_PATHS.items()
    }

    standard_scalers = {
        k: joblib.load(v) for k, v in AppConfig.STANDARD_SCALER_PATHS.items()
    }

    # return classification_model, classification_scaler, prediction_models, standard_scalers
    output = ModelLoaderFunctionOutput(
        classification_model=classification_model,
        classification_scaler=classification_scaler,
        prediction_models=prediction_models,
        standard_scalers=standard_scalers
    )

    return output
