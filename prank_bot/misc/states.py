from aiogram.dispatcher.filters.state import StatesGroup, State


class user_(StatesGroup):
    pay_ = State()
    order_call = State()
    my_pranks = State()
    pay_list = State()


class admin_func(StatesGroup):
    post_ = State()
    new_prank = State()
    choose_category = State()
    delete_prank = State()
