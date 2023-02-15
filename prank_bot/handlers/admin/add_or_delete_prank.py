from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentType, CallbackQuery, Message

from prank_bot.db_api.db import add_prank, delete_prank
from prank_bot.keyboards import admin_markup, prank_categories_kb
from prank_bot.misc.states import admin_func


async def add_prank_cb(cb: CallbackQuery):
    await cb.answer()
    await admin_func.choose_category.set()
    await cb.message.edit_text("Выберите категорию, куда хотите добавить пранк", reply_markup=prank_categories_kb)


async def cancel_add_prank(cb: CallbackQuery, state:FSMContext):
    await cb.answer()
    await state.finish()
    await cb.message.edit_text("Админ-Панель", reply_markup=admin_markup)


async def choose_category(cb: CallbackQuery, state:FSMContext):
    await cb.answer()
    await state.update_data(category = cb.data)
    await admin_func.new_prank.set()
    await cb.message.edit_text("Отправьте мне аудиофайлы с записью пранка. После сохранения всех файлов напишите "
                               "/done, чтобы вернуться в админ панель", reply_markup=None)


async def admin_add_prank(msg: Message, state:FSMContext):
    data = await state.get_data()
    category = data.get("category")[4:]
    prank_audio = msg.audio.file_id
    name = msg.audio.file_name[:-4]
    performer = msg.audio.performer
    if add_prank(prank_audio, name, performer, category):
        await msg.reply("Аудиофайл успешно добавлен в базу данных")
    else:
        await msg.reply("Такой пранк уже есть в базе данных")


async def admin_delete_prank_cb(cb: CallbackQuery):
    await cb.answer()
    await admin_func.delete_prank.set()
    await cb.message.edit_text("Перешлите мне аудиофайлы, которые хотите удалить. После удаления всех файлов "
                               "напишите /done, чтобы вернуться в админ панель")


#всегда отвечает об успехе
async def admin_delete_prank(msg: Message, state:FSMContext):
    name = msg.audio.file_name[:-4]
    delete_prank(name)
    await msg.reply("Аудиофайл успешно удален")


async def finish_delete_or_upload(msg: Message, state:FSMContext):
    await state.finish()
    await msg.answer("Вы вернулись в админ панель", reply_markup=admin_markup)


def register_admin_add_prank(dp:Dispatcher):
    dp.register_callback_query_handler(add_prank_cb, lambda callback_query: callback_query.data == "admin_add_prank")
    dp.register_callback_query_handler(cancel_add_prank, lambda callback_query: callback_query.data == "return_",
                                       state=admin_func.choose_category)
    dp.register_callback_query_handler(admin_delete_prank_cb,
                                       lambda callback_query: callback_query.data == "admin_delete_prank")
    dp.register_callback_query_handler(choose_category, state=admin_func.choose_category)
    dp.register_message_handler(admin_add_prank, content_types=ContentType.AUDIO,state=admin_func.new_prank)
    dp.register_message_handler(admin_delete_prank, content_types=ContentType.AUDIO, state=admin_func.delete_prank)
    dp.register_message_handler(finish_delete_or_upload, commands=['done'], state=admin_func.new_prank)
    dp.register_message_handler(finish_delete_or_upload, commands=['done'], state=admin_func.delete_prank)
