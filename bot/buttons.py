from aiogram.types import ReplyKeyboardRemove, \
        ReplyKeyboardMarkup, KeyboardButton, \
        InlineKeyboardMarkup, InlineKeyboardButton

# main menu
def main_menu():
    btn_scan = InlineKeyboardButton(text='Scan the QR code', callback_data='scan_qr')
    btn_gen = InlineKeyboardButton(text='Generate QR code', callback_data='gen_qr')
    btn_exit = InlineKeyboardButton(text='Exit', callback_data='exit')

    markup_menu = InlineKeyboardMarkup()
    markup_menu.row(btn_scan, btn_gen)
    markup_menu.row(btn_exit)

    return markup_menu