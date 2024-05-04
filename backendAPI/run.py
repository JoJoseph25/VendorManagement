import uvicorn
import logging
from models import *
from fastapi import FastAPI
from configs.config import Config
from routes import configure_routing
from uvicorn.config import LOGGING_CONFIG
from configs.extensions import configure_logging

description = """
FatMug API helps you to create Vendor, PO, and fetch Vendor Trend and other details.

You will be able to:
* **Get Scripts** (GET /scripts/<_clientID_>).
* **Add a Script** (POST /scripts/<_clientID_>).

* **Get Instances** (GET /instances/<_clientID_>).
* **Get Credits Information** (GET /credits/<_clientID_>).
* **Get Billing Information** (GET /bills/<_clientID_>).

"""
tags_metadata = [
    {
        "name": "User",
        "description": "Signup/Login User Info",
    },
    {
        "name": "Vendor",
        "description": "Fetch/Add Vendor Info",
    },
    {
        "name": "PurchaseOrder",
        "description": "Fetch/Create PO",
    },
    {
        "name": "Vendor Metrics",
        "description": "Vendor Metrics",
    },
]

app = FastAPI(
    title="FatMug BackendAPI",
    description=description,
    version="1.0.0",
    openapi_tags=tags_metadata,
    openapi_url=f"{Config.DOCS_URL_PREFIX}/openapi.json",
    docs_url=f"{Config.DOCS_URL_PREFIX}/docs",
    redoc_url=f"{Config.DOCS_URL_PREFIX}/redocs",
)

def configure(app):
    configure_routing(app)
    # add logger to app
    logger = logging.getLogger(__name__)
    app.logger = logger
    return app

# configure the application
app = configure(app)

if __name__ == "__main__":
    uvicorn.run("run:app", host="0.0.0.0", port=5000, reload=True, log_config=configure_logging(LOGGING_CONFIG))


