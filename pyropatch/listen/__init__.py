from pyrogram.types import Update

from .message import *
from .callback import *
from .inline_query import *
from .inline_result import *
import pyrogram
from ..utils import patch2, patchable


async def temp(_: Client, update: Update):
    update.continue_propagation()


@patch2(pyrogram.client.Client)
class Client(Client):
    @patchable
    def __init__(self, *args, **kwargs):
        self.cbd_listeners = {}
        self.msg_listeners = {}
        self.inline_listeners = {}
        self.result_listeners = {}
        self.old2___init__(*args, **kwargs)

    @patchable
    async def start(self, *args, **kwargs):
        self.add_handler(pyrogram.handlers.CallbackQueryHandler(temp))
        self.add_handler(pyrogram.handlers.InlineQueryHandler(temp))
        self.add_handler(pyrogram.handlers.ChosenInlineResultHandler(temp))
        await self.old2_start(*args, **kwargs)
