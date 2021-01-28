from os import path,getenv
from dotenv import load_dotenv


if path.isfile(".env"):
    load_dotenv(verbose=True)

MONGODB_URI = getenv("MONGO_DB_URI")