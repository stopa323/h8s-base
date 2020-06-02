import uvicorn

from fastapi import FastAPI

from base.common.config import get_config
from base.router import pancake


app = FastAPI()
app.include_router(pancake.router, prefix="/v1/pancakes")


@app.on_event("startup")
async def startup():
    pass


if __name__ == "__main__":
    cfg = get_config()
    uvicorn.run(app, host=cfg.get("DEFAULT", "bind_host"),
                port=cfg.getint("DEFAULT", "bind_port"))
