# Copyright (C) 2020 by UsergeTeam@Github, < https://github.com/UsergeTeam >.
#
# This file is part of < https://github.com/UsergeTeam/Userge > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/uaudith/Userge/blob/master/LICENSE >
#
# All rights reserved.


from userge import userge, Message


@userge.on_cmd("logs", about="__check userge logs__")
async def check_logs(message: Message):
    """check logs"""
    await message.edit("`checking logs ...`")
    with open("./logs/TGTRON.log", "r") as l_f:
        await message.edit_or_send_as_file(
            l_f.read(), filename='TGTRON.log', caption='TGTRON.log')
