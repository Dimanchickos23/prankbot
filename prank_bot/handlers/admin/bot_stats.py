from aiogram import Bot, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from prank_bot.db_api.db import get_all_bot_users
from prank_bot.keyboards import admin_markup


async def bot_stat_cb(call: CallbackQuery, state=FSMContext):
    bot = Bot.get_current()
    await call.answer()
    chat_id = call.message.chat.id
    if call.data == 'bot_stat':
        await bot.delete_message(chat_id, message_id=call.message.message_id)
        users = get_all_bot_users()
        await bot.send_message(chat_id, f"<strong>Всего в боте {len(users)} пользователей</strong>", parse_mode='HTML',
                               reply_markup=admin_markup)


def register_bot_stat(dp: Dispatcher):
    dp.register_callback_query_handler(bot_stat_cb, lambda callback_query: callback_query.data == "bot_stat")