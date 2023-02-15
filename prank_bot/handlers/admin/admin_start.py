from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery

from prank_bot.keyboards import admin_markup, admin_start_markup


async def admin_start_message(message: Message):
    await message.answer("<strong>🔥 Добро пожаловать в Пранк-Бота 🔥</strong>\n\n"
                         "<strong>Здесь ты можешь разыграть своего друга, заказав угарный аудио звонок "
                         "на его номер телефона 😉</strong>",
                         parse_mode='HTML', reply_markup=admin_start_markup)


async def admin_menu(cb: CallbackQuery):
    await cb.message.edit_text("Админ-Панель", reply_markup=admin_markup)


def register_admin_start(dp: Dispatcher):
    dp.register_message_handler(admin_start_message, commands=['start'], is_admin=True)
    dp.register_callback_query_handler(admin_menu, lambda callback_query: callback_query.data == "admin_menu")
