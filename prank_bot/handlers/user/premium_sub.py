from aiogram import Dispatcher, Bot
from aiogram.types import CallbackQuery

from prank_bot.db_api.db import get_user_balance, get_prem_
from prank_bot.keyboards import get_prem_sub


async def premium_sub_cb(cb: CallbackQuery):
    await cb.answer()
    await cb.message.edit_text("💎ПРЕМИУМ ПОДПИСКА:\n\n"
                                    "- Скидка <strong>30%</strong> на все услуги 🔥\n"
                                    "Успей купить премиум со скидкой всего за <strong>299 руб/мес.❗️</strong>\n",
                           parse_mode='HTML', reply_markup=get_prem_sub())


async def make_premium(cb: CallbackQuery):
    await cb.answer()
    bot = Bot.get_current()
    chat_id = cb.message.chat.id
    user_balance = get_user_balance(chat_id)
    if int(user_balance) > int(299):
        get_prem_(chat_id)
        await bot.send_message(chat_id, "Премиум доступ успешно оформен !")
    else:
        await cb.answer('Не достаточно баланса !', show_alert=True)


def register_premium_sub(dp: Dispatcher):
    dp.register_callback_query_handler(premium_sub_cb, lambda callback_query: callback_query.data == "premium_sub")
    dp.register_callback_query_handler(make_premium, lambda callback_query: callback_query.data == "design_prem")
