import sqlite3
from datetime import datetime

from aiogram import Bot

database = sqlite3.connect("/Users/dmitryklimenko/PycharmProjects/prankbot/prank_bot/db_api/db.sqlite")
cursor = database.cursor()


# admin_func
def get_all_bot_users():
    users = cursor.execute("SELECT id FROM Users").fetchall()
    return users


# admin_func
def delete_no_active_user(user_id):
    cursor.execute("DELETE FROM Users WHERE id=?", (user_id,))
    database.commit()


def get_max_user_pay_info_numb(user_id):
    cursor.execute("SELECT MAX(numb) FROM user_pay_info WHERE id=?", (user_id,))
    max_numb = cursor.fetchone()[0]
    return max_numb


def add_user_pay_info(user_id, info):
    cursor.execute("SELECT id FROM user_pay_info WHERE id=?", (user_id,))
    user = cursor.fetchone()
    if user is None:
        cursor.execute("INSERT INTO user_pay_info VALUES(?,?,?,?)",
                       (user_id, info['amount']['value'], info['created_at'], int(1),))
        database.commit()
    else:
        numb = get_max_user_pay_info_numb(user_id)
        numb += int(1)
        cursor.execute("INSERT INTO user_pay_info VALUES(?,?,?,?)",
                       (user_id, info['amount']['value'], info['created_at'], numb,))

        database.commit()


def get_user_pay_list(user_id):
    cursor.execute("SELECT * FROM user_pay_info WHERE id=?", (user_id,))
    user_pay_list = cursor.fetchall()
    return user_pay_list


def add_pay_info(message, pay_id):
    cursor.execute("SELECT id FROM pay_ WHERE id=?", (message.chat.id,))
    user = cursor.fetchone()
    if user is None:
        cursor.execute("INSERT INTO pay_ VALUES(?,?,?)", (message.chat.id, pay_id, int(message.text)))
        database.commit()
    else:
        cursor.execute("UPDATE pay_ SET pay_id=? WHERE id=?", (pay_id, message.chat.id,))
        cursor.execute("UPDATE pay_ SET price=? WHERE id=?", (int(message.text), message.chat.id,))
        database.commit()


def get_pay__pay_id(user_id):
    cursor.execute("SELECT pay_id FROM pay_ WHERE id=?", (user_id,))
    pay_id = cursor.fetchone()[0]
    return pay_id


def get_pay__price_(user_id):
    cursor.execute("SELECT price FROM pay_ WHERE id=?", (user_id,))
    pay_id = cursor.fetchone()[0]
    return pay_id


def add_user_price(user_id, price):
    user_b = get_user_balance(user_id)
    user_price = float(user_b) + float(price)
    cursor.execute("UPDATE Users SET balance=? WHERE id=?", (user_price, user_id,))
    database.commit()


# Юзер
def add_user(message):
    cursor.execute("SELECT id FROM Users WHERE id=?", (message.chat.id,))
    user = cursor.fetchone()
    if user is None:
        d_time = datetime.now()
        cursor.execute("INSERT INTO Users VALUES(?,?,?,?,?)",
                       (message.chat.id, int(0), int(0), str('NO'), str(d_time),))
        database.commit()
    else:
        pass


# new_db_funcs
def add_prank(prank_audio, name, title, category):
    cursor.execute("SELECT prank_audio FROM all_pranks_beta_1 WHERE name=?", (name,))
    prank = cursor.fetchone()
    if prank is None:
        cursor.execute("INSERT INTO all_pranks_beta_1 (name,prank_audio,prank_title, category) VALUES(?,?,?,?)",
                       (name, prank_audio, title, category))
        database.commit()
        return True
    else:
        return False


def delete_prank(name):
    cursor.execute("DELETE FROM all_pranks_beta_1 WHERE name=?", (name,))
    deleted_prank = cursor.fetchone()
    database.commit()


def prank_categories() -> list[str]:
    cursor.execute("SELECT DISTINCT category FROM all_pranks_beta_1")
    categories = cursor.fetchall()
    return categories


def prank_names_id_in_category(category) -> list[list[str, int]]:
    cursor.execute("SELECT DISTINCT name, prank_id FROM all_pranks_beta_1 WHERE category=?", (category,))
    prank_names = cursor.fetchall()
    return prank_names


def prank_ids_in_category(category) -> list[str]:
    cursor.execute("SELECT DISTINCT prank_id FROM all_pranks_beta_1 WHERE category=?", (category,))
    prank_ids = cursor.fetchall()
    return prank_ids


def add_ref_user(message, ref):
    cursor.execute("SELECT id FROM Users WHERE id=?", (message.chat.id,))
    user = cursor.fetchone()
    if user is None:
        d_time = datetime.now()
        cursor.execute("INSERT INTO Users VALUES(?,?,?,?,?)",
                       (message.chat.id, int(ref), int(0), str('NO'), str(d_time),))
        database.commit()
    else:
        pass


def get_vip_status(user_id):
    cursor.execute("SELECT vip FROM Users WHERE id=?", (user_id,))
    status = cursor.fetchone()[0]
    if status == "NO":
        return False
    else:
        return True


def get_user_balance(user_id):
    cursor.execute("SELECT balance FROM Users WHERE id=?", (user_id,))
    balance = cursor.fetchone()[0]
    return balance


