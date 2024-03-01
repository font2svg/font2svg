from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from yuanfen import Logger, SuccessResponse

logger = Logger()


@asynccontextmanager
async def lifespan(_: FastAPI):
    logger.info("api service started")
    yield
    logger.info("api service stopped")


app = FastAPI(lifespan=lifespan)


@app.get("/health")
def health_check():
    return SuccessResponse()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
