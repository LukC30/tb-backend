from fastapi import FastAPI
import uvicorn
import logging

from app.core.lifespan import lifespan
from app.modules.users.routes import user_router
from app.modules.auth.routes import auth_router

app = FastAPI(
    title="tb-backend",
    description="para a tigre branco :)",
    lifespan=lifespan
)

app.include_router(user_router)
app.include_router(auth_router)

@app.get('/')
def test_route():
    return {"message" : 'vrumvrummmm'}

if __name__ == "__main__":
    logging.info("[INFO][Starting application]...")
    uvicorn.run(app)