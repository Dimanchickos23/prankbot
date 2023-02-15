import asyncio

from aiogram import Bot, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery, ContentType


from prank_bot.db_api.db import get_all_bot_users, delete_no_active_user
from prank_bot.keyboards import admin_markup, admin_return_markup
from prank_bot.misc.states import admin_func


async def admin_send_post_start(cb: CallbackQuery):
    bot = Bot.get_current()
    await cb.answer()
    chat_id = cb.message.chat.id
    await bot.delete_message(chat_id, message_id=cb.message.message_id)
    await bot.send_message(chat_id, "Отправьте или перешелите рассылку", reply_markup=admin_return_markup())
    await admin_func.post_.set()


async def admin_send_text(message: Message, state=FSMContext):
    bot = Bot.get_current()
    await state.finish()
    await message.answer("<strong>Рассылка начинается</strong>", parse_mode='HTML')
    users = get_all_bot_users()
    i = 0
    for user in users:
        try:
            await bot.send_message(user[0], message.text, entities=message.entities,
                                   reply_markup=message.reply_markup)
            i += 1
        except:
            delete_no_active_user(user[0])
            await asyncio.sleep(3)
            continue
    await message.answer('<strong>Рассылка успешно завершена !\n\n</strong>'
                         '<strong>Статистика Рассылки📊\n</strong>'
                         f'<i>Отправлено : {i}-пользователям</i>', parse_mode='HTML')


async def admin_send_photo(message: Message, state=FSMContext):
    bot = Bot.get_current()
    await state.finish()
    await message.answer("<strong>Рассылка начинается</strong>", parse_mode='HTML')
    users = get_all_bot_users()
    i = 0
    for user in users:
        try:
            await bot.send_photo(user[0], photo=message.photo[0].file_id, caption=message.caption,
                                 caption_entities=message.entities, reply_markup=message.reply_markup)
            i += 1
        except:
            delete_no_active_user(user[0])
            await asyncio.sleep(3)
            continue
    await message.answer('<strong>Рассылка успешно завершена !\n\n</strong>'
                         '<strong>Статистика Рассылки📊\n</strong>'
                         f'<i>Отправлено : {i}-пользователям</i>', parse_mode='HTML')


async def admin_send_video(message: Message, state=FSMContext):
    bot = Bot.get_current()
    await state.finish()
    await message.answer("<strong>Рассылка начинается</strong>", parse_mode='HTML')
    users = get_all_bot_users()
    i = 0
    for user in users:
        try:
            await bot.send_video(user[0], video=message.video.file_id, caption=message.caption,
                                 caption_entities=message.entities, reply_markup=message.reply_markup)
            i += 1
        except:
            delete_no_active_user(user[0])
            await asyncio.sleep(3)
            continue
    await message.answer('<strong>Рассылка успешно завершена !\n\n</strong>'
                         '<strong>Статистика Рассылки📊\n</strong>'
                         f'<i>Отправлено : {i}-пользователям</i>', parse_mode='HTML')


async def admin_send_animation(message: Message, state=FSMContext):
    bot = Bot.get_current()
    await state.finish()
    await message.answer("<strong>Рассылка начинается</strong>", parse_mode='HTML')
    users = get_all_bot_users()
    i = 0
    for user in users:
        try:
            await bot.send_animation(user[0], animation=message.animation.file_id, caption=message.caption,
                                     caption_entities=message.entities, reply_markup=message.reply_markup)
            i += 1
        except:
            delete_no_active_user(user[0])
            await asyncio.sleep(3)
            continue
    await message.answer('<strong>Рассылка успешно завершена !\n\n</strong>'
                         '<strong>Статистика Рассылки📊\n</strong>'
                         f'<i>Отправлено : {i}-пользователям</i>', parse_mode='HTML')


async def admin_send_voice(message: Message, state=FSMContext):
    bot = Bot.get_current()
    await state.finish()
    await message.answer("<strong>Рассылка начинается</strong>", parse_mode='HTML')
    users = get_all_bot_users()
    i = 0
    for user in users:
        try:
            await bot.send_voice(user[0], voice=message.voice.file_id, caption=message.caption,
                                 caption_entities=message.entities, reply_markup=message.reply_markup)
            i += 1
        except:
            delete_no_active_user(user[0])
            await asyncio.sleep(3)
            continue
    await message.answer('<strong>Рассылка успешно завершена !\n\n</strong>'
                         '<strong>Статистика Рассылки📊\n</strong>'
                         f'<i>Отправлено : {i}-пользователям</i>', parse_mode='HTML')


async def admin_send_audio(message: Message, state=FSMContext):
    bot = Bot.get_current()
    await state.finish()
    await message.answer("<strong>Рассылка начинается</strong>", parse_mode='HTML')
    users = get_all_bot_users()
    i = 0
    for user in users:
        try:
            await bot.send_audio(user[0], audio=message.audio.file_id, caption=message.caption,
                                 caption_entities=message.entities, reply_markup=message.reply_markup)
            i += 1
        except:
            delete_no_active_user(user[0])
            await asyncio.sleep(3)
            continue
    await message.answer('<strong>Рассылка успешно завершена !\n\n</strong>'
                         '<strong>Статистика Рассылки📊\n</strong>'
                         f'<i>Отправлено : {i}-пользователям</i>', parse_mode='HTML')


async def admin_cancel_post(call: CallbackQuery, state=FSMContext):
    bot = Bot.get_current()
    chat_id = call.message.chat.id
    await bot.delete_message(chat_id, message_id=call.message.message_id)
    await state.finish()
    await bot.send_message(chat_id, "Рассылка отменена !", reply_markup=admin_markup)


def register_admin_send_post(dp: Dispatcher):
    dp.register_callback_query_handler(admin_send_post_start, lambda callback_query: callback_query.data == "send_bot" )
    dp.register_message_handler(admin_send_text, state=admin_func.post_, content_types=ContentType.TEXT)
    dp.register_message_handler(admin_send_photo, state=admin_func.post_, content_types=ContentType.PHOTO)
    dp.register_message_handler(admin_send_video, state=admin_func.post_, content_types=ContentType.VIDEO)
    dp.register_message_handler(admin_send_animation, state=admin_func.post_, content_types=ContentType.ANIMATION)
    dp.register_message_handler(admin_send_voice, state=admin_func.post_, content_types=ContentType.VOICE)
    dp.register_message_handler(admin_send_audio, state=admin_func.post_, content_types=ContentType.AUDIO)
    dp.register_callback_query_handler(admin_cancel_post, state=admin_func.post_)
