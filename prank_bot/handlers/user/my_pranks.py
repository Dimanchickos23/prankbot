from aiogram import Dispatcher, Bot
from aiogram.types import CallbackQuery

from prank_bot.db_api.db import get_max_user_prank_prank_title, get_max_user_prank_number, \
    get_max_user_prank_result_audio, \
    get_max_user_prank_numb
from prank_bot.keyboards import get_all_user_pranks, return_user_prank_keyboard


async def my_pranks_cb(cb: CallbackQuery):
    await cb.answer()
    chat_id = cb.message.chat.id
    await cb.message.edit_text("<strong>🔊 Здесь вы можете прослушать аудиозаписи пранков.</strong>",
                               parse_mode='HTML',
                               reply_markup=get_all_user_pranks(chat_id))


async def return_prank_menu_cb(cb: CallbackQuery):
    await cb.message.edit_text("<strong>🔊 Здесь вы можете прослушать аудиозаписи пранков.</strong>",
                               parse_mode='HTML',
                               reply_markup=get_all_user_pranks(cb.message.chat.id))


async def user_prank_cb(cb: CallbackQuery):
    await cb.answer()
    bot = Bot.get_current()
    chat_id = cb.message.chat.id
    await cb.answer()
    await cb.message.delete()
    prank_numb_ = cb.data[11:]
    prank_title = get_max_user_prank_prank_title(chat_id, prank_numb_)
    prank_user_number = get_max_user_prank_number(chat_id, prank_numb_)
    prank_user_audio_result = get_max_user_prank_result_audio(chat_id, prank_numb_)
    await bot.send_message(chat_id, f"<strong>Информация о пранке : {prank_numb_}</strong>\n\n"
                                    f"<i>Назвние пранка </i>: <code>{prank_title}</code>\n\n"
                                    f"<i>Номер </i>: <code>{prank_user_number}</code>\n\n"
                                    f"<a href='{prank_user_audio_result}'>Запись диалога</a>",
                           parse_mode='HTML', reply_markup=return_user_prank_keyboard(prank_numb_))


async def next_prank_cb(cb: CallbackQuery):
    await cb.answer()
    prank_numb_ = cb.data[11:]
    chat_id = cb.message.chat.id
    bot = Bot.get_current()
    user_max_numb = get_max_user_prank_numb(chat_id)
    next_prank_numb = int(prank_numb_) + int(1)
    if int(next_prank_numb) > int(user_max_numb):
        await cb.answer('Это ваш последний совершенный пранк !', show_alert=True)
    else:
        await cb.message.edit_reply_markup()
        prank_title = get_max_user_prank_prank_title(chat_id, next_prank_numb)
        prank_user_number = get_max_user_prank_number(chat_id, next_prank_numb)
        prank_user_audio_result = get_max_user_prank_result_audio(chat_id, next_prank_numb)
        await bot.send_message(chat_id, f"<strong>Информация о пранке : {next_prank_numb}</strong>\n\n"
                                        f"<i>Назвние пранка </i>: <code>{prank_title}</code>\n\n"
                                        f"<i>Номер </i>: <code>{prank_user_number}</code>\n\n"
                                        f"<a href='{prank_user_audio_result}'>Запись диалога</a>",
                               parse_mode='HTML', reply_markup=return_user_prank_keyboard(next_prank_numb))


async def last_prank_cb(cb: CallbackQuery):
    await cb.answer()
    chat_id = cb.message.chat.id
    bot = Bot.get_current()
    await cb.message.edit_reply_markup()
    prank_numb_ = cb.data[11:]
    prank_ = int(prank_numb_) - int(1)
    if int(prank_) == int(0):
        await cb.answer('Вы на первой странице!', show_alert=True)
        prank_title = get_max_user_prank_prank_title(chat_id, int(1))
        prank_user_number = get_max_user_prank_number(chat_id, int(1))
        prank_user_audio_result = get_max_user_prank_result_audio(chat_id, int(1))
        await bot.send_message(chat_id, f"<strong>Информация о пранке : {int(1)}</strong>\n\n"
                                        f"<i>Назвние пранка </i>: <code>{prank_title}</code>\n\n"
                                        f"<i>Номер </i>: <code>{prank_user_number}</code>\n\n"
                                        f"<a href='{prank_user_audio_result}'>Запись диалога</a>",
                               parse_mode='HTML', reply_markup=return_user_prank_keyboard(prank_))
    else:
        prank_title = get_max_user_prank_prank_title(chat_id, prank_)
        prank_user_number = get_max_user_prank_number(chat_id, prank_)
        prank_user_audio_result = get_max_user_prank_result_audio(chat_id, prank_)
        await bot.send_message(chat_id, f"<strong>Информация о пранке : {prank_}</strong>\n\n"
                                        f"<i>Назвние пранка </i>: <code>{prank_title}</code>\n\n"
                                        f"<i>Номер </i>: <code>{prank_user_number}</code>\n\n"
                                        f"<a href='{prank_user_audio_result}'>Запись диалога</a>",
                               parse_mode='HTML', reply_markup=return_user_prank_keyboard(prank_))


def register_my_pranks(dp: Dispatcher):
    dp.register_callback_query_handler(my_pranks_cb, lambda callback_query: callback_query.data == "my_pranks")
    dp.register_callback_query_handler(user_prank_cb, lambda callback_query: 'user_prank_' in callback_query.data)
    dp.register_callback_query_handler(return_prank_menu_cb,
                                       lambda callback_query: callback_query.data == "return_prank_m")
    dp.register_callback_query_handler(next_prank_cb, lambda callback_query: 'next_prank_' in callback_query.data)
    dp.register_callback_query_handler(last_prank_cb, lambda callback_query: 'last_prank_' in callback_query.data)
