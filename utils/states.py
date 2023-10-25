from aiogram.fsm.state import State,StatesGroup


class form_price(StatesGroup):
    first_sum = State()
    second_sum = State()
    third_sum = State()



class form_send_messages(StatesGroup):
    text = State()
    photo = State()