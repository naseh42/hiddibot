async def save_backup(user_id, config_link):
    from datetime import datetime
    import aiosqlite
    async with aiosqlite.connect("data.db") as db:
        await db.execute("INSERT INTO backups VALUES (?, ?, ?)",
                         (user_id, config_link, datetime.now().isoformat()))
        await db.commit()
