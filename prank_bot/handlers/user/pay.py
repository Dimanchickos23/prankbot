import asyncio

from aiogram import Bot, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Regexp
from aiogram.types import Message, CallbackQuery

from prank_bot.db_api.db import get_user_date, get_user_balance, get_ref_users, get_vip_status
from prank_bot.keyboards import pay__markup, retrun_markup, my_room_markup
from prank_bot.misc.pay_ import cheack_payment, create_payment
from prank_bot.misc.states import user_


async def start_pay(cb: CallbackQuery):
    await cb.answer()
    await cb.message.edit_text("<strong>❗️ Укажите сумму пополнения целым числом в рублях.</strong>",
                                 parse_mode='HTML', reply_markup=retrun_markup())
    await user_.pay_.set()


async def nice_user_pay(message: Message, state=FSMContext):
    chat_id = message.chat.id
    bot = Bot.get_current()
    await state.finish()
    create_info = create_payment(message.text, message)
    pay_url = create_info['confirmation']['confirmation_url']
    pay_values = create_info['amount']['value']
    await bot.send_message(chat_id, "<strong>💳 Пополнение баланса</strong>\n\n"
                                        f"<strong>💰 Сумма пополнения: {pay_values}р</strong>\n", parse_mode='HTML',
                               reply_markup=pay__markup(pay_url))
    await asyncio.sleep(1)
    loop = asyncio.get_event_loop()
    loop.create_task(cheack_payment(chat_id, bot))



async def wrong_user_pay(message: Message, state=FSMContext):
    chat_id = message.chat.id
    bot = Bot.get_current()
    await bot.send_message(chat_id, "<strong>❗️ Укажите сумму пополнения целым числом в рублях.</strong>",
                           parse_mode='HTML', reply_markup=retrun_markup())
    await user_.pay_.set()


async def user_pay_call(call: CallbackQuery, state=FSMContext):
    await call.answer()
    await state.finish()
    chat_id = call.message.chat.id
    d_time = get_user_date(chat_id)
    user_balance = get_user_balance(chat_id)
    user_ref = get_ref_users(chat_id)
    vip_check = get_vip_status(chat_id)
    if vip_check == True:
        await call.message.edit_text("<strong>🧑🏻‍💻 Кабинет </strong>\n\n"
                                     f"<strong>🆔 Ваш ID: </strong><i>{call.message.chat.id}</i>\n"
                                     f"<strong>📅 Дата регистрации: {d_time[:19]} </strong>\n"
                                     f"<strong>💰 Ваш баланс: {user_balance} RUB </strong>\n"
                                     f"<strong>👥 Рефералов приглашено: {user_ref} </strong>\n"
                                     "<strong>💎 Премиум статус: Активный </strong>\n", parse_mode='HTML',
                                     reply_markup=my_room_markup)
    else:
        await call.message.edit_text("<strong>🧑🏻‍💻 Кабинет </strong>\n\n"
                                     f"<strong>🆔 Ваш ID: </strong><i>{call.message.chat.id}</i>\n"
                                     f"<strong>📅 Дата регистрации: {d_time[:19]} </strong>\n"
                                     f"<strong>💰 Ваш баланс: {user_balance} RUB </strong>\n"
                                     f"<strong>👥 Рефералов приглашено: {user_ref} </strong>\n"
                                     "<strong>💎 Премиум статус: Неактивен </strong>\n", parse_mode='HTML',
                                     reply_markup=my_room_markup)


async def cancel_pay(cb: CallbackQuery, state=FSMContext):
    await state.finish()
    await cb.answer()
    chat_id = cb.message.chat.id
    d_time = get_user_date(chat_id)
    user_balance = get_user_balance(chat_id)
    user_ref = get_ref_users(chat_id)
    vip_check = get_vip_status(chat_id)
    if vip_check == True:
        await cb.message.edit_text("<strong>🧑🏻‍💻 Кабинет </strong>\n\n"
                                   f"<strong>🆔 Ваш ID: </strong><i>{cb.message.chat.id}</i>\n"
                                   f"<strong>📅 Дата регистрации: {d_time[:19]} </strong>\n"
                                   f"<strong>💰 Ваш баланс: {user_balance} RUB </strong>\n"
                                   f"<strong>👥 Рефералов приглашено: {user_ref} </strong>\n"
                                   "<strong>💎 Премиум статус: Активный </strong>\n", parse_mode='HTML',
                                   reply_markup=my_room_markup)
    else:
        await cb.message.edit_text("<strong>🧑🏻‍💻 Кабинет </strong>\n\n"
                                   f"<strong>🆔 Ваш ID: </strong><i>{cb.message.chat.id}</i>\n"
                                   f"<strong>📅 Дата регистрации: {d_time[:19]} </strong>\n"
                                   f"<strong>💰 Ваш баланс: {user_balance} RUB </strong>\n"
                                   f"<strong>👥 Рефералов приглашено: {user_ref} </strong>\n"
                                   "<strong>💎 Премиум статус: Неактивен </strong>\n", parse_mode='HTML',
                                   reply_markup=my_room_markup)


def register_user_pay(dp: Dispatcher):
    dp.register_callback_query_handler(start_pay, lambda callback_query: callback_query.data == "pay_balance")
    dp.register_message_handler(nice_user_pay, Regexp(r'^\d+$'), state=user_.pay_)
    dp.register_message_handler(wrong_user_pay, state=user_.pay_)
    dp.register_callback_query_handler(user_pay_call, state=user_.pay_)
    dp.register_callback_query_handler(cancel_pay, lambda callback_query:callback_query.data == "return_", state=user_.pay_)