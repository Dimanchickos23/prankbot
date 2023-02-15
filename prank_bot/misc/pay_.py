import asyncio
import json


from yookassa import Configuration, Payment

from prank_bot import config
from prank_bot.config import load_config
from prank_bot.db_api.db import add_pay_info, add_user_pay_info, add_user_price, get_pay__pay_id
from prank_bot.keyboards import my_room_markup


Configuration.account_id = load_config(".env").pay_api.shop_id
Configuration.secret_key = load_config(".env").pay_api.token


def create_payment(value, message):
    payment = Payment.create({
        "amount": {
            "value": value,
            "currency": "RUB"
        },
        "payment_method_data": {
            "type": "bank_card"
        },
        "confirmation": {
            "type": "redirect",
            "return_url": "https://t.me/funny_prank_bot"
        },
        "capture": True,
        "description": 'Оплата'
    })
    s_info = json.loads(payment.json())
    add_pay_info(message, s_info['id'])
    return json.loads(payment.json())


# def check_payment(payment_id,user_id):
# 	payment = json.loads((Payment.find_one(payment_id)).json())
# 	if payment['status'] == 'succeeded':
# 		print("SUCCSESS RETURN")
# 		print(payment)
# 		add_user_pay_info(user_id,payment)
# 		return True
# 	else:
# 		print("BAD RETURN")
# 		print(payment)
# 		return False
async def cheack_payment(chat_id, bot):
    pay_ment_id = get_pay__pay_id(chat_id)
    while True:
        await asyncio.sleep(1)
        payment = json.loads((Payment.find_one(pay_ment_id)).json())
        pay_values = payment['amount']['value']
        if payment['status'] == 'succeeded':
            add_user_pay_info(chat_id, payment)
            add_user_price(chat_id, pay_values)
            await bot.send_message(chat_id, f"<strong>Ваш аккаунт успешно пополнен на {pay_values}р!</strong>\n",
                                   parse_mode='HTML', reply_markup=my_room_markup)
            break
        if payment['status'] == 'canceled':
            await bot.send_message(chat_id, "Время на оплату истекла !\n"
                                            "Платеж не выполнен !")
            break
        else:
            continue
