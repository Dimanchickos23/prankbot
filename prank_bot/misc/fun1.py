async def fun1(chat_id):
    await bot.send_message(chat_id, "Получения Информации..")
    numb = 89210191999
    # check__ = check_(numb)
    prank_campaign_id = get_user_prank_id(chat_id)
    await bot.send_message(chat_id, '<strong>Звонок будет совершен в ближайщее время</strong>\n\n'
                                    '<i>Статус</i>:<code> В процессе</code>', parse_mode='HTML',
                           reply_markup=check_prank_status(numb))
    while True:
        check__ = new_check_call(prank_campaign_id, int(numb))
        if check__['dial_status_display'] == 'Не дозвонились':
            await bot.send_message(chat_id, '<strong>Звонок не смог быть совершен❌</strong>\n\n'
                                            '<i>Статус</i>:<code> Не дозвонились </code>', parse_mode='HTML',
                                   reply_markup=retrun_markup())
            break
        if check__[
            'dial_status_display'] == 'Абонент ответил, но продолжительности разговора не достаточно для фиксации результата в статистике':
            prank_title = get_user_prank_title(prank_campaign_id)
            add_user_order_prank(chat_id, prank_title, check__['recorded_audio'], numb)
            await bot.send_message(chat_id, '<strong>Звонок совершен✅</strong>\n\n'
                                            '<i>Статус</i>:<code> Совершен Абонент ответил ✅</code>\n'
                                            '<i>Абонент ответил, но продолжительности разговора не достаточно для фиксации результата в статистике</i>\n\n'
                                            f'<a href="{check__["recorded_audio"]}">Запись звонка ❕</a>',
                                   parse_mode='HTML', reply_markup=retrun_markup())
            break
        if check__['dial_status_display'] == 'Ответил автоответчик':
            prank_title = get_user_prank_title(prank_campaign_id)
            add_user_order_prank(chat_id, prank_title, check__['recorded_audio'], numb)
            await bot.send_message(chat_id, '<strong>Звонок совершен✅</strong>\n\n'
                                            '<i>Статус</i>:<code> Совершен ответил автоответчик✅</code>\n\n'
                                            f'<a href="{check__["recorded_audio"]}">Запись звонка ❕</a>',
                                   parse_mode='HTML',
                                   reply_markup=retrun_markup())
            break
        if check__['status'] == 'compl_finished':
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