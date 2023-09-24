from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "13305226"))
    API_HASH = getenv("API_HASH", "8cde2475d6b0cb1162b89ebbac71a95d")
    BOT_TOKEN = getenv("BOT_TOKEN", "5088998402:AAGMWFsZfCSsW6IAMxuWuK2WGWPNqAQPQrM")
    FSUB = getenv("FSUB", "wmteams")
    CHID = int(getenv("CHID", "-1001651905628"))
    SUDO = list(map(int, getenv("SUDO").split(1258310642)))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://v:v@cluster0.zznxusa.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()
