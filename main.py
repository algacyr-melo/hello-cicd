from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Ola, Mundo! Forcando rebuild da imagem pra testar o workflow"}

