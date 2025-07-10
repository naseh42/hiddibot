async def forward_receipt_to_admin(bot, message):
    from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
    keyboard = InlineKeyboardMarkup().add(
        InlineKeyboardButton("✅ تأیید", callback_data=f"confirm:{message.from_user.id}"),
        InlineKeyboardButton("❌ رد", callback_data="reject")
    )
    await bot.send_photo(ADMIN_ID, message.photo[-1].file_id, caption="رسید جدید", reply_markup=keyboard)
