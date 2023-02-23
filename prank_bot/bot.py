import asyncio
import logging

from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from apscheduler.jobstores.redis import RedisJobStore
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler_di import ContextSchedulerDecorator

from prank_bot.bot_commands import force_reset_all_commands, set_restart_command
from prank_bot.config import load_config
from prank_bot.filters.admin import AdminFilter
from prank_bot.handlers.admin.add_or_delete_prank import register_admin_add_prank
from prank_bot.handlers.admin.admin_send_post import register_admin_send_post
from prank_bot.handlers.admin.admin_start import register_admin_start
from prank_bot.handlers.admin.bot_stats import register_bot_stat
from prank_bot.handlers.user.my_pranks import register_my_pranks
from prank_bot.handlers.user.my_room import register_my_room
from prank_bot.handlers.user.order_call import register_order_call
from prank_bot.handlers.user.pay import register_user_pay
from prank_bot.handlers.user.prank_order import register_prank_order
from prank_bot.handlers.user.premium_sub import register_premium_sub
from prank_bot.handlers.user.start_menu import register_start_menu
import sentry_sdk

from prank_bot.middlewares.scheduler import SchedulerMiddleware

sentry_sdk.init(
    dsn="https://87544813cc664aa297084b1b8910fd37@o4504680945025024.ingest.sentry.io/4504680950464512",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)


logger = logging.getLogger(__name__)


def register_all_filters(dp):
    dp.filters_factory.bind(AdminFilter)


def register_admin(dp):
    register_admin_start(dp)
    register_admin_send_post(dp)
    register_bot_stat(dp)
    register_admin_add_prank(dp)


def register_user(dp):
    register_start_menu(dp)
    register_prank_order(dp)
    register_my_pranks(dp)
    register_my_room(dp)
    register_premium_sub(dp)
    register_user_pay(dp)
    register_order_call(dp)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    logger.info("Starting bot")
    config = load_config(".env")

    # Чтобы работал Redis brew services start/stop/restart redis

    storage = RedisStorage2() if config.tg_bot.use_redis else MemoryStorage()
    bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp = Dispatcher(bot, storage=storage)

    job_stores = {
        "default": RedisJobStore(db=2,
            jobs_key="dispatched_trips_jobs", run_times_key="dispatched_trips_running",
            # параметры host и port необязательны, для примера показано как передавать параметры подключения
            # host="localhost", port=6379
            # , password=config.tg_bot.redis_password
            # host="redis_cache", port=6379, password=config.tg_bot.redis_password
        )
    }

    scheduler = AsyncIOScheduler(jobstores=job_stores)

    bot['config'] = config

    dp.setup_middleware(SchedulerMiddleware(scheduler))

    register_all_filters(dp)

    register_admin(dp)
    register_user(dp)

    await force_reset_all_commands(bot)
    await set_restart_command(bot)

    # start
    try:
        scheduler.start()
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()
        scheduler.shutdown()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")

# @dp.message_handler(commands=["test"])
# async def start_message(message: types.Message, state=FSMContext):
#     chat_id = message.chat.id
#     # await asyncio.create_task(check_user_prank(chat_id))
#     loop = asyncio.get_event_loop()
#     loop.create_task(cheack_payment(chat_id, bot))
#
#
# @dp.callback_query_handler()
# async def callback_message(call: types.CallbackQuery, state=FSMContext):
#     await call.answer()
#     chat_id = call.message.chat.id
#
#     if call.data.startswith('get_call_info_'):
#         await bot.send_message(chat_id, "Получения Информации..")
#         numb = call.data[14:]
#         # check__ = check_(numb)
#         loop = asyncio.get_event_loop()
#         loop.create_task(check_user_prank(chat_id))
