"""
Команда, которая генерирует бомбу на время заданное в конфиге
"""
import json
import asyncio
from vkbottle.user import Blueprint, Message
from utils.edit_msg import edit_msg
from filters import ForEveryoneRule


bp = Blueprint("Bomb generator")


@bp.on.message(ForEveryoneRule("bomb"), text="<prefix>бомба <text>")
async def bomb(message: Message, text):

    with open("config.json", "r", encoding="utf-8") as file:
        config = json.load(file)
        bomb_time = config["bomb_time"]

    if message.from_id == int(config["user_id"]):
        bomb_id = message.id
    else:
        bomb_id = await message.answer("абоба")

    for second in range(bomb_time, 0, -1):
        await edit_msg(
            bp.api,
            message,
            (
                f"{text}\n\nДанное сообщение взорвется через {second} секунд! "
                "&#128163;"
            ),
            mode="bomb",
            bomb_id=bomb_id
        )
        await asyncio.sleep(1.0)
    await edit_msg(
        bp.api,
        message,
        "БУМ! Взрывная беседа!! &#128165;&#128165;",
        bomb_id=bomb_id
    )
