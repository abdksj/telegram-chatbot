
from pyrogram import Client, filters
import random

api_id = 22984152
api_hash = "c7109bc2ffd1390e5b36f1ac94e111d3"
bot_token = "7994756864:AAGV8DVtCfjeCSwK_M5QwH_OilC3ah7cENM"

app = Client("abod_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# قائمة ردود عشوائية باللهجة اليمنية
replies = [
    "مشغول دحين، رجع لي بعدين، أو خلِّك محترم بس.",
    "ايوه قد شفت رسالتك، مالك مستعجل؟",
    "ههههه ومالك وقلبي؟ من فين ظهرت؟",
    "حياك يا زعيم، بس أنا مشغول شوية.",
    "ما فهمتش عليك، وضّح كلامك يا عمّي.",
    "هاه، قول بسرعه قبل ما اطفي النت!",
    "قوّك الله، ايش المطلوب يا طيّب؟"
]

@app.on_message(filters.private & filters.incoming)
def auto_reply(client, message):
    message.reply(random.choice(replies))

app.run()
