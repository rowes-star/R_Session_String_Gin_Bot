from pyrogram.types import InlineKeyboardButton

class Data:
    generate_single_button = [InlineKeyboardButton("↯︙ بدء استخراج .", callback_data="generate")]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("↯︙المطور .", url="http//t.me/E_I_9"),
        ],
    ]

    START = """
↯︙اهلا بك في بوت انشاء كود جلسة .

↯︙ يمكنك انشاء كود بايروجرام وتليثون بسهولة .

↯︙يتم ارسال الكود في الرسائل المحفوظة .
    """
