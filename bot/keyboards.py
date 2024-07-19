from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def get_menu_keyboard():
    keyboard = [
        [
            InlineKeyboardButton('Авто 🚗', callback_data='cars'),
        ],
        [
            InlineKeyboardButton('Цены 💵', callback_data='price'),
        ],
        [
            InlineKeyboardButton('Сервисы 🔧', callback_data='services')
        ],
        [
            InlineKeyboardButton('О нас 👀', callback_data='about')
        ],
        [
            InlineKeyboardButton('Контакты 📞', callback_data='contacts')
        ],
        [
            InlineKeyboardButton('Профиль 👤', callback_data='profile')
        ],
        [
            InlineKeyboardButton('Наша команда 👥', callback_data='team')
        ],
        [
            InlineKeyboardButton('Поиск 🔍', callback_data='search')
        ]
    ]

    return InlineKeyboardMarkup(keyboard)


def get_cars_list_keyboard(data):
    keyboard = []
    temp = []
    for i in data:
        temp.append(
            InlineKeyboardButton(i["id"], callback_data=f'car_{i["id"]}'),
        )
    keyboard.append(temp)

    keyboard.append(
        [
            InlineKeyboardButton('Назад', callback_data='back_menu'),
        ]
    )

    return InlineKeyboardMarkup(keyboard)


def get_price_keyboard(data):
    keyboard = []
    temp = []
    for i in data:
        temp.append(
            InlineKeyboardButton(i["id"], callback_data=f'car_{i["id"]}'),
        )
    keyboard.append(temp)

    keyboard.append(
        [
            InlineKeyboardButton('Назад', callback_data='back_menu'),
        ]
    )

    return InlineKeyboardMarkup(keyboard)


def get_category_detail_keyboard(data=None):
    keyboard = []
    if data:
        temp = []
        for i in data:
            temp.append(
                InlineKeyboardButton(i["id"],
                                     callback_data=f'product_{i["id"]}'),
            )
        keyboard.append(temp)

    keyboard.append(
        [
            InlineKeyboardButton('Back', callback_data='back_categories'),
        ]
    )

    return InlineKeyboardMarkup(keyboard)


def get_car_detail_keyboard(data, context):
    keyboard = [
        [
            InlineKeyboardButton('Назад', callback_data='back_cars'),
        ],
    ]

    return InlineKeyboardMarkup(keyboard)


def get_price_detail_keyboard(data, context):
    keyboard = [
        [
            InlineKeyboardButton('Назад', callback_data='back_price'),
        ],
    ]

    return InlineKeyboardMarkup(keyboard)


def get_cart_keyboard():
    keyboard = [
        [
            InlineKeyboardButton('Checkout', callback_data=f'checkout'),
        ],
        [
            InlineKeyboardButton('Back', callback_data='back_menu'),
        ],
    ]

    return InlineKeyboardMarkup(keyboard)
