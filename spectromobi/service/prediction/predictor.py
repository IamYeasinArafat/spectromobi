import pandas as pd
from typing import Tuple
from spectromobi import AppConfig
from spectromobi.schema.purity_pipline import PredictorFunctionOutput, PredictorFucntionInput

def predict_oil_and_value(
    params: PredictorFucntionInput
) -> PredictorFunctionOutput:
    r = params.rgb_average.r
    g = params.rgb_average.g
    b = params.rgb_average.b
    
    input_df = pd.DataFrame([[r, g, b]], columns=['R', 'G', 'B'])

    # Classification stage
    scaled_class = params.classification_scaler.transform(input_df)
    scaled_class_df = pd.DataFrame(scaled_class, columns=['R', 'G', 'B'])
    oil_class: int = params.classification_model.predict(scaled_class_df)[0]

    # Prediction stage
    scaler = params.standard_scalers[oil_class]
    scaled_pred = scaler.transform(input_df)
    scaled_pred_df = pd.DataFrame(scaled_pred, columns=['R', 'G', 'B'])
    
    purity_value: float = params.prediction_models[oil_class].predict(scaled_pred_df)[0]
    oil_type: str = PredictorFucntionInput.label_decoder.decoder(label=oil_class)

    return PredictorFunctionOutput(
        purity=purity_value,
        contaminant=oil_type,
        contamination=100-purity_value
    )
