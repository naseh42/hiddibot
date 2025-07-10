from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor
from config import BOT_TOKEN
from plans import plans, trial_plan
from hiddify_api import create_profile
from db import init_db
import asyncio

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    for plan in plans:
        kb.add(KeyboardButton(plan["label"]))
    kb.add(KeyboardButton("🧪 اشتراک تست"))
    await message.answer("سلام! لطفاً پلن مورد نظر را انتخاب کن:", reply_markup=kb)

@dp.message_handler(lambda m: m.text == "🧪 اشتراک تست")
async def trial(message: types.Message):
    link = create_profile(message.from_user.full_name, trial_plan["volume"], trial_plan["duration"])
    await message.answer(f"🧪 اشتراک تست:\n{link}")

@dp.message_handler(lambda m: any(m.text == p["label"] for p in plans))
async def buy_plan(message: types.Message):
    plan = next(p for p in plans if p["label"] == message.text)
    link = create_profile(message.from_user.full_name, plan["volume"], plan["duration"])
    await message.answer(f"✅ اشتراک ساخته شد:\n{link}")

if __name__ == "__main__":
    asyncio.run(init_db())
    executor.start_polling(dp)
