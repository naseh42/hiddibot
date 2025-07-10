import aiosqlite

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
        CREATE TABLE IF NOT EXISTS discounts (
            code TEXT PRIMARY KEY,
            amount INTEGER,
            type TEXT,  -- percent / fixed
            expires TEXT
        )""")
        await db.execute("""
        CREATE TABLE IF NOT EXISTS backups (
            telegram_id INTEGER,
            config_link TEXT,
            created_at TEXT
        )""")
        await db.commit()
