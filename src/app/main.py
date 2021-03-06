import logging

import uvicorn
from fastapi import FastAPI

from app.api import ping, reservations
from app.db import init_db

log = logging.getLogger(__name__)


def create_application() -> FastAPI:
    application = FastAPI()
    application.router.redirect_slashes = False
    application.include_router(ping.router)
    application.include_router(reservations.router, prefix="/reservations", tags=["reservations"])

    return application


app = create_application()


@app.on_event("startup")
async def startup_event():
    log.info("Starting up...")
    init_db(app)


@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down...")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
