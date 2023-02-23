import datetime

from aiogram import Dispatcher, Bot
from aiogram.types import CallbackQuery

from prank_bot.db_api.db import get_user_balance, get_prem_, remove_prem
from prank_bot.keyboards import get_prem_sub


async def premium_sub_cb(cb: CallbackQuery):
    await cb.answer()
    await cb.message.edit_text("💎ПРЕМИУМ ПОДПИСКА:\n\n"
                                    "- Безлимит на <strong>1 день</strong> на все услуги 🔥\n"
                                    "Успей купить премиум со скидкой всего за <strong>250 руб.❗️</strong>\n",
                           parse_mode='HTML', reply_markup=get_prem_sub())


async def make_premium(cb: CallbackQuery, scheduler):
    await cb.answer()
    bot = Bot.get_current()
    chat_id = cb.message.chat.id
    user_balance = get_user_balance(chat_id)
    if int(user_balance) > int(250):
        get_prem_(chat_id)
        scheduler.add_job(remove_prem, 'date', run_date=datetime.datetime.now() + datetime.timedelta(days=1),
                          kwargs=dict(user_id=chat_id))
        await bot.send_message(chat_id, "Премиум доступ на сутки успешно оформен !")
    else:
        await cb.answer('Не достаточно баланса !', show_alert=True)


def register_premium_sub(dp: Dispatcher):
    dp.register_callback_query_handler(premium_sub_cb, lambda callback_query: callback_query.data == "premium_sub")
    dp.register_callback_query_handler(make_premium, lambda callback_query: callback_query.data == "design_prem")
