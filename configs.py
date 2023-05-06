from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "API_ID"))
    API_HASH = getenv("API_HASH", "API_HASH")
    BOT_TOKEN = getenv("BOT_TOKEN", "BOT_TOKEN")
    CHID = int(getenv("CHID", "CHID"))
    SUDO = list(map(int, getenv("SUDO").split()))
    MONGO_URI = getenv("MONGO_URI", "MONGO_URI")
    LOGCHID = int(getenv("LOGCHID", "LOGCHID"))
    API = getenv("API", "API")
cfg = Config()
