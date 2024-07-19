import requests

from keyboards import (get_menu_keyboard, get_cars_list_keyboard,
                       get_category_detail_keyboard, get_car_detail_keyboard,
                       get_price_keyboard)
from bot.utils import save_user


def start(update, context):
    user = update.effective_user
    save_user(user)
    update.message.reply_text(
        'Добро пожаловать!\nВыберите что хотите посмотреть:',
        reply_markup=get_menu_keyboard())


def get_cars_list(update, context):
    query = update.callback_query

    data = requests.get('http://127.0.0.1:8000/en/api/cars/').json()

    text = ''
    for car in data:
        text += f'{car["id"]}. {car["title"]}\n'

    query.edit_message_text(text=text,
                            reply_markup=get_cars_list_keyboard(data))


def get_price(update, context):
    query = update.callback_query

    data = requests.get('http://127.0.0.1:8000/en/api/cars/').json()

    text = ''
    for car in data:
        text += f'{car["id"]}. {car["title"]} - ${car["price"]} в день\n'

    query.edit_message_text(text=text, reply_markup=get_price_keyboard(data))


def category_detail(update, context):
    query = update.callback_query
    pk = query.data.split('_')[1]

    data = requests.get(f'http://127.0.0.1:8000/en/api/cars/{pk}/').json()

    if not data:
        query.edit_message_text(text='No products yet',
                                reply_markup=get_category_detail_keyboard())
        return

    text = ''
    for product in data:
        text += f'{product["id"]}. {product["title"]}\n'

    query.edit_message_text(text=text,
                            reply_markup=get_category_detail_keyboard(data))


def car_detail(update, context):
    query = update.callback_query
    pk = query.data.split('_')[1]

    car = requests.get(f'http://127.0.0.1:8000/ru/api/cars/{pk}/').json()

    text = f'Название:  {car["title"]}\n' \
           f'Марка:  {car["brand"]["title"]}\n' \
           f'Тип:  {car["type"]["title"]}\n' \
           f'Мощность:  {car["power"]["amount"]} л.с.\n' \
           f'Топливо:  {car["fuel"]["title"]}\n' \
           f'Привод:  {car["drive"]["title"]}\n' \
           f'Коробка передач:  {car["transmission"]["title"]}\n' \
           f'Цвет:  {car["color"]["title"]}\n' \
           f'Год:  {car["year"]["title"]}\n' \
           f'Цена:  ${car["price"]} в день' \
        # f'Описание:  ${car["description"]}' \

    context.bot.send_photo(
        chat_id=query.message.chat.id,
        photo=requests.get(car["image"]).content,
        caption=text,
        reply_markup=get_car_detail_keyboard(car, context)
    )
    context.bot.delete_message(chat_id=query.message.chat.id,
                               message_id=query.message.message_id)


def search(update, message):
    pass


def back(update, context):
    query = update.callback_query
    level = query.data.split('_')[1]

    if level == 'menu':
        query.message.reply_text(
            text='Добро пожаловать!\nВыберите что хотите посмотреть:',
            reply_markup=get_menu_keyboard())
    elif level == 'cars':
        data = requests.get('http://127.0.0.1:8000/en/api/cars/').json()

        text = ''
        for category in data:
            text += f'{category["id"]}. {category["title"]}\n'

        query.message.reply_text(text=text,
                                 reply_markup=get_price_keyboard(data))
    if level == 'car':
        pk = query.data.split('_')[1]

        data = requests.get(f'http://127.0.0.1:8000/en/api/cars/{pk}/').json()

        if not data:
            query.message.reply_text(text='No products yet',
                                     reply_markup=get_car_detail_keyboard(
                                         data, context))
            return

        text = ''
        for car in data:
            text += f'{car["id"]}. {car["title"]}\n'

        query.message.reply_text(text=text,
                                 reply_markup=get_car_detail_keyboard(data,
                                                                      context))

    context.bot.delete_message(chat_id=query.message.chat.id,
                               message_id=query.message.message_id)


def checkout(update, context):
    query = update.callback_query
    user_id = update.effective_user.id
    cart = context.user_data['cart']

    requests.post(
        'http://localhost/orders/create/',
        data={
            'user_id': user_id,
            'products': cart
        }
    )

    query.answer('Order is created')
    context.user_data['cart'] = []

    query.edit_message_text(text='Menu', reply_markup=get_menu_keyboard())
