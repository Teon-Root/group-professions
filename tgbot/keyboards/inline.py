from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

# -------------------------------------------------------------------------------------------------------- keyboard back
url_button_1 = InlineKeyboardButton(
    text='Дистанційна робота',
    url='tg://resolve?domain=Carriers_Europe'
)
url_button_2 = InlineKeyboardButton(
    text='Робота в офісі',
    url='https://t.me/+EusrRXfIi740NjUy'
)
url_button_3 = InlineKeyboardButton(
    text='Заочна робота',
    url='https://t.me/+EusrRXfIi740NjUy'
)
url_button_4 = InlineKeyboardButton(
    text='Стажування',
    url='tg://resolve?domain=Carriers_Europe'
)

# Создаем объект инлайн-клавиатуры
keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[url_button_1],
                     [url_button_2],
                     [url_button_3],
                     [url_button_4]]
)

# remote_control_button = InlineKeyboardButton(test='Дистанційна робота', url='tg://resolve?domain=telegram')
# office_button = InlineKeyboardButton(test='Робота в офісі', url='tg://resolve?domain=telegram')
# part_time_button = InlineKeyboardButton(test='Заочна робота', url='tg://resolve?domain=telegram')
# internship_button = InlineKeyboardButton(test='Стажування', url='tg://resolve?domain=telegram')
# url_inline.add(remote_control_button, office_button, part_time_button, internship_button)

# --------------------------------------------------------------------------------------------------- keyboard yes or no
