from fastapi import FastAPI

from app.routers import users, documents, tags

app = FastAPI(
    title="InsightHub API",
    description="API for managing users, documents and tags",
    version="1.0.0",
    debug=True,
)


# Register application routers.
app.include_router(users.router)
app.include_router(documents.router)
app.include_router(tags.router)


@app.get("/")
def root():
    return {"message": "Welcome to InsightHub API"}
