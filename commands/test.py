from utils.edit_msg import edit_msg
from utils.emojis import ERROR
from utils.request_url import request
from filters import ForEveryoneRule

from typing import Optional
from PIL import Image, ImageFont, ImageDraw, ImageOps
from vkbottle.tools import PhotoMessageUploader
from vkbottle.user import Blueprint, Message
import operator

bp = Blueprint("Testing")


DEM_PATH = "sources/demotivators/"
DEM_FONT = ImageFont.truetype(DEM_PATH + "TNR.ttf", 70)
DEM_FONT_SEC = ImageFont.truetype(DEM_PATH + "TNR.ttf", 40)

@bp.on.message(
    ForEveryoneRule("test"),
    text=[
        "prefix>ст <first_text>/<second_text>",
        "<prefix>ст <first_text>",
        "<prefix>ст /<second_text>",
    ],
)

async def testing(message: Message,
    first_text: Optional[str] = "",
    second_text: Optional[str] = ""):
    a = message.reply_message.attachments[0].sticker.images
    z = []
    for i in a:
        z.append({"url": i.url, "width": i.width})
    z.sort(key=operator.itemgetter("width"))
    print(z[len(z)-1]["url"])

    file = z[len(z)-1]["url"]

    photo_bytes = await request(file)

    with open("usfolder/t_dem.png", "wb") as file:
        file.write(photo_bytes)

    size=(609,517)
    original = Image.open(DEM_PATH + "demotivator.png").convert("RGBA")
    to_paste = Image.open("usfolder/t_dem.png").convert("RGBA")
    draw = ImageDraw.Draw(original)
    out = to_paste.resize(size,resample=2, box=None)

    original.paste(out, (75, 45))

    photo_width = original.size[0]
    text_width = draw.textsize(first_text, font=DEM_FONT)[0]
    second_text_width = draw.textsize(second_text, font=DEM_FONT_SEC)[0]

    # First text
    draw.text(
        ((photo_width - text_width) / 2, 575),
        first_text,
        font=DEM_FONT,
        fill="white",
    )

    # Second text
    draw.text(
        ((photo_width - second_text_width) / 2, 650),
        second_text,
        font=DEM_FONT_SEC,
        fill="white",
    )

    # Saving and uploading image
    original.save("output/t_final.png")
    attachment = await PhotoMessageUploader(bp.api).upload(
        "output/t_final.png", peer_id=message.peer_id
    )
    await edit_msg(bp.api, message, attachment=attachment)
