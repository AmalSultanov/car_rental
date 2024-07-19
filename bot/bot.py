# import requests
# import telebot
# from telebot import types
# from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
# from decouple import config
# bot = telebot.TeleBot(config('BOT_TOKEN'))
#
#
# def category_detail(update, context):
#     query = update.callback_query
#     pk = query.data.split('_')[1]
#
#     data = requests.get(f'http://localhost/categories/{pk}/').json()
#
#     if not data:
#         query.edit_message_text(text='No products yet',
#                                 reply_markup=get_category_detail_keyboard())
#         return
#
#     text = ''
#     for product in data:
#         text += f'{product["id"]}. {product["title"]}\n'
#
#     query.edit_message_text(text=text, reply_markup=get_category_detail_keyboard(data))
#
#
# def product_detail(update, context):
#     query = update.callback_query
#     pk = query.data.split('_')[1]
#
#     product = requests.get(f'http://localhost/products/{pk}/').json()
#
#     text = f'Title: {product["title"]}\n' \
#            f'Price: {product["price"]}\n' \
#            f'Description: {product["description"]}'
#
#     context.bot.send_photo(
#         chat_id=query.message.chat.id,
#         photo=requests.get(product["image"]).content,
#         caption=text,
#         reply_markup=get_product_detail_keyboard(product, context)
#     )
#     context.bot.delete_message(chat_id=query.message.chat.id,
#                                message_id=query.message.message_id)
#
#
#
# def back(update, context):
#     query = update.callback_query
#     level = query.data.split('_')[1]
#
#     if level == 'menu':
#         query.message.reply_text(text='Menu', reply_markup=get_menu_keyboard())
#     elif level == 'categories':
#         data = requests.get('http://localhost/categories/').json()
#
#         text = ''
#         for category in data:
#             text += f'{category["id"]}. {category["title"]}\n'
#
#         query.message.reply_text(text=text, reply_markup=get_categories_list_keyboard(data))
#     if level == 'category':
#         pk = query.data.split('_')[2]
#
#         data = requests.get(f'http://localhost/categories/{pk}/').json()
#
#         if not data:
#             query.message.reply_text(text='No products yet',
#                                      reply_markup=get_category_detail_keyboard())
#             return
#
#         text = ''
#         for product in data:
#             text += f'{product["id"]}. {product["title"]}\n'
#
#         query.message.reply_text(text=text, reply_markup=get_category_detail_keyboard(data))
#
#     context.bot.delete_message(chat_id=query.message.chat.id,
#                                message_id=query.message.message_id)
#
#
#
#
#
#
#
# def get_menu_keyboard():
#     keyboard = [
#         [
#             InlineKeyboardButton('Categories', callback_data='categories'),
#         ],
#         [
#             InlineKeyboardButton('Cart', callback_data='cart'),
#         ],
#         [
#             InlineKeyboardButton('Search', callback_data='search')
#         ],
#     ]
#
#     return InlineKeyboardMarkup(keyboard)
#
#
# def get_categories_list_keyboard(data):
#     keyboard = []
#     temp = []
#     for i in data:
#         temp.append(
#             InlineKeyboardButton(i["id"], callback_data=f'category_{i["id"]}'),
#         )
#     keyboard.append(temp)
#
#     keyboard.append(
#         [
#             InlineKeyboardButton('Back', callback_data='back_menu'),
#         ]
#     )
#
#     return InlineKeyboardMarkup(keyboard)
#
#
# def get_category_detail_keyboard(data=None):
#     keyboard = []
#     if data:
#         temp = []
#         for i in data:
#             temp.append(
#                 InlineKeyboardButton(i["id"], callback_data=f'product_{i["id"]}'),
#             )
#         keyboard.append(temp)
#
#     keyboard.append(
#         [
#             InlineKeyboardButton('Back', callback_data='back_categories'),
#         ]
#     )
#
#     return InlineKeyboardMarkup(keyboard)
#
#
# def get_product_detail_keyboard(product, context):
#     text = 'Add to cart'
#
#     if product["id"] in context.user_data.get('cart', []):
#         text = 'Remove from cart'
#
#     keyboard = [
#         [
#             InlineKeyboardButton(text, callback_data=f'cart_{product["id"]}'),
#         ],
#         [
#             InlineKeyboardButton('Cart', callback_data='cart'),
#         ],
#         [
#             InlineKeyboardButton('Back', callback_data=f'back_category_{product["category"]["id"]}'),
#         ],
#     ]
#
#     return InlineKeyboardMarkup(keyboard)
#
#
#
# def get_cars_keyboard(data):
#     keyboard = []
#     if data:
#         temp = []
#         for i in data:
#             temp.append(
#                 InlineKeyboardButton(i["id"], callback_data=f'car_{i["id"]}'),
#             )
#         keyboard.append(temp)
#
#     return InlineKeyboardMarkup(keyboard)
#
#
# def get_car_detail_keyboard():
#     data = requests.get('http://127.0.0.1:8000/en/api/cars/').json()
#     keyboard = []
#     if data:
#         temp = []
#         for i in data:
#             temp.append(
#                 InlineKeyboardButton(i["id"], callback_data=f'car_{i["id"]}'),
#             )
#         keyboard.append(temp)
#
#     keyboard.append(
#         [
#             InlineKeyboardButton('Назад', callback_data='back')
#         ]
#     )
#
#     return InlineKeyboardMarkup(keyboard)
#
#
# def car_detail(update, context):
#     query = update.callback_query
#     pk = query.data.split('_')[1]
#
#     car = requests.get(f'http://127.0.0.1:8000/en/api/cars/{pk}/').json()
#
#     text = f'Название: {car["title"]}\n' \
#            f'Марка: {car["brand"]}\n' \
#            f'Тип: {car["type"]}\n' \
#            f'Мощность: {car["power"]}\n' \
#            f'Топливо: {car["fuel"]}\n' \
#            f'Привод: {car["drive"]}\n' \
#            f'Коробка передач: {car["transmission"]}\n' \
#            f'Цвет: {car["color"]}\n' \
#            f'Год: {car["year"]}\n' \
#            f'Цена: ${car["price"]}' \
#            f'Описание: {car["description"]}' \
#
#     context.bot.send_photo(
#         chat_id=query.message.chat.id,
#         photo=requests.get(car["image"]).content,
#         caption=text,
#         reply_markup=get_car_detail_keyboard()
#     )
#
#     context.bot.delete_message(chat_id=query.message.chat.id, message_id=query.message.message_id)
#
#
# @bot.message_handler(regexp='^Авто 🚗$')
# def get_cars(message):
#     data = requests.get('http://127.0.0.1:8000/en/api/cars/').json()
#     text = ''
#
#     for car in data:
#         text += f'{car["id"]}. {car["title"]}\n'
#
#     bot.send_message(message.chat.id, text, reply_markup=get_cars_keyboard(data))
#
#
# @bot.message_handler(regexp='^Цены 💵$')
# def get_price(message):
#     data = requests.get('http://127.0.0.1:8000/en/api/cars/').json()
#     text = ''
#
#     for car in data:
#         text += f'{car["id"]}.  {car["title"]} - ${car["price"]} в день\n'
#
#     bot.send_message(message.chat.id, text, reply_markup=get_cars_keyboard(data))
#
#
# @bot.message_handler(regexp='^Профиль$')
# def get_profile(message):
#     bot.send_message(message.chat.id, 'Профиль')
#
#
# @bot.message_handler(regexp='^Сервисы 🔧$')
# def get_profile(message):
#     bot.send_message(message.chat.id, 'Сервисы')
#
#
# @bot.message_handler(regexp='^О нас 👀$')
# def get_profile(message):
#     bot.send_message(message.chat.id, 'О нас')
#
#
# @bot.message_handler(regexp='^Контакты 📞$')
# def get_profile(message):
#     bot.send_message(message.chat.id, 'Контакты')
#
#
# @bot.message_handler(regexp='^Профиль 👤$')
# def get_profile(message):
#     bot.send_message(message.chat.id, 'Профиль')
#
#
# @bot.message_handler(regexp='^Наша команда 👥$')
# def get_profile(message):
#     bot.send_message(message.chat.id, 'Наша команда')
#
#
# @bot.message_handler(regexp='^Поиск 🔍$')
# def get_profile(message):
#     bot.send_message(message.chat.id, 'Поиск')
#
#
# @bot.message_handler(commands=['start'])
# def send_welcome(message):
#     keyboard = types.ReplyKeyboardMarkup(row_width=2)
#     cars = types.KeyboardButton('Авто 🚗')
#     price = types.KeyboardButton('Цены 💵')
#     services = types.KeyboardButton('Сервисы 🔧')
#     about = types.KeyboardButton('О нас 👀')
#     contacts = types.KeyboardButton('Контакты 📞')
#     profile = types.KeyboardButton('Профиль 👤')
#     team = types.KeyboardButton('Наша команда 👥')
#     search = types.KeyboardButton('Поиск 🔍')
#     keyboard.add(cars, price, services, about, contacts, profile, team, search)
#
#     bot.send_message(message.chat.id, 'Добро пожаловать!\nВыберите что хотите посмотреть:', reply_markup=keyboard)
#
#
# bot.polling()
