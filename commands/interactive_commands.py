"""
Roleplay commands (!me, !бросить кактус, etc.)
"""
from vkbottle.user import Blueprint, Message

from utils.edit_msg import edit_msg
from utils.emojis import ERROR
from filters import ForEveryoneRule

from random import randint

bp = Blueprint("Interactive commands")


class Interactive:
    def __init__(
        self, api, message: Message, split_to: int, name_case: str = "acc"
    ):
        self.api = api
        self.message = message
        self.split_to = split_to
        self.name_case = name_case

    async def get_my_name(self) -> str:
        """
        Returns first name and last name
        """
        response = await self.api.users.get(
            user_ids=self.message.from_id, fields="first_name,last_name"
        )
        return (
            f"{response[0].first_name} {response[0].last_name}"
        )

    async def get_target_name(self) -> str:
        """
        322615766 -> [id322615766|Тимур Богданов]
        """
        if len(self.message.text.split()) > self.split_to:
            mention = self.message.text.split()[self.split_to]
            if mention.startswith("["):
                who = mention.split("|")[0][1:].replace(
                    "id", ""
                )
                response = await self.api.users.get(
                    user_ids=who,
                    fields="first_name,last_name",
                    name_case=self.name_case,
                )
                return (
                    "[id"
                    f"{who}|{response[0].first_name} {response[0].last_name}"
                    "]"
                )

            else:
                await edit_msg(
                    bp.api,
                    self.message,
                    text=(
                        f"{ERROR} | Вы написали не упоминание, а какую ту "
                        "чушь!"
                    )
                )

        elif self.message.reply_message is not None:
            who = self.message.reply_message.from_id
            response = await self.api.users.get(
                user_ids=who,
                fields="first_name,last_name",
                name_case=self.name_case,
            )
            return (
                f"[id{who}|{response[0].first_name} {response[0].last_name}]"
            )

        else:
            await edit_msg(
                bp.api,
                self.message,
                text=f"{ERROR} | Вы не ответили никому!",
            )


@bp.on.message(
    ForEveryoneRule("interactive_commands"), text="<prefix>me <action>"
)
async def me_handler(message: Message, action):
    """
    > !me съел суши
    > Тимур Богданов съел суши 💬
    """
    who = await bp.api.users.get(user_ids=message.from_id)
    name = who[0].first_name
    last_name = who[0].last_name
    await edit_msg(
        bp.api, message, text=f"{name} {last_name} {action} &#128172;"
    )


@bp.on.message(
    ForEveryoneRule("interactive_commands"),
    text=["<prefix>бонкнуть", "<prefix>пнуть <mention>"],
)
async def bonk_handler(message: Message):
    """
    > !бонкнуть @vcirnik
    > Тимур Богданов бонкнул Влада Сырника 🧹
    """
    interactive = Interactive(bp.api, message, 1)
    await edit_msg(
        bp.api,
        message,
        text=(
            f"{await interactive.get_my_name()} пнул "
            f"{await interactive.get_target_name()} &#129529;"
        )
    )


@bp.on.message(
    ForEveryoneRule("interactive_commands"),
    text=["<prefix>вуф"],
)
async def cactus_handler(message: Message):

    interactive = Interactive(bp.api, message, 2)
    await edit_msg(
        bp.api,
        message,
        text=(
            f"{await interactive.get_my_name()} ВУФНУЛ!!!"
        )
    )


@bp.on.message(
    ForEveryoneRule("interactive_commands"),
    text=["<prefix>кости <mention>"],
)
async def bonk_handler(message: Message):

    interactive = Interactive(bp.api, message, 1)
    await edit_msg(
        bp.api,
        message,
        text=(
            f"{await interactive.get_my_name()} пнул "
            f"{await interactive.get_target_name()} &#129529;"
        )
    )
