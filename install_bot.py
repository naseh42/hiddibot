import os

print("📦 نصب ربات V2Ray با پنل Hiddify در حال آغاز است...\n")

# جمع‌آوری اطلاعات موردنیاز
bot_token = input("🤖 توکن ربات تلگرام: ")
admin_id = input("🛡️ آی‌دی عددی ادمین: ")
merchant_id = input("💳 کد مرچنت زرین‌پال: ")
callback_url = input("🌐 لینک بازگشت زرین‌پال (مثلاً https://yourdomain.com/callback): ")
hiddify_url = input("🔗 آدرس API پنل Hiddify (مثلاً https://panel.domain.com/api/v1): ")
hiddify_token = input("🔐 توکن API پنل Hiddify: ")

print("\n🔧 در حال نصب کتابخانه‌های مورد نیاز...")
os.system("pip install aiogram aiosqlite requests flask")

print("\n📁 در حال ساخت فایل config.py...")
with open("config.py", "w") as f:
    f.write(f'''BOT_TOKEN = "{bot_token}"
ADMIN_ID = {admin_id}
MERCHANT_ID = "{merchant_id}"
CALLBACK_URL = "{callback_url}"
HIDDIFY_API_URL = "{hiddify_url}"
HIDDIFY_TOKEN = "{hiddify_token}"
''')

print("\n📂 ساخت دیتابیس اولیه...")
with open("db.py", "w") as f:
    f.write('''import aiosqlite

async def init_db():
    async with aiosqlite.connect("data.db") as db:
        await db.execute("""
        CREATE TABLE IF NOT EXISTS users (
            telegram_id INTEGER PRIMARY KEY,
            full_name TEXT,
            has_trial INTEGER DEFAULT 0,
            referral_code TEXT,
            ref_by TEXT,
            plan TEXT,
            config_link TEXT,
            is_reseller INTEGER DEFAULT 0
        )""")
        await db.execute("""
        CREATE TABLE IF NOT EXISTS backups (
            telegram_id INTEGER,
            config_link TEXT,
            created_at TEXT
        )""")
        await db.commit()
''')

print("\n📄 افزودن سایر فایل‌ها (main.py و بخش‌های دیگر)...")
# برای ساده‌سازی، اینجا فقط اسکلت main.py ساخته می‌شه
with open("main.py", "w") as f:
    f.write('''from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from config import BOT_TOKEN
from db import init_db
import asyncio

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def welcome(msg: types.Message):
    await msg.answer("✅ ربات با موفقیت نصب شد و آماده است!")

if __name__ == "__main__":
    asyncio.run(init_db())
    executor.start_polling(dp)
''')

print("\n✅ نصب کامل شد! حالا می‌تونی با دستور زیر ربات رو اجرا کنی:")
print("python main.py")

print("\n🚀 برای نصب به‌صورت دائمی یا اتصال Webhook، لطفاً مرحله بعد رو به من بگو تا برات Docker یا Webhook سروری بنویسم!")
