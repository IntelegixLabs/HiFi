import uvicorn
from models import Base
from fastapi import FastAPI, Depends
from config.database import engine
from routers.auth import get_user_info
from schemas import *

app = FastAPI()

# Base.metadata.create_all(bind=engine)


@app.get("/healthy")
def health_check():
    return {'status': 'Healthy'}


@app.get("/secure")
async def root(user: User = Depends(get_user_info)):
    return {"message": f"Hello {user.username} you have the following service: {user.realm_roles}"}


if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=5000, reload=True)
