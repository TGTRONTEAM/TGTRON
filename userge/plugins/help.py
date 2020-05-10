# Copyright (C) 2020 by UsergeTeam@Github, < https://github.com/UsergeTeam >.
#
# # Copyright (C) 2020 by TGTRONTEAM@Github, < https://github.com/TGTRONTEAM >.
## This file is part of < https://github.com/TGTRONTEAM/TGTRON> project,# and is released under the "GNU v3.0 License Agreement".
## All rights reserved.



from userge import userge, Message


@userge.on_cmd("help", about="__to know how to use **TGTRON** commands__")
async def helpme(message: Message):
    out, is_mdl_or_key = userge.get_help(message.input_str)
    cmd = message.input_str

    if not out:
        out_str = "__No Module or Command Found!__"

    elif isinstance(out, str):
        out_str = f"`{is_mdl_or_key}`\n\n{out}"

    elif isinstance(out, list) and is_mdl_or_key:
        out_str = f"""**--Which module you want TGTRON?--**

**Usage**:

    `.help [module_name]`

**Hint**:

    use `.s` for search commands.
    ex: `.s wel`

**({len(out)}) Modules Available:**\n\n"""

        for i in out:
            out_str += f"`{i}`    "

    elif isinstance(out, list) and not is_mdl_or_key:
        out_str = f"""**--Which command you want TGTRON?--**

**Usage**:

    `.help .[command_name]`

**Hint**:

    use `.s` for search commands.
    ex: `.s wel`

**({len(out)}) Commands Available Under `{cmd}` Module:**\n\n"""

        for i in out:
            out_str += f"`{i}`    "

    await message.edit(text=out_str, del_in=0)
