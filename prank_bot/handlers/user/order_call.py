import asyncio

from aiogram import Bot, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Regexp
from aiogram.types import CallbackQuery, Message

from prank_bot.db_api.db import add_numb_info, get_vip_status,add_user_numb_prank, \
    get_user_prank_id, \
    get_user_prank_title, get_user_prank_numb, check_take_user_prank_money, get_prank_text_info, get_prank_audio_info
from prank_bot.keyboards import retrun_markup, orerder_prank_user_markup, prank_categories_kb, orerder_prank_1_markup
from prank_bot.misc.callink import call_ncreate_call
from prank_bot.misc.prank_checker import check_user_prank
from prank_bot.misc.states import user_


async def order_call_info(cb: CallbackQuery):
    await cb.answer()
    bot = Bot.get_current()
    chat_id = cb.message.chat.id
    await bot.delete_message(chat_id, message_id=cb.message.message_id)
    prank_id = cb.data[5:]
    print(prank_id)
    prank_info = get_prank_text_info(prank_id)
    prank_audio = get_prank_audio_info(prank_id)
    await bot.send_voice(chat_id, voice=prank_audio, caption=prank_info,
                         reply_markup=orerder_prank_1_markup(prank_id))
    await user_.order_call.set()


async def cancel_order_call(cb: CallbackQuery, state: FSMContext):
    await state.finish()
    await cb.answer()
    bot = Bot.get_current()
    await bot.delete_message(cb.message.chat.id, message_id=cb.message.message_id)
    await bot.send_message(cb.message.chat.id, "<strong>🔥 Добро пожаловать в Пранк-Бота 🔥</strong>\n\n"
                                               "<strong>Здесь ты можешь разыграть своего друга, заказав угарный аудио "
                                               "звонок на его "
                                               "номер телефона 😉</strong>",
                           parse_mode='HTML', reply_markup=prank_categories_kb)


# starts with order
async def order_call_start(cb: CallbackQuery, state: FSMContext):
    await cb.answer()
    bot = Bot.get_current()
    await bot.delete_message(cb.message.chat.id, message_id=cb.message.message_id)
    prank_id = cb.data[6:]
    add_numb_info(cb.message, prank_id)
    await bot.send_message(cb.message.chat.id, "🎙 Заказать пранк\n\n"
                                               "❗ Введите номер телефона для отправки,\n       как в примере:"
                                               " <b>89991234567</b>", reply_markup=retrun_markup())


async def call_user_order_confirm(message: Message, state=FSMContext):
    bot = Bot.get_current()
    chat_id = message.chat.id
    # "📲 Звонок поступит с номера: <code>79210191999</code>\n\n"
    await state.finish()
    status = get_vip_status(chat_id)
    # user_pay = get_user_vip_procent(25)
    if status != False:
        add_user_numb_prank(message)
        user_prank_id = get_user_prank_id(chat_id)
        prank_title = get_prank_text_info(user_prank_id)
        await bot.send_message(chat_id, "Название пранка: \n"
                                        f"<code>{prank_title}</code>\n"
                                        "🇷🇺 Номер получателя: \n"
                                        f"<code>{message.text}</code>\n"
                                        f"💸 С Вашего баланса будет списано: <code>0</code> RUB\n\n"
                                        "<strong>Отправить?</strong>\n"
                                        "<strong>❗️ВАЖНО❗</strong>️При соединении с <strong>автоответчиком, "
                                        "оператор</strong> всё равно <strong>списывает с нас оплату</strong> "
                                        "<i>(и за звонок, и за его запись)</i>, поэтому в таком случае, увы,<strong> "
                                        "вернуть оплату мы не сможем 😕</strong>\n "
                                        "Нажимая на кнопку <strong>«Отправить»</strong> вы подтверждаете, "
                                        "что ознакомились и согласны с этим правилом ❗️",
                               parse_mode='HTML', reply_markup=orerder_prank_user_markup())
    else:
        add_user_numb_prank(message)
        user_prank_id = get_user_prank_id(chat_id)
        prank_title = get_user_prank_title(user_prank_id)
        await bot.send_message(chat_id, "Название пранка: \n"
                                        f"<code>{prank_title}</code>\n"
                                        "🇷🇺 Номер получателя: \n"
                                        f"<code>{message.text}</code>\n"
                                        f"💸 С Вашего баланса будет списано: <code>30</code> RUB\n\n"
                                        "<strong>Отправить?</strong>\n"
                                        "<strong>❗️ВАЖНО❗</strong>️При соединении с <strong>автоответчиком, "
                                        "оператор</strong> всё равно <strong>списывает с нас оплату</strong> "
                                        "<i>(и за звонок, и за его запись)</i>, поэтому в таком случае, увы,"
                                        "<strong> вернуть оплату мы не сможем 😕</strong>\n "
                                        "Нажимая на кнопку <strong>«Отправить»</strong> вы подтверждаете, "
                                        "что ознакомились и согласны с этим правилом ❗️",
                               parse_mode='HTML', reply_markup=orerder_prank_user_markup())


async def call_user_order_error(message: Message, state: FSMContext):
    chat_id = message.chat.id
    bot = Bot.get_current()
    await bot.send_message(chat_id, "🎙 Заказать пранк\n\n"
                                    "❗ Введите номер телефона для отправки,\nкак в примере:"
                                    " <b>89991234567</b>", reply_markup=retrun_markup())
    await user_.order_call.set()


async def cancel_call_user_order(call: CallbackQuery, state=FSMContext):
    await call.answer()
    await state.finish()
    await call.message.edit_text("<strong>🔥 Добро пожаловать в Пранк-Бота 🔥</strong>\n\n"
                                 "<strong>Здесь ты можешь разыграть своего друга, заказав угарный аудио звонок на его "
                                 "номер телефона 😉</strong>",
                                 parse_mode='HTML', reply_markup=prank_categories_kb)


async def call_user_send(cb: CallbackQuery, state: FSMContext):
    await cb.answer()
    bot = Bot.get_current()
    chat_id = cb.message.chat.id
    await bot.delete_message(chat_id, message_id=cb.message.message_id)
    take_prank_m = check_take_user_prank_money(chat_id)
    if take_prank_m != False:
        prank_numb = get_user_prank_numb(chat_id)
        prank_campaign_id = get_user_prank_id(chat_id)
        await bot.send_message(chat_id, '<strong>Звонок будет совершен в ближайщее время</strong>\n\n'
                                        '<i>Статус</i>:<code> В процессе</code>', parse_mode='HTML')
        call_ncreate_call(prank_campaign_id, prank_numb)
        await asyncio.sleep(2)
        loop = asyncio.get_event_loop()
        loop.create_task(check_user_prank(chat_id))
    else:
        await cb.answer('На вашем аккаунте не достаточно баланса!', show_alert=True)


def register_order_call(dp: Dispatcher):
    dp.register_callback_query_handler(order_call_info, lambda callback_query: "call_" in callback_query.data)
    dp.register_callback_query_handler(cancel_order_call, lambda callback_query: callback_query.data == "return_1",
                                       state=user_.order_call)
    dp.register_callback_query_handler(order_call_start, lambda callback_query: "order_" in callback_query.data,
                                       state=user_.order_call)
    dp.register_message_handler(call_user_order_confirm, Regexp(r"^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?["
                                                                r"0-9]{4,6}$"), state=user_.order_call)
    dp.register_message_handler(call_user_order_error, state=user_.order_call)
    dp.register_callback_query_handler(cancel_call_user_order, state=user_.order_call)
    dp.register_callback_query_handler(call_user_send, lambda callback_query: callback_query.data == "phone")
