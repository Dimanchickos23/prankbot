from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

from prank_bot.db_api.db import get_user_prank_all_title_keyboard

start_markup = InlineKeyboardMarkup(row_width=1,
                                    inline_keyboard=[
                                        [
                                            InlineKeyboardButton(text='🔥Заказать пранк', callback_data='prank_order')
                                        ],
                                        [
                                            InlineKeyboardButton(text='🔊Мои пранки', callback_data='my_pranks')
                                        ],
                                        [
                                            InlineKeyboardButton(text='🏠Личный кабинет', callback_data='my_room')
                                        ],
                                        [
                                            InlineKeyboardButton(text='💎Премиум подписка',
                                                                 callback_data='premium_sub')
                                        ],
                                        [
                                            InlineKeyboardButton(text='⭐️Лучшие пранки',
                                                                 url='https://t.me/PranksBot_86')
                                        ]
                                    ])

admin_start_markup = InlineKeyboardMarkup(row_width=1,
                                          inline_keyboard=[
                                              [
                                                  InlineKeyboardButton(text='🔥Заказать пранк',
                                                                       callback_data='prank_order')
                                              ],
                                              [
                                                  InlineKeyboardButton(text='🔊Мои пранки', callback_data='my_pranks')
                                              ],
                                              [
                                                  InlineKeyboardButton(text='🏠Личный кабинет', callback_data='my_room')
                                              ],
                                              [
                                                  InlineKeyboardButton(text='💎Премиум подписка',
                                                                       callback_data='premium_sub')
                                              ],
                                              [
                                                  InlineKeyboardButton(text='⭐️Лучшие пранки',
                                                                       url='https://t.me/PranksBot_86')
                                              ],
                                              [
                                                  InlineKeyboardButton(text='⚙️Админ-панель',
                                                                       callback_data='admin_menu')
                                              ]
                                          ])

admin_markup = InlineKeyboardMarkup(row_width=1,
                                    inline_keyboard=[
                                        [
                                            InlineKeyboardButton(text='Статистика📊', callback_data='bot_stat')
                                        ],
                                        [
                                            InlineKeyboardButton(text='Сделать рассылку✉️', callback_data='send_bot')
                                        ],
                                        [
                                            InlineKeyboardButton(text='Добавить пранк😁',
                                                                 callback_data="admin_add_prank")
                                        ],
                                        [
                                            InlineKeyboardButton(text='Удалить пранк😩',
                                                                 callback_data="admin_delete_prank")
                                        ],
                                        [
                                            InlineKeyboardButton(text='В главное меню↪️', callback_data='return_')
                                        ]
                                    ]
                                    )


def admin_return_markup():
    markup = InlineKeyboardMarkup(row_width=True)
    markup.add(InlineKeyboardButton(text='Отменить❌', callback_data='send_return'))
    return markup


def get_all_user_pranks(user_id):
    markup = InlineKeyboardMarkup(row_width=True)
    user_all_prank_info = get_user_prank_all_title_keyboard(user_id)
    i = 1
    for title in user_all_prank_info:
        markup.add(InlineKeyboardButton(text=f'{i}.{title[0]}', callback_data=f'user_prank_{i}'))
        i += 1
    markup.add(InlineKeyboardButton(text='🔙Назад', callback_data='return_'))
    return markup


def return_user_prank_keyboard(i):
    markup = InlineKeyboardMarkup(row_width=True)
    markup.row(InlineKeyboardButton(text='⬅️️', callback_data=f'last_prank_{i}'),
               InlineKeyboardButton(text='➡️', callback_data=f'next_prank_{i}'), )
    markup.add(InlineKeyboardButton(text='🔙Назад', callback_data='return_prank_m'))
    return markup


def check_prank_status(numb):
    markup = InlineKeyboardMarkup(row_width=True)
    keyboard_1 = InlineKeyboardButton(text='Получить отчет📥', callback_data=f'get_call_info_{numb}')
    markup.add(keyboard_1)
    return markup


def orerder_prank_1_markup(prank_id):
    markup = InlineKeyboardMarkup(row_width=True)
    markup.add(InlineKeyboardButton(text='📲Отправить', callback_data=f'order_{prank_id}'))
    markup.add(InlineKeyboardButton(text='🔙Назад', callback_data='return_1'))
    return markup


def orerder_prank_user_markup():
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(InlineKeyboardButton(text='📲Отправить', callback_data=f'phone'),
               InlineKeyboardButton(text='🔙Назад', callback_data='return_m'))
    return markup


