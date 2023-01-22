## Coder are here

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BQB4zr4dUyDCBXWKOFInGKa0QaEcPNm52hTN3YP9Uoa22g3qj3ht5R8TK___NlZ7WtS43PyFPp3AqermGEPZoMPI5Y8giJVeJrJMp-3QjjrYHshkvsWaF9cB0RAm2mBOU0PKOmJy5fxgklIJXbXFVwOYV5mJC9dXYQNA_gwCG5VwrfeLm5-Db5N2bL1fZUTJfUstWoNeFobuYHv0leetgGZ5npNALT-4Tp3CGPJ86FRDZtCNz7_OLvBCC35wrUw_JaupxlnmplakAu4ioQ-Zzj3Qo_2dRYeZQ-UjLapyYEsdz0pjDy63GBtY4UNOC2mo019bJJksr5cvoxbiDnTdqpTvAAAAAVZcvoYA")
BOT_TOKEN = getenv("BOT_TOKEN", "5862886147:AAF7INyrdbnesEcXtjn7AWhK02eoTtgJF84")
BOT_NAME = getenv("BOT_NAME", "Osana Najimi")
API_ID = int(getenv("API_ID", 24833791))
API_HASH = getenv("API_HASH", "42488cb247a33d13d5f97d6839c8e52b")
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
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/AMANTYA1/RaiChu-MusicV2")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/c3401a572375b569138c3.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/d8f8fc1de9110b93ca94c.jpg")
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL", "https://telegra.ph/file/58da23d726b601dc3b18e.jpg")
