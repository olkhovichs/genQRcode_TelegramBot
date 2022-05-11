from bot.config import TOKEN
import bot.buttons as btn

from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.utils.markdown import text
from aiogram.dispatcher import Dispatcher

bot = Bot(TOKEN)
dp = Dispatcher(bot)


#main
@dp.message_handler(commands = ['start'])
async def main(message: types.Message):
    await message.reply("Choice an action:", reply_markup = btn.main_menu())

#menu
'''
@dp.callback_query_handler(lambda call: True)
async def event_buttons(call: types.CallbackQuery):
    #main menu
    if call.data == ''
    '''






if __name__ == '__main__':
    executor.start_polling(dp)