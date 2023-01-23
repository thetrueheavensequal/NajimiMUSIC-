## Coder are here

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BQBWrTm8QHIAYRaSFTiEQxycP-Y8iV1kSRmDjfosKH8JOsiNbNqUGAGTmY-a3S832A4vlHcH-xnsPlQZABiSy4c32a2KjvCoYOPcyF21GgdopkIv9gN3IDUf4GRXn4yzTSzjtXBodtnJv9-i6ACw3snISDVDLV6gLCY1O6NZnFvEmNgGwap5ABWPQDmtnq962jS6eB1YOy1DbOShCYpNbBN_uTQvP7voRZBt4fZ_KyaFnZw5JyuQAsMpcH0EUnKccrtwAhAz_ZMS4qRymhsRkZkRwRJXDTgLGS2tnhYtrgQwu1OyeEK6dI8fm5zAOOUGcST49B2F6-iD3HS16EElsVjBAAAAAVZcvoYA")
BOT_TOKEN = getenv("BOT_TOKEN", "5801306815:AAFZBlAsczrlebLcLQUXTQbmSqVFzzkGWCU")
BOT_NAME = getenv("BOT_NAME", "TEST")
API_ID = int(getenv("API_ID", "21927988"))
API_HASH = getenv("API_HASH", "e18f720acdff1e5b0ec80616aecd8a5a")
OWNER_NAME = getenv("OWNER_NAME", "plumblossomsword")
ALIVE_NAME = getenv("ALIVE_NAME", "Anna")
ASSISTANT_USERNAME = getenv("ASSISTANT_USERNAME", "theYoRHa2B")
BOT_USERNAME = getenv("BOT_USERNAME", "AnnahNishikinomiyaBot")
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
