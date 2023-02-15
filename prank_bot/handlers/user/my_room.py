from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from prank_bot.db_api.db import get_user_pay_list, get_user_balance, get_ref_users, get_user_date, get_vip_status
from prank_bot.keyboards import retrun_markup,  my_room_markup
from prank_bot.misc.states import user_


async def my_room_cb(cb: CallbackQuery):
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


async def pay_balance_cb(cb:CallbackQuery):
    await cb.answer()
    await cb.message.edit_text("<strong>❗️ Укажите сумму пополнения целым числом в рублях.</strong>",
                                 parse_mode='HTML', reply_markup=retrun_markup())
    await user_.pay_.set()


async def pay_list_cb(cb: CallbackQuery):
    await cb.answer()
    await user_.pay_list.set()
    chat_id = cb.message.chat.id
    user_pay_list = get_user_pay_list(chat_id)
    text = '<strong>❗️ Список платежей</strong>\n\n'
    i = 0
    all_price_pay = 0
    for pay_ in user_pay_list:
        all_price_pay += int(pay_[1])
        i += 1
        text += f'<strong>{i}.Дата : {pay_[2]}</strong>\n' \
                f'<i>Сумма : {pay_[1]}р</i>\n\n'
    text += f'<strong>Общая пополненая сумма за все время : {all_price_pay}р</strong>'
    await cb.message.edit_text(text, parse_mode='HTML', reply_markup=retrun_markup())


async def cancel_pay_list(cb: CallbackQuery, state=FSMContext):
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


async def ref_system_cb(cb: CallbackQuery):
    await cb.answer()
    chat_id = cb.message.chat.id
    user_balance = get_user_balance(chat_id)
    user_ref = get_ref_users(chat_id)
    await cb.message.edit_text("<strong>👥 Реферальная сеть</strong>\n\n"
                                 "<strong>Отправь друзьям эту ссылку:</strong>\n"
                                 f"https://t.me/prank_test_bot?start={cb.message.chat.id}\n\n"
                                 "<strong>Получай 20 % от суммы пополнений друзей!</strong>\n"
                                 f"<strong>За все время вы заработали - {user_balance} ₽</strong>\n\n"
                                 f"<strong>Вы пригласили - {user_ref} людей</strong>", parse_mode='HTML',
                                 reply_markup=my_room_markup)


async def terms_of_use_cb(cb:CallbackQuery):
    await cb.answer()
    await cb.message.edit_text("Условия :", reply_markup=my_room_markup)


async def help_cb(cb:CallbackQuery):
    await cb.answer()
    await cb.message.edit_text("Какая проблема ?", reply_markup=my_room_markup)


def register_my_room(dp: Dispatcher):
    dp.register_callback_query_handler(my_room_cb, lambda callback_query: callback_query.data == "my_room")
    dp.register_callback_query_handler(pay_balance_cb, lambda callback_query: callback_query.data == "pay_balance")
    dp.register_callback_query_handler(pay_list_cb, lambda callback_query: callback_query.data == "pay_list")
    dp.register_callback_query_handler(cancel_pay_list,lambda callback_query:callback_query.data == 'return_',
                                       state=user_.pay_list )
    dp.register_callback_query_handler(ref_system_cb, lambda callback_query: callback_query.data == "ref_system")
    dp.register_callback_query_handler(terms_of_use_cb, lambda callback_query: callback_query.data == "terms_of_use")
    dp.register_callback_query_handler(help_cb, lambda callback_query: callback_query.data == "help")