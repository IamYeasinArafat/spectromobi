import logging
from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from spectromobi.core.logging import init_logging
from pydantic import ValidationError
from spectromobi.schema.prediction import PredictionRequest, PredictionResponse

init_logging()
logger = logging.getLogger("spectromobi.api")

router = APIRouter(prefix="/v1")

@router.post("/get-oil-prediction")
async def get_prediction(
    image: UploadFile = File(...),
    params: str = Form(...)
):
    # Parse the JSON string 'params' into PredictionRequest model
    try:
        prediction_params = PredictionRequest.model_validate_json(json_data=params)
    except ValidationError as ve:
        raise HTTPException(
            status_code=422,
            detail=ve.errors()
          )    
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid JSON parameters: {e}")

    # You can now process the image and prediction_params
    # e.g., read image bytes
    image_bytes = await image.read()

    # Log or process prediction
    # (replace with your real logic)
    logger.info("Received image and params for prediction")

    # Return dummy response for now
    return PredictionResponse(
        oil_type="Oil",
        purity_value=42.0,
        contamination=0.1
    )

