from aiogram.utils.keyboard import ReplyKeyboardBuilder

def calc():
    items= [
        "1","2","3","/",
        "4","5","6","*",
        "7","8","9","-",
        "0",".","=","+",
    ]
    builder = ReplyKeyboardBuilder()
    [builder.button(text=item) for item in items]
    builder.button(text="Back")
    builder.adjust(*[4] * 4) #контроль количества кнопок на 1 ряду
    return builder.as_markup(resize_keyboard = True)
