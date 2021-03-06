"""
Upgrade user bot vk+ by Timur Bogdanov
update by 0xy group
"""
import json
import os
import logging
from time import time

from vkbottle import User, load_blueprints_from_package
from middlewares.has_prefix_middleware import HasPrefixMiddleware


if not os.path.exists('output'):
    os.mkdir('output')

with open("config.json", "r", encoding="utf-8") as file:
    content = json.load(file)

logging.basicConfig(
    level=("DEBUG" if content["debug"] is True else "INFO")
)

bot = User()# TODO: доделать запуск токена из content
for bp in load_blueprints_from_package("commands"):
    bp.load(bot)
bot.labeler.message_view.register_middleware(HasPrefixMiddleware)

with open("time_started.txt", "w", encoding="utf-8") as file:
    file.write(str(round(time())))

bot.run_forever()
