from aiogram import Bot
from aiogram.types import BotCommandScopeAllGroupChats, BotCommandScopeAllPrivateChats, \
    BotCommandScopeAllChatAdministrators, BotCommandScopeDefault, BotCommand, BotCommandScopeChat


async def set_restart_command(bot: Bot):
    return await bot.set_my_commands(commands=[
        BotCommand("start", "Перезапустить бота")
    ]
    )


async def force_reset_all_commands(bot: Bot):
    for language_code in ('ru', 'en', 'uk', 'uz'):
        for scope in (
                BotCommandScopeAllGroupChats(),
                BotCommandScopeAllPrivateChats(),
                BotCommandScopeAllChatAdministrators(),
                BotCommandScopeDefault(),
        ):
            await bot.delete_my_commands(scope, language_code)