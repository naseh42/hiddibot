#!/bin/bash

echo "🚀 شروع نصب Hiddibot با Webhook و اجرای دائمی"

# نصب پیش‌نیازها
sudo apt update
sudo apt install -y git python3 python3-pip python3-venv curl

# دریافت اطلاعات لازم
read -p "🤖 توکن ربات تلگرام: " BOT_TOKEN
read -p "🛡️ آی‌دی عددی ادمین: " ADMIN_ID
read -p "💳 کد مرچنت زرین‌پال: " MERCHANT_ID
read -p "🌐 لینک بازگشت زرین‌پال (مثلاً https://yourdomain.com/callback): " CALLBACK_URL
read -p "🔗 آدرس API پنل Hiddify: " HIDDIFY_API_URL
read -p "🔐 توکن API پنل Hiddify: " HIDDIFY_API_KEY
read -p "🌍 دامنه با SSL معتبر برای Webhook (مثلاً yourdomain.com): " WEBHOOK_DOMAIN
read -p "📄 مسیر فایل fullchain.pem: " SSL_CERT
read -p "🔑 مسیر فایل privkey.pem: " SSL_KEY

# کلون کردن پروژه
git clone https://github.com/naseh42/hiddibot.git
cd hiddibot

# ساخت virtualenv
python3 -m venv venv
source venv/bin/activate

# نصب کتابخانه‌ها
pip install --upgrade pip
pip install -r requirements.txt flask

# ساخت فایل تنظیمات .env
echo "✅ ساخت فایل تنظیمات .env"
cat <<EOF > .env
BOT_TOKEN=$BOT_TOKEN
ADMIN_ID=$ADMIN_ID
MERCHANT_ID=$MERCHANT_ID
CALLBACK_URL=$CALLBACK_URL
HIDDIFY_API_URL=$HIDDIFY_API_URL
HIDDIFY_API_KEY=$HIDDIFY_API_KEY
EOF

# ثبت Webhook
echo "📮 ثبت Webhook در تلگرام..."
curl -X POST https://api.telegram.org/bot$BOT_TOKEN/setWebhook -d url=https://$WEBHOOK_DOMAIN/webhook

# ساخت سرویس systemd
SERVICE_PATH="/etc/systemd/system/hiddibot.service"
echo "⚙️ ساخت سرویس systemd در $SERVICE_PATH"

sudo bash -c "cat <<EOF > $SERVICE_PATH
[Unit]
Description=Hiddibot Telegram Bot (Webhook)
After=network.target

[Service]
WorkingDirectory=$(pwd)
ExecStart=$(pwd)/venv/bin/python3 $(pwd)/webhook_server.py
Restart=always
User=$USER

[Install]
WantedBy=multi-user.target
EOF"

# فعال‌سازی و اجرای سرویس
sudo systemctl daemon-reexec
sudo systemctl enable hiddibot
sudo systemctl start hiddibot

echo ""
echo "✅ نصب کامل شد و ربات اکنون به Webhook متصل است."
echo "📡 آدرس Webhook: https://$WEBHOOK_DOMAIN/webhook"
echo "📦 برای مشاهده وضعیت سرویس: sudo systemctl status hiddibot"
