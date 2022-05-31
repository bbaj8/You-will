import asyncio

from program import LOGS
from pytgcalls import idle
from driver.core import calls, bot, user


async def start_bot():
    await bot.start()
    LOGS.info("[ INFO ] BOT & Songs CLIENT STARTED")
    await calls.start()
    LOGS.info("[ INFO ] PY-TGCALLS CLIENT STARTED")
    await user.join_chat("R125R")
    await user.join_chat("teinthon")
    await idle()
    LOGS.info("[ INFO ] BOT & Songs CLIENT STOPPED")
    await bot.stop()

loop = asyncio.get_event_loop_policy().get_event_loop()
loop.run_until_complete(start_bot())
