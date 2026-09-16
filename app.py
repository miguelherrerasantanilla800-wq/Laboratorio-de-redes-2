import fastapi
import requests
from routers import auth, questions, answers

app = fastapi.FastAPI()

# Include routers
app.include_router(auth.router)
app.include_router(questions.router)
app.include_router(answers.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}
