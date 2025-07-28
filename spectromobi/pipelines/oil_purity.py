from spectromobi.schema.purity_pipline import OilPurity_Input, PredictorFunctionOutput
from spectromobi.service.prediction import load_models, predict_oil_and_value
import logging
from spectromobi.core.logging import init_logging

def predict_purity(params: OilPurity_Input) -> PredictorFunctionOutput | None:
    pass