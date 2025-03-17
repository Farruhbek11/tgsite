

    
import logging
from aiogram import Bot, Dispatcher, executor, types
from keyboards import get_main_keyboard
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

API_TOKEN = "7694486159:AAEU5CyXSsaNIzCgM0EJwcLoijSjbWm7fcI" 

logging.basicConfig(level=logging.INFO)

bot = Bot(token="7609505448:AAE2LF8C_k8MB50iZlxUaO8mYIYkTN1lw5A")
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def salom_ber(message: types.Message):
    await message.answer(text="Assalomu aleykum, xush kelibsiz!, buyurtma berish uchun avval kanalimizga obuna boling!  https://t.me/Shahzodalovecooking", reply_markup=get_main_keyboard())


@dp.message_handler(commands=['menu'])
async def send_menu(message: types.Message):
    await message.reply("Quyidagi shirinliklardan birini tanlang:", reply_markup=get_main_keyboard())


PIES = {
    "Napalyon": {"price": "300.000 so'm", "image": "https://t.me/Shahzodalovecooking/27727"},    
    "Medovi": {"price": "300.000 so'm", "image": "https://safiabakery.uz/uploads/products/362_1719310501.jpg"},
    "Trayfel": {"price": "70.000 so'm", "image": "https://i.ytimg.com/vi/WmOJMmmuiQ4/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLBeEMstXeKlyj4yeyiWcNSobRAUrg"},
    "Shokoladli banan": {"price": "10.000 so'm", "image": "https://static.toiimg.com/thumb/62378305.cms?width=1200&height=900"},
    "Shokoladli qulupnay": {"price": "13.000 so'm", "image": "https://i.ytimg.com/vi/EioHSjINAiM/maxresdefault.jpg"},
    "Tartaletka": {"price": "12.000 so'm", "image": "https://t.me/Shahzodalovecooking/27723"},
    "Choko Napalyon": {"price": "350.000 so'm", "image": "https://img.freepik.com/premium-photo/piece-chocolate-napoleon-cake-close-up_711700-9717.jpg"},
    "Brauni Sendvich": {"price": "kottasi: 25.000 so'm kichkinasi: 20.000 so'm", "image": "https://i.ytimg.com/vi/1a8ZV8jf6w4/hqdefault.jpg"},
    "Matilda": {"price": "350.000 so'm", "image": "https://bakewithzoha.com/wp-content/uploads/2024/05/matilda-chocolate-cake-featured2.jpg"},
    "Xarid qilish": {"price": "kelishish uchun shu lichkaga yozing @Shahzoda_love_cooking", "image": "https://images.app.goo.gl/43X6FtjEpw1D7gaH8"}
}


@dp.message_handler(lambda message: message.text in PIES.keys())
async def send_pie_details(message: types.Message): 
    pie_name = message.text
    pie_info = PIES[pie_name]
    
    await message.answer_photo(
        photo=pie_info["image"],
        caption=f"{pie_name}\nNarxi: {pie_info['price']}"
    )

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)






