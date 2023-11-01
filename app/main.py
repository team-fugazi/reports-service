from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Config and Routes
from .core.config import origins, details

# Routes
from .routers.v1.actions import router as actions_v1
from .routers.v1.attachments import router as attachments_v1
from .routers.v1.categories import router as categories_v1
from .routers.v1.comments import router as comments_v1
from .routers.v1.reports import router as reports_v1


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

# Routers
app.include_router(actions_v1, prefix="/v1")
app.include_router(attachments_v1, prefix="/v1")
app.include_router(categories_v1, prefix="/v1")
app.include_router(comments_v1, prefix="/v1")
app.include_router(reports_v1, prefix="/v1")


# Root route
@app.get("/")
def read_root():
    return {"ping": "pong"}