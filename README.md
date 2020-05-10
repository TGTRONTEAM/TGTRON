<p align="center">
    <a href="https://github.com/TGTRONTEAM/TGTRON">
        <img src="resources/PicsArt_05-10-11.31.40.jpg" alt="TGTRON">
    </a>
    <br>
    <b>Pluggable Telegram UserBot With Extra Features</b>
    <br>
    
    

# TGTRON 🔥

> **Userge** is a Powerful , _Pluggable_ Telegram UserBot written in _Python_ using [Pyrogram](https://github.com/pyrogram/pyrogram).

## Inspiration 😇

> This project is inspired by the following projects :)

* [tg_userbot](https://github.com/watzon/tg_userbot) ( heavily ) 🤗
* [PyroGramUserBot](https://github.com/SpEcHiDe/PyroGramUserBot)
* [Telegram-Paperplane](https://github.com/RaphielGang/Telegram-Paperplane)
* [UniBorg](https://github.com/SpEcHiDe/UniBorg)

> Special Thanks to all of you !!!.

## Features 😍

* Powerful and Very Useful **built-in** Plugins
  * gdrive ( Team Drives Supported! ) 🤥
  * zip / unzip
  * telegram upload
  * telegram download
  * etc...
* Channel & Group log support
* Database support
* Build-in help support
* Easy to Setup & Use
* Easy to add / port Plugins
* Easy to write modules with the modified client

## Example Plugin 🤨

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/dacadcbabdb74de3903ddae25dc95375)](https://app.codacy.com/gh/UsergeTeam/Userge?utm_source=github.com&utm_medium=referral&utm_content=UsergeTeam/Userge&utm_campaign=Badge_Grade_Dashboard)

```python
from userge import userge, Message

LOG = userge.getLogger(__name__)  # logger object

CHANNEL = userge.getCLogger(__name__)  # channel logger object

@userge.on_cmd("test", about="help text to this command")  # adding handler and help text to .test command
async def testing(message: Message):
   LOG.info("starting test command...")  # log to console

   await message.edit("testing...", del_in=5)  # this will be automatically deleted after 5 sec

   await CHANNEL.log("testing completed!")  # log to channel
```

## Requirements 🥴

* Python 3.6 or Higher 👻
* Telegram [API Keys](https://my.telegram.org/apps)
* Google Drive [API Keys](https://console.developers.google.com/)
* MongoDB [Database URL](https://cloud.mongodb.com/)

## How To Deploy 👷

* **[HEROKU](https://www.heroku.com/) Method** 🔧

  > First click the button below. 

  > If you don't have HU_STRING_SESSION just ignore it.  

  > After Deployed to Heroku first turn off the app (resources -> turn off) and run `bash genStr` in console (more -> run console).  

  > After that copy the string session and past it in Config Vars (settings -> reveal config vars). 

  > Finally turn on the app and check the logs (settings -> view logs) :)

  [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/UsergeTeam/Userge)

* **Other Method** 🔧

  ```bash
  # clone the repo
  git clone https://github.com/UsergeTeam/Userge.git
  cd Userge

  # create virtualenv
  virtualenv -p /usr/bin/python3 venv
  . ./venv/bin/activate

  # install requirements
  pip install -r requirements.txt

  # Create config.env as given config.env.sample and fill that
  cp config.env.sample config.env

  # get string session and add it to config.env
  bash genStr

  # finally run the Userge ;)
  bash run
  ```

* **[More Detailed Guide](https://docs.google.com/document/d/15uoiOn2NkN518MMkx9h5UaMEWMp8aNZqJocXvS0uI6E)** 📝

> TODO: add Docker Support.

### Support & Discussions 👥

> Head over to the [Discussion Group](https://t.me/TGTRONS) and [Update Channel](https://t.me/TGTRON)

### Project Credits 💆‍
)
* [@MARIODEVS](https://t.me/MARIODEVS)
* [@Jr_Genesis](https://t.me/Jr_Jenesis)
* [@Creatorofworld](https://t.me/Creatorofworld)


### Copyright & License 👮

* Copyright (C) 2020 by [TGTRONTEAM](https://github.com/TGTRONTEAM) ❤️️
* Licensed under the terms of the [GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007](https://github.com/TGTRONTEAM/TGTRON/blob/master/LICENSE)
