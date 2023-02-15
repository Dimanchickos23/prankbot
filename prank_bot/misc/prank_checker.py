import asyncio

from aiogram import Bot

from prank_bot.db_api.db import get_user_prank_numb, get_user_prank_id, get_user_prank_title, add_user_order_prank, \
    get_take_prank_money
from prank_bot.keyboards import retrun_markup
from prank_bot.misc.callink import new_check_call


async def check_user_prank(chat_id):
    bot = Bot.get_current()
    numb = get_user_prank_numb(chat_id)
    # check__ = check_(numb)
    prank_campaign_id = get_user_prank_id(chat_id)
    while True:
        print('a')
        await asyncio.sleep(1)
        check__ = new_check_call(prank_campaign_id, int(numb))
        if check__['dial_status_display'] == 'Ошибка при вызове абонента':
            await bot.send_message(chat_id, '<strong>Звонок не смог быть совершен❌</strong>\n\n'
                                            '<i>Статус</i>:<code> Ошибка при вызове абонента</code>', parse_mode='HTML',
                                   reply_markup=retrun_markup())
            break
        if check__['dial_status_display'] == 'Не дозвонились':
            await bot.send_message(chat_id, '<strong>Звонок не смог быть совершен❌</strong>\n\n'
                                            '<i>Статус</i>:<code> Не дозвонились </code>', parse_mode='HTML',
                                   reply_markup=retrun_markup())
            break
        if check__['dial_status_display'] == 'Абонент сбросил звонок':
            await bot.send_message(chat_id, '<strong>Звонок не смог быть совершен❌</strong>\n\n'
                                            '<i>Статус</i>:<code> Абонент сбросил звонок </code>', parse_mode='HTML',
                                   reply_markup=retrun_markup())
            break
        if check__['dial_status_display'] == 'Абонент занят':
            await bot.send_message(chat_id, '<strong>Звонок не смог быть совершен❌</strong>\n\n'
                                            '<i>Статус</i>:<code> Абонент занят </code>', parse_mode='HTML',
                                   reply_markup=retrun_markup())
            break
        if check__['dial_status_display'] == 'Номер удалён из прозвона':
            await bot.send_message(chat_id, '<strong>Звонок не смог быть совершен❌</strong>\n\n'
                                            '<i>Статус</i>:<code> Номер удалён из прозвона </code>', parse_mode='HTML',
                                   reply_markup=retrun_markup())
            break
        if check__['dial_status_display'] == 'По максимальной продолжительности звонка':
            await bot.send_message(chat_id, '<strong>Звонок не смог быть совершен❌</strong>\n\n'
                                            '<i>Статус</i>:<code> По максимальной продолжительности звонка </code>',
                                   parse_mode='HTML',
                                   reply_markup=retrun_markup())
            break
        if check__['dial_status_display'] == 'Внутренняя ошибка сервера':
            await bot.send_message(chat_id, '<strong>Звонок не смог быть совершен❌</strong>\n\n'
                                            '<i>Статус</i>:<code> Внутренняя ошибка сервера </code>', parse_mode='HTML',
                                   reply_markup=retrun_markup())
            break
        if check__['dial_status_display'] == 'Событие по нажатию кнопки и продолжительности разговора':
            await bot.send_message(chat_id, '<strong>Звонок не смог быть совершен❌</strong>\n\n'
                                            '<i>Статус</i>:<code> Событие по нажатию кнопки и продолжительности разговора </code>',
                                   parse_mode='HTML',
                                   reply_markup=retrun_markup())
            break
        if check__['dial_status_display'] == 'Попытка приостановлена по отрицательному баланс':
            await bot.send_message(chat_id, '<strong>Звонок не смог быть совершен❌</strong>\n\n'
                                            '<i>Статус</i>:<code> Попытка приостановлена </code>', parse_mode='HTML',
                                   reply_markup=retrun_markup())
            break
        if check__['dial_status_display'] == 'Не найден транк для звонка':
            await bot.send_message(chat_id, '<strong>Звонок не смог быть совершен❌</strong>\n\n'
                                            '<i>Статус</i>:<code> Не найден транк для звонка </code>',
                                   parse_mode='HTML',
                                   reply_markup=retrun_markup())
            break
        if check__['dial_status_display'] == 'Не найден исходящий номер для звонка':
            await bot.send_message(chat_id, '<strong>Звонок не смог быть совершен❌</strong>\n\n'
                                            '<i>Статус</i>:<code> Не найден исходящий номер для звонка </code>',
                                   parse_mode='HTML',
                                   reply_markup=retrun_markup())
            break
        if check__['dial_status_display'] == 'Данное направление заблокировано':
            await bot.send_message(chat_id, '<strong>Звонок не смог быть совершен❌</strong>\n\n'
                                            '<i>Статус</i>:<code> Данное направление заблокировано </code>',
                                   parse_mode='HTML',
                                   reply_markup=retrun_markup())
            break
        if check__['dial_status_display'] == 'Ошибка генерации ролика':
            await bot.send_message(chat_id, '<strong>Звонок не смог быть совершен❌</strong>\n\n'
                                            '<i>Статус</i>:<code> Ошибка генерации ролика </code>', parse_mode='HTML',
                                   reply_markup=retrun_markup())
            break
        if check__['dial_status_display'] == 'Слишком короткий ролик':
            await bot.send_message(chat_id, '<strong>Звонок не смог быть совершен❌</strong>\n\n'
                                            '<i>Статус</i>:<code> Слишком короткий ролик </code>', parse_mode='HTML',
                                   reply_markup=retrun_markup())
            break
        if check__['dial_status_display'] == 'Не найден провайдер для звонка':
            await bot.send_message(chat_id, '<strong>Звонок не смог быть совершен❌</strong>\n\n'
                                            '<i>Статус</i>:<code> Не найден провайдер для звонка </code>',
                                   parse_mode='HTML',
                                   reply_markup=retrun_markup())
            break
        if check__['dial_status_display'] == 'Истекло время жизни звонка':
            await bot.send_message(chat_id, '<strong>Звонок не смог быть совершен❌</strong>\n\n'
                                            '<i>Статус</i>:<code> Истекло время жизни звонка </code>',
                                   parse_mode='HTML',
                                   reply_markup=retrun_markup())
            break
        if check__['dial_status_display'] == 'Попытки закончились':
            await bot.send_message(chat_id, '<strong>Звонок не смог быть совершен❌</strong>\n\n'
                                            '<i>Статус</i>:<code> Попытки закончились </code>', parse_mode='HTML',
                                   reply_markup=retrun_markup())
            break
        if check__['status_display'] == 'Попытки закончились':
            prank_title = get_user_prank_title(prank_campaign_id)
            add_user_order_prank(chat_id, prank_title, check__['recorded_audio'], numb)
            await bot.send_message(chat_id, '<strong>Звонок совершен ✅</strong>\n\n'
                                            '<i>Статус</i>:<code> Абонент недоступен ⛔️</code>\n'
                                            '<i>Абонент недоступен ⛔</i>\n\n',
                                   parse_mode='HTML', reply_markup=retrun_markup())
            break
        if check__[
            'dial_status_display'] == 'Абонент ответил, но продолжительности разговора не достаточно для фиксации результата в статистике':
            prank_title = get_user_prank_title(prank_campaign_id)
            add_user_order_prank(chat_id, prank_title, check__['recorded_audio'], numb)
            await bot.send_message(chat_id, '<strong>Звонок совершен ✅</strong>\n\n'
                                            '<i>Статус</i>:<code> Абонент недоступен ⛔️</code>\n'
                                            '<i>Абонент недоступен ⛔</i>\n\n'
                                            f'<a href="{check__["recorded_audio"]}">Запись звонка ❕</a>',
                                   parse_mode='HTML', reply_markup=retrun_markup())
            break
        if check__['dial_status_display'] == 'Ответил автоответчик':
            get_take_prank_money(chat_id)
            prank_title = get_user_prank_title(prank_campaign_id)
            add_user_order_prank(chat_id, prank_title, check__['recorded_audio'], numb)
            await bot.send_message(chat_id, '<strong>Звонок совершен✅</strong>\n\n'
                                            '<i>Статус</i>:<code> Совершен ответил автоответчик✅</code>\n\n'
                                            f'<a href="{check__["recorded_audio"]}">Запись звонка ❕</a>',
                                   parse_mode='HTML',
                                   reply_markup=retrun_markup())
            break
        if check__['dial_status_display'] == 'Ответил автоответчик (deprecated)':
            get_take_prank_money(chat_id)
            get_take_prank_money(chat_id)
            prank_title = get_user_prank_title(prank_campaign_id)
            add_user_order_prank(chat_id, prank_title, check__['recorded_audio'], numb)
            await bot.send_message(chat_id, '<strong>Звонок совершен✅</strong>\n\n'
                                            '<i>Статус</i>:<code> Совершен ответил автоответчик✅</code>\n\n'
                                            f'<a href="{check__["recorded_audio"]}">Запись звонка ❕</a>',
                                   parse_mode='HTML',
                                   reply_markup=retrun_markup())
            break
        if check__['status'] == 'compl_finished':
            get_take_prank_money(chat_id)
            user_prank_title = get_user_prank_title(prank_campaign_id)
            add_user_order_prank(chat_id, user_prank_title, check__['recorded_audio'], numb)
            await bot.send_message(chat_id, '<strong>Звонок успешно совершен✅</strong>\n\n'
                                            '<i>Статус</i>:<code> Совершен✅</code>\n\n'
                                            f'<a href="{check__["recorded_audio"]}">Запись звонка ❕</a>',
                                   parse_mode='HTML',
                                   reply_markup=retrun_markup())
            break
        else:
            continue