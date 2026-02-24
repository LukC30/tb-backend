from fastapi import FastAPI
import uvicorn
import logging

app = FastAPI(
    title="tb-backend",
    description="para a tigre branco :)",
    
)

@app.get('/')
def test_route():
    return {"message" : 'vrumvrummmm'}

if __name__ == "__main__":
    #TODO, fazer o gerenciamento do lifespan do app
    logging.info("[INFO][Starting application]...")
    uvicorn.run(app)