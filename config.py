import os
from os import getenv
from dotenv import load_dotenv

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AgApdH3O3ZZn6Prh_2HM1JCkrcSqCqIYl83xnMGMsKXC4TWppxoL7VyfKwaeIBtyvshYgDjNqOqrkdPwUa6siWHD4AaMRZkJ5H7wJPAjFg3kTtQh333WTkys9F_znNjctHrinw6OspG3JlSUR1fwIsjUhH0pa6YWGTPL33YklufFsHqx3S2oYulBmLboJVP7DfUf72EOWC1nDct9saicYML_PNOGCn1IUFIn5UFQ_igWvgmzgdOkl6kisAeVsswaSjYqWC570amIfq6U09IOHaDBNOd86E6GUcu7dKhh6bvXia3YlAoBSVjoeEC-NeUssIXP206y4Ce1UMDQ27VCfnleAAAAAS_SqegA")
BOT_TOKEN = getenv("BOT_TOKEN", "5380301524:AAFPJHk2lPG9K4eAQeEgOGuWl6t8wC4tMPU")
BOT_NAME = getenv("BOT_NAME", "πΎπΆπΉπ³π« π΄πΌπΊπ°πͺ πΛ£")
API_ID = int(getenv("API_ID")
API_HASH = getenv("API_HASH", "3c852e55d6ef31f7acd8e4a666465e07")
MONGODB_URL = getenv("MONGODB_URL", "mongodb://mongo:Sourceworled@cluster0.gn7l7.mongodb.net/?retryWrites=true&w=majority")
OWNER_NAME = getenv("OWNER_NAME", "WORLD_MUSIC_F")
ALIVE_NAME = getenv("ALIVE_NAME", "πΎπΆπΉπ³π« π΄πΌπΊπ°πͺ πΛ£")
BOT_PHOTO = getenv("BOT_PHOTO", "https://telegra.ph/file/a6c96cdbd066ca2388d06.jpg")
DEV_PHOTO = getenv("DEV_PHOTO", "https://telegra.ph/file/a6c96cdbd066ca2388d06.jpg")
DEV_NAME = getenv("DEV_NAME", "WORLD_MUSIC_F")
BOT_USERNAME = getenv("BOT_USERNAME", "WorldMusicly_Bot")
UPSTREAM_REPO = getenv("UPSTREAM_REPO")
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "World_Musicly")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "Gr_World_Music")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Ch_World_Music")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1491415522 1419419100 2112059230").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . Ψͺ Ω Ψ§ ΨΊ Ψ³ Ψ΄ Ω S").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/9c497543705d61530039b.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "900"))
UPSTREAM_REPO = getenv("https://github.com/USDDBOOT/Shadow")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/d08d6474628be7571f013.png")
