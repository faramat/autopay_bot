from aiogram.fsm.state import State,StatesGroup


class Form(StatesGroup):
    first_sum = State()
    second_sum = State()
    third_sum = State()