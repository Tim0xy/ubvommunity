"""
Команда, которая показывает, что бот работает
"""
from time import time
import json
import platform
import psutil

from vkbottle.bot import Blueprint, Message
from utils.edit_msg import edit_msg
from filters import ForEveryoneRule


bp = Blueprint("Ping-pong command")


@bp.on.message(ForEveryoneRule("ping"), text="<prefix>пинг")
async def ping_handler(message: Message):
 
    start = time()
    with open("config.json", "r", encoding="utf-8") as file:
        content = json.load(file)

    if content["debug"] is not True:
        end = time()
        result = round(end - start, 4)
        await edit_msg(
            bp.api,
            message,
            f"&#127955; | Понг!\n&#9201; | Ответ за {result} секунд",
        )
    else:
        try:
            cpu = str(psutil.cpu_percent()) + "%"
        except PermissionError:
            cpu = "не известно (android?)"

        system_name = platform.system()

        """
        Если бот запущен на ОС Windows 11, то platform.release()
        вернет 10, что бы этого избежать, можно сделать проверку
        на версию системы:
        """
        if system_name == "Windows":
            if int(platform.version().split(".")[2]) > 20000:
                system_version = "11"
            else:
                system_version = platform.release()
        else:
            system_version = platform.release()

        system = system_name + " " + system_version
        with open("time_started.txt", "r", encoding="utf-8") as file:
            work_hours = round((round(time()) - int(file.read())) / 3600, 4)
        work_days = work_hours // 24
        end = time()
        result = round(end - start, 4)
        await edit_msg(
            bp.api, message,
            f"&#127955; | Понг!\n&#9201; | Ответ за {result} секунд (debug)\n"
            f"&#128187; | ОС: {system}\n"
            f"&#128295; | Процессор: {cpu}\n"
            f"&#9881; | Работает {work_hours} часов ({work_days} дней)\n"
            "&#10084; | Работает за счет 0xy gen"
        )
