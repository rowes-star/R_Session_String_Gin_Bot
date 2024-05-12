from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("↯︙ انشاء جلسة سيشن  .", callback_data="generate")]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("↯︙المطور .", url="https://t.me/R7_OX"),
        ],
    ]

    START = """
↯︙اهلا بك في بوت انشاء كود جلسة بايروجرام ، تليثون .

↯︙ يمكنك انشاء كود بايروجرام بسهولة .

↯︙يتم ارسال الكود في الرسائل المحفوضة .
    """
