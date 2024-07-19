from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

from handlers import (start, get_cars_list, category_detail, back,
                      search, checkout, get_price, car_detail)


def main():
    updater = Updater(config('BOT_TOKEN'))

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))

    dispatcher.add_handler(
        CallbackQueryHandler(get_cars_list, pattern='^cars'))
    dispatcher.add_handler(CallbackQueryHandler(get_price, pattern='^price'))
    dispatcher.add_handler(
        CallbackQueryHandler(category_detail, pattern='^category_'))
    dispatcher.add_handler(CallbackQueryHandler(car_detail, pattern='^car_'))
    dispatcher.add_handler(CallbackQueryHandler(back, pattern='^back_'))
    dispatcher.add_handler(CallbackQueryHandler(search, pattern='^search$'))
    dispatcher.add_handler(
        CallbackQueryHandler(checkout, pattern='^checkout$'))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
