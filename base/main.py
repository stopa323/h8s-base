import uvicorn

from fastapi import FastAPI

from base.router import pancake


app = FastAPI()
app.include_router(pancake.router, prefix="/v1/pancakes")


@app.on_event("startup")
async def startup():
    pass


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8002)