def get_ref_users(user_id):
    cursor.execute("SELECT id FROM Users WHERE ref=?", (user_id,))
    ref_users = cursor.fetchall()
    return len(ref_users)


def get_user_date(user_id):
    cursor.execute("SELECT date FROM Users WHERE id=?", (user_id,))
    data = cursor.fetchone()[0]
    return data


def get_prank_text_info(prank_id):
    cursor.execute("SELECT name FROM all_pranks_beta_1 WHERE prank_id=?", (prank_id,))
    prank_ = cursor.fetchone()[0]
    return prank_


def get_prank_audio_info(prank_id):
    cursor.execute("SELECT prank_audio FROM all_pranks_beta_1 WHERE prank_id=?", (prank_id,))
    prank_ = cursor.fetchone()[0]
    return prank_


def add_numb_info(message, prank_id):
    cursor.execute("SELECT id FROM prank WHERE id=?", (message.chat.id,))
    user = cursor.fetchone()
    if user is None:
        cursor.execute("INSERT INTO prank VALUES(?,?,?)", (message.chat.id, prank_id, 'numb',))
        database.commit()
    else:
        cursor.execute("UPDATE prank SET prank_id=? WHERE id=?", (prank_id, message.chat.id,))
        database.commit()


def clear_somethink_(numb):
    new = numb.replace('(', '')
    new_2 = new.replace(')', '')
    new_3 = new_2.replace('-', '')
    result_numb = new_3.replace(' ', '')
    print(result_numb)
    return result_numb


def add_user_numb_prank(message):
    numb = clear_somethink_(message.text)
    cursor.execute("UPDATE prank SET numb=? WHERE id=?", (numb, message.chat.id,))
    database.commit()


def get_user_prank_id(user_id):
    cursor.execute("SELECT prank_id FROM prank WHERE id=?", (user_id,))
    prank_id = cursor.fetchone()[0]
    return prank_id


def get_user_prank_numb(user_id):
    cursor.execute("SELECT numb FROM prank WHERE id=?", (user_id,))
    prank_numb = cursor.fetchone()[0]
    return prank_numb


def get_user_prank_title(prank_id):
    cursor.execute("SELECT prank_title FROM all_pranks_beta_1 WHERE prank_id=?", (prank_id,))
    prank_title = cursor.fetchone()[0]
    return prank_title


def check_take_user_prank_money(user_id):
    user_balance = get_user_balance(user_id)
    if user_balance < int(25):
        return False
    else:
        pass


def get_take_prank_money(user_id):
    vip_check = get_vip_status(user_id)
    user_balance = get_user_balance(user_id)
    if not vip_check:
        balance = int(user_balance) - int(30)
        cursor.execute("UPDATE Users SET balance=? WHERE id=?", (balance, user_id,))
        database.commit()


# def get_user_vip_procent(price):
#     first_price = price
#     price_procent = 70
#     result_price = float(first_price) / 100 * float(price_procent)
#     return result_price


def get_prem_(user_id):
    balance = get_user_balance(user_id)
    balance -= int(250)
    cursor.execute("UPDATE Users SET balance=? WHERE id=?", (balance, user_id,))
    cursor.execute("UPDATE Users SET vip=? WHERE id=?", ('YES', user_id,))
    database.commit()


async def remove_prem(user_id):
    cursor.execute("UPDATE Users SET vip=? WHERE id=?", ('NO', user_id,))
    database.commit()
    bot = Bot.get_current()
    await bot.send_message(user_id, "У вас закончилась премиум подписка.")


def add_user_order_prank(user_id, prank_title, result_audio, user_numb):
    cursor.execute("SELECT id FROM user_pranks WHERE id=?", (user_id,))
    user = cursor.fetchone()
    if user is None:
        cursor.execute("INSERT INTO user_pranks VALUES(?,?,?,?,?)",
                       (user_id, prank_title, result_audio, user_numb, int(1),))
        database.commit()
    else:
        numb = get_max_user_prank_numb(user_id)
        numb += int(1)
        cursor.execute("INSERT INTO user_pranks VALUES(?,?,?,?,?)",
                       (user_id, prank_title, result_audio, user_numb, numb,))
        database.commit()


def get_max_user_prank_numb(user_id):
    cursor.execute("SELECT MAX(numb) FROM user_pranks WHERE id=?", (user_id,))
    user_max_numb = cursor.fetchone()[0]
    return user_max_numb


def get_max_user_prank_prank_title(user_id, numb):
    cursor.execute("SELECT prank_title FROM user_pranks WHERE id=? AND numb=?", (user_id, numb,))
    user_prank_title = cursor.fetchone()[0]
    return user_prank_title


def get_max_user_prank_result_audio(user_id, numb):
    cursor.execute("SELECT prank_audio FROM user_pranks WHERE id=? AND numb=?", (user_id, numb,))
    result_audio = cursor.fetchone()[0]
    return result_audio


def get_max_user_prank_number(user_id, numb):
    cursor.execute("SELECT number FROM user_pranks WHERE id=? AND numb=?", (user_id, numb,))
    rnumber = cursor.fetchone()[0]
    return rnumber


def get_user_prank_all_title_keyboard(user_id):
    cursor.execute("SELECT prank_title FROM user_pranks WHERE id=?", (user_id,))
    all_user_prank_title = cursor.fetchall()
    return all_user_prank_title
