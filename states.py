from aiogram.dispatcher.filters.state import State, StatesGroup

class Form(StatesGroup):
    ish = State()
    ism = State()
    firma = State()
    inn = State()
    tel = State()
    
