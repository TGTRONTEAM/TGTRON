# Copyright (C) 2020 by UsergeTeam@Github, < https://github.com/TGTRONTEAM>.##
This file is part of < https://github.com/TGTRONTEAM/TGTRON >
project,# and is released under the "GNU v3.0 License Agreement"

from userge import userge, Message
from .. import __all__


@userge.on_cmd("all", about="__list all plugins in plugins/ path__")
async def getplugins(message: Message):
    all_plugins = ['/'.join(i.split('.')) for i in __all__]

    out_str = f"**--({len(__all__)}) Plugins Loaded!--**\n\n"

    for plugin in all_plugins:
        out_str += f"    `{plugin}.py`\n"

    await message.edit(text=out_str, del_in=0)
