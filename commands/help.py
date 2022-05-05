from utils.edit_msg import edit_msg
from utils.emojis import ERROR
from utils.request_url import request
from filters import ForEveryoneRule

from typing import Optional
from vkbottle.user import Blueprint, Message

bp = Blueprint("Help panel")

@bp.on.message(
    ForEveryoneRule("helptext"),
    text=[
        "<prefix>help",
        "<prefix>Команды",
        "<prefix>помощь",
        "<prefix>команды"
    ],
)
async def helptext(message: Message):
    text = (
        f"Команды: \n"
        f"!д <Текст> / <Текст> - Демотиватор на отвеченую фотографию\n"
        f"!дем <Текст> / <Текст> - Демотиватор со свей фотографией\n"
        f"!ачивка <Название> / <Текст> - Создание ачивки из Майнкрафта\n"
        f"!цит - Цитита на отвеченое сообщение\n"
        f"!чб - Превращяет фото в отвеченом сообщении в чёрно-белое\n"
        f"!бомба <Текст> - Взрывает чат/беседу!\n"
        f"!вуф - ВУФНУТЬ\n"
        f"!пнуть @id - Пнуть\n"
        F"!qr <Текст> - Делает из текста QR код\n"
        f"!код <Код Python> - Запускает код, данную команду НЕРЕКОМЕНУЕТСЯ включать для всех, отступы строк <Новая строка/Enter>\n"
        f"!для всех - Посмотреть названия команд"
        f"!пуст - Пустое сообщение\n"
        f"!погода <Город> - Погода в городе\n"
        f"!пинг - Проверка задержки бота\n"
        f"!для всех <Команда> - Выдача команды всем\n"
        f"!конфиг - Конфиг файл\n"
        f"\n\n User bot for community ver 0.3"
    )

    await edit_msg(bp.api, message, text=text)