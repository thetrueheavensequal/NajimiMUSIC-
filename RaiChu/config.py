## Coder are here

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BQBHoDY7PWmxdK_dgFGCcC3SwC8Sn-8_0_Q7iw3xLwoSyS60wNqtlxsyHbf81xLnXY8WORrX5ZdvfRRklJaAAMnaDjfTJ8y0xeanYHUWWP7oCDED-c8TFqQPqX0-vG130qdz0kjtsmNLGRzmhUKgXLZZWVNTv32hR3ggnDdZGywWhnImLCRh0phdm5GXqHhq7kPuygOrvp1BN-gN6CLyRE9YJvdMs55IWmcG_sZvnTO6bCVd_YKHM_SK0OY50SzPoJCsRZMEa_14ZbUX6DgBChJgYIiMTcJxtxlyUupz7HFQivJwuPztXUUJ1kjRhP6e8-sPDfoSi0g5CPJrXZ11o4XXAAAAAVZcvoYA")
BOT_TOKEN = getenv("BOT_TOKEN", "5862886147:AAFZK2fqZpiPI1MDavK0cX_3m2obo0fIsx4")
BOT_NAME = getenv("BOT_NAME", "Najimi")
API_ID = int(getenv("API_ID", "21927988"))
API_HASH = getenv("API_HASH", "e18f720acdff1e5b0ec80616aecd8a5a")
OWNER_NAME = getenv("OWNER_NAME", "plumblossomsword")
ALIVE_NAME = getenv("ALIVE_NAME", "Najimi")
ASSISTANT_USERNAME = getenv("ASSISTANT_USERNAME", "theYoRHa2B")
BOT_USERNAME = getenv("BOT_USERNAME", "NajimiMusicBot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "2B")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "theoneandonlymurim")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "RimuruBots")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "2064735436").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/65137f9aee29fdc129c1b.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/thetrueheavensequal/NajimiMUSIC-")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/c3401a572375b569138c3.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/d8f8fc1de9110b93ca94c.jpg")
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL", "https://telegra.ph/file/58da23d726b601dc3b18e.jpg")