my_room_markup = InlineKeyboardMarkup(row_width=1,
                                      inline_keyboard=[
                                          [
                                              InlineKeyboardButton(text='💸Пополнить баланс',
                                                                   callback_data='pay_balance')
                                          ],
                                          [
                                              InlineKeyboardButton(text='💳Список платежей', callback_data='pay_list')
                                          ],
                                          [
                                              InlineKeyboardButton(text='👥Реферальная система',
                                                                   callback_data='ref_system')
                                          ],
                                          [
                                              InlineKeyboardButton(text='📙Условия использования',
                                                                   callback_data='terms_of_use')
                                          ],
                                          [
                                              InlineKeyboardButton(text='⛔Сообщить о проблеме', callback_data='help')
                                          ],
                                          [
                                              InlineKeyboardButton(text='🔙Назад', callback_data='return_')
                                          ]
                                      ])


def get_prem_sub():
    markup = InlineKeyboardMarkup(row_width=True)
    markup.add(InlineKeyboardButton(text='💸Оформить премиум', callback_data='design_prem'),
               InlineKeyboardButton(text='🔙Назад', callback_data='return_'))
    return markup


def pay__markup(pay_url):
    markup = InlineKeyboardMarkup(row_width=True)
    markup.add(InlineKeyboardButton(text='Оплатить💵', url=pay_url))
    markup.add(InlineKeyboardButton(text='🔙Назад', callback_data='return_'))
    return markup


def retrun_markup():
    markup = InlineKeyboardMarkup(row_width=True)
    markup.add(InlineKeyboardButton(text='🔙Назад', callback_data='return_'))
    return markup


prank_categories_kb = InlineKeyboardMarkup(row_width=2,
                                           inline_keyboard=[
                                               [
                                                   InlineKeyboardButton(text="🧔‍Именные мужские",
                                                                        callback_data="cat_men_names"),
                                                   InlineKeyboardButton(text="💔Девушка изменяет",
                                                                        callback_data="cat_girl_izmena")
                                               ],
                                               [
                                                   InlineKeyboardButton(text="💂‍От Кавказца",
                                                                        callback_data="cat_from_kavkazec"),
                                                   InlineKeyboardButton(text="👮‍От полиции",
                                                                        callback_data="cat_from_police")
                                               ],
                                               [
                                                   InlineKeyboardButton(text="👱‍Для парней",
                                                                        callback_data="cat_for_men"),
                                                   InlineKeyboardButton(text="👩‍🦳Для девушек",
                                                                        callback_data="cat_for_girls")
                                               ],
                                               [
                                                   InlineKeyboardButton(text="🚙Автомобилистам",
                                                                        callback_data="cat_car_man"),
                                                   InlineKeyboardButton(text="💵Долги/кредиты",
                                                                        callback_data="cat_debts")
                                               ],
                                               [
                                                   InlineKeyboardButton(text="🎓Универ/ школа",
                                                                        callback_data="cat_university"),
                                                   InlineKeyboardButton(text="🚛Доставка", callback_data="cat_delivery")
                                               ],
                                               [
                                                   InlineKeyboardButton(text="👩‍🦳👱‍Именные",
                                                                        callback_data="cat_named"),
                                                   InlineKeyboardButton(text="🔞Секс-шоп(жен)",
                                                                        callback_data="cat_sex_shop")
                                               ],
                                               [
                                                   InlineKeyboardButton(text='🔙Назад', callback_data='return_')
                                               ]
                                           ])

prank_cb = CallbackData("choose_prank", "flag", "category")


def choose_prank_kb(prank_names_ids: list[list[str, int]], category: str, flag=0):
    markup = InlineKeyboardMarkup(row_width=1)
    count = len(prank_names_ids)
    a = flag
    back = a - 6
    next = a + 6
    for i in range(a, 6 + a):
        markup.add(InlineKeyboardButton(text=f"🔸{prank_names_ids[i % count][0]}🔸",
                                        callback_data=f"call_{prank_names_ids[i % count][1]}"))
    markup.row(InlineKeyboardButton(text='⬅️️', callback_data=prank_cb.new(flag=back, category=category)),
               InlineKeyboardButton(text=f'{abs(flag) // 6 + 1}/{count // 6 + 1}', callback_data=f'now_'),
               InlineKeyboardButton(text='➡️', callback_data=prank_cb.new(flag=next, category=category)))
    markup.add(InlineKeyboardButton(text='🔙Назад', callback_data='return_m'))
    return markup
