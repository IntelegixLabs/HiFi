import uvicorn
from models import Base
from fastapi import FastAPI, Depends, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from config.database import engine
from routers.auth import get_user_info
from schemas import userPayload
from routers import userProfile

app = FastAPI()

# Define CORS settings
origins = ["*"]  # Allow requests from any origin

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "PATCH"],
    allow_headers=["*"],
)


Base.metadata.create_all(bind=engine)


@app.get("/healthy")
def health_check():
    return {'status': 'Healthy'}


@app.get("/secure")
async def root(user: userPayload = Depends(get_user_info)):
    return {"message": f"Hello {user.username} you have the following service: {user.realm_roles}"}


app.include_router(userProfile.router)

if __name__ == '__main__':
    uvicorn.run("main:app", host="localhost", port=5000, reload=True)
