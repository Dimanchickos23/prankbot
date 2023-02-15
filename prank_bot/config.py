from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str
    admin_ids: list[int]
    use_redis: bool


@dataclass
class Pay_API:
    token: str
    shop_id: int


@dataclass
class Config:
    tg_bot: TgBot
    pay_api: Pay_API


def load_config(path: str = None):
    env = Env()
    env.read_env(path)

    return Config(
        tg_bot=TgBot(
            token=env.str("BOT_TOKEN"),
            admin_ids=list(map(int, env.list("ADMINS"))),
            use_redis=env.bool("USE_REDIS")
        ),
        pay_api=Pay_API(
            token=env.str("SHOP_API_TOKEN"),
            shop_id=env.int("SHOP_ID")
        )
    )