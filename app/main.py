from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# Config and Routes
from .core.config import origins, details

# Routes
# from .routers.router_v1 import router as services_v1

# User Model
class User(BaseModel):
    id: int
    name: str
    email: str

app = FastAPI(
    title=details["title"],
    description=details["description"],
    version=details["version"],
    contact=details["contact"],
)

# Add CORS to app
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Root route
@app.get("/")
def read_root():
    return {"ping": "pong"}

# random dict


# demo route
@app.get("/demo")
def read_demo() -> list[User]:
    users = [
        {
            "id": 1,
            "name": "John Doe",
            "email": "john@doe.com"
        },
        {
            "id": 2,
            "name": "Jane Doe",
            "email": "jane@doe.com"
        },
    ]

    return users

# Routers
# app.include_router(services_v1, prefix="/v1")