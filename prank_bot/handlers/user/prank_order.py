import asyncio

from aiogram import Dispatcher
from aiogram.types import CallbackQuery

from prank_bot.db_api.db import prank_names_id_in_category
from prank_bot.keyboards import prank_categories_kb, choose_prank_kb, prank_cb


async def prank_order_cb(cb: CallbackQuery):
    await cb.answer()
    await cb.message.edit_text("<strong>🔥 Добро пожаловать в Пранк-Бота 🔥</strong>\n\n"
                                 "<strong>Здесь ты можешь разыграть своего друга, заказав угарный аудио звонок на его "
                               "номер телефона 😉</strong>",
                                 parse_mode='HTML', reply_markup=prank_categories_kb)


async def list_pranks_by_categories(cb: CallbackQuery):
    await cb.answer()
    category = cb.data[4:]
    prank_name_id = prank_names_id_in_category(category)
    kb = choose_prank_kb(prank_name_id,category)
    #await asyncio.sleep(0.1)
    await cb.message.edit_text("<strong>☎️ Список аудиозвонков</strong>", parse_mode='HTML',reply_markup=kb)


async def change_page(cb: CallbackQuery, callback_data: dict):
    await cb.answer()
    flag = int(callback_data['flag'])
    category = callback_data['category']
    prank_name_id = prank_names_id_in_category(category)
    if abs(flag) >= len(prank_name_id):
        flag = 0
    kb = choose_prank_kb(prank_name_id,category,flag)
    await asyncio.sleep(0.5)
    await cb.message.edit_text("<strong>☎️ Список аудиозвонков</strong>", parse_mode='HTML',reply_markup=kb)


async def return_to_main_menu(cb: CallbackQuery):
    await cb.answer()
    await cb.message.edit_text("<strong>🔥 Добро пожаловать в Пранк-Бота 🔥</strong>\n\n"
                                                 "<strong>Здесь ты можешь разыграть своего друга, заказав угарный "
                               "аудио звонок на его номер телефона 😉</strong>",
                           parse_mode='HTML',
                           reply_markup=prank_categories_kb)


def register_prank_order(dp: Dispatcher):
    dp.register_callback_query_handler(prank_order_cb, lambda callback_query: callback_query.data == "prank_order")
    dp.register_callback_query_handler(list_pranks_by_categories, lambda callback_query: "cat_" in callback_query.data)
    dp.register_callback_query_handler(change_page, prank_cb.filter())
    dp.register_callback_query_handler(return_to_main_menu, lambda callback_query: callback_query.data == "return_m")
