from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("↯︙ انشاء كود بايروجرام .", callback_data="generate")]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("↯︙المطور .", url="https://t.me/RQ_V0"),
        ],
    ]

    START = """
↯︙اهلا بك في بوت انشاء كود بايروجرام .

↯︙ يمكنك انشاء كود بايروجرام وتليثون بسهولة .

↯︙يتم ارسال الكود في الرسائل المحفوظة .
    """
