from aiogram import Bot, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery

from prank_bot.db_api.db import add_ref_user, add_user
from prank_bot.keyboards import start_markup


async def start_message(message: Message, state=FSMContext):
    bot = Bot.get_current()
    chat_id = message.chat.id
    if message.text[7:]:
        add_ref_user(message, message.text[7:])
        await bot.send_message(chat_id, "<strong>🔥 Добро пожаловать в Пранк-Бота 🔥</strong>\n\n"
                                        "<strong>Здесь ты можешь разыграть своего друга, заказав угарный аудио звонок "
                                        "на его номер телефона 😉</strong>",
                               parse_mode='HTML', reply_markup=start_markup)
    else:
        add_user(message)
        await bot.send_message(chat_id, "<strong>🔥 Добро пожаловать в Пранк-Бота 🔥</strong>\n\n"
                                        "<strong>Здесь ты можешь разыграть своего друга, заказав угарный аудио звонок "
                                        "на его номер телефона 😉</strong>",
                               parse_mode='HTML', reply_markup=start_markup)


async def return_cb(cb: CallbackQuery):
    await cb.answer()
    await cb.message.edit_text("<strong>🔥 Добро пожаловать в Пранк-Бота 🔥</strong>\n\n"
                                 "<strong>Здесь ты можешь разыграть своего друга, заказав угарный аудио звонок на его номер телефона 😉</strong>",
                                 parse_mode='HTML', reply_markup=start_markup)


def register_start_menu(dp: Dispatcher):
    dp.register_message_handler(start_message, commands=['start'])
    dp.register_callback_query_handler(return_cb, lambda callback_query: callback_query.data == 'return_')