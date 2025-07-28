import uvicorn
from spectromobi.core.logging import init_logging
from spectromobi.app import app  # adjust to your app location

if __name__ == "__main__":
    init_logging()
    uvicorn.run(
        app=app,  # "module_name:app_instance"
        host="127.0.0.1",
        port=8000,
    )
