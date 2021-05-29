HEROKU = True  # NOTE Make it false if you're not deploying on heroku.

if HEROKU:
    from os import environ

    BOT_TOKEN = environ.get("BOT_TOKEN", None)
    API_ID = int(environ.get("API_ID", 6))
    API_HASH = environ.get("API_HASH", "eb06d4abfb49dc3eeb1aeb98ae0f581e")
    SESSION_STRING = environ.get("SESSION_STRING", None)
    USERBOT_PREFIX = environ.get("USERBOT_PREFIX", None)
    SUDO_USERS_ID = list(
        int(x) for x in environ.get("SUDO_USERS_ID", "").split()
    )
    LOG_GROUP_ID = int(environ.get("LOG_GROUP_ID", None))
    GBAN_LOG_GROUP_ID = int(environ.get("GBAN_LOG_GROUP_ID", None))
    MESSAGE_DUMP_CHAT = int(environ.get("MESSAGE_DUMP_CHAT", None))
    FERNET_ENCRYPTION_KEY = environ.get("FERNET_ENCRYPTION_KEY", None)
    WELCOME_DELAY_KICK_SEC = int(environ.get("WELCOME_DELAY_KICK_SEC", None))
    MONGO_DB_URI = environ.get("MONGO_DB_URI", None)
    ARQ_API_URL = environ.get("ARQ_API_URL", None)
    ARQ_API_KEY = environ.get("ARQ_API_KEY", None)
    LOG_MENTIONS = (
        True if int(environ.get("LOG_MENTIONS", None)) == 1 else False
    )
else:
    BOT_TOKEN = "1846522668:AAFNHX5XhHCSLRSH_0eTowW54zfKaHIzjAo"
    API_ID = 5749052
    API_HASH = "b730db07c712aaa6f492dad18d64f822"
    USERBOT_PREFIX = "."
    PHONE_NUMBER = "+573223715340"  # Need for Helper Userbot
    SUDO_USERS_ID = [
        863388285,
        1184867988,
    ]  # Sudo users have full access to everythin, don't trust anyone
    LOG_GROUP_ID = -1417568413
    GBAN_LOG_GROUP_ID = -1417568413
    MESSAGE_DUMP_CHAT = -1244731698
    FERNET_ENCRYPTION_KEY = (
        "iKMq0WZMnJKjMQxZWKtv-cplMuF_LoyshXj0XbTGGWM="  # Leave this as it is
    )
    WELCOME_DELAY_KICK_SEC = 300
    MONGO_DB_URI = "mongodb+srv://BL:Scarlet@vcpb.fedpa.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    ARQ_API_KEY = "QPRMRX-GUEZZC-RHKSFC-KOIDLU-ARQ"
    ARQ_API_URL = "http://thearq.tech"
    LOG_MENTIONS = True
