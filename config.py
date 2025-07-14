import os

class Config:
    MONGO_URI = os.environ.get("MONGO_URI") or "mongodb://localhost:27017/diet_planner"
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev")
