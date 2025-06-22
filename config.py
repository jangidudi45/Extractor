# --------------M----------------------------------

import os
from os import getenv
# ---------------R---------------------------------
API_ID = int(os.environ.get("25586552", ""))
# ------------------------------------------------
API_HASH = os.environ.get("f265cba9d76dc6ad70914accbe758f47", "")
# ----------------D--------------------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
# -----------------A-------------------------------
BOT_USERNAME = os.environ.get("@thetxtextractorbot")
# ------------------X------------------------------
OWNER_ID = int(os.environ.get("1368753935", ""))
# ------------------X------------------------------

SUDO_USERS = list(map(int, getenv("7062964338", "").split()))
# ------------------------------------------------
CHANNEL_ID = int(os.environ.get("-1001948647139", "-100"))
# ------------------------------------------------
MONGO_URL = os.environ.get("mongodb+srv://jangidudit45:Gautam5257@cluster0.s8fbcy9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", "mongodb+srvter")
# -----------------------------------------------
PREMIUM_LOGS = int(os.environ.get("-1002521082833", "-100"))

