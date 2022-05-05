from vkbottle.user import Blueprint, Message

from utils.edit_msg import edit_msg
from utils.emojis import ERROR
from filters import ForEveryoneRule

from typing import Optional
import operator
from vkbottle.tools import VoiceMessageUploader

bp = Blueprint("Ben command")

#Пути звуков
SOUND_PATH = "sources/sounds/sound.wav"

@bp.on.message(
    ForEveryoneRule("ben"),
    text=[
        "<prefix>бен <main_text>"#,
        #"<prefix>Бен <main_text>"
    ],
)
async def ben(message: Message,
    main_text: Optional[str] = ""):
    print(main_text)

    #attachment = await VoiceMessageUploader(bp.api).upload("voice.wav",
    #    SOUND_PATH,peer_id=message.peer_id
    #)

    voice_upd = VoiceMessageUploader(bp.api)
    print(message.attachments)

    voice = await voice_upd.upload("sv.wav",SOUND_PATH, peer_id=message.peer_id)
    print(voice)

    print(message.attachments)
    #await edit_msg(bp.api, message, attachment=)
    await message.answer(attachment=voice)
    print("Sended ben")
