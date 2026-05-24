from aiogram import Router, F
from aiogram.types import Message
from config import config

router = Router()
router.message.filter(F.from_user.id.in_(config.ADMIN_IDS))

@router.message(F.text.startswith("/audit "))
async def audit_session(message: Message):
    # Faqat qonuniy sabab bilan (masalan, foydalanuvchi report qilgan chatni tekshirish)
    session_id = message.text.split(" ")[1]
    
    # DB dan ushbu session loglarini chaqirish
    # logs = await db.get_reported_logs(session_id)
    
    await message.answer(f"🔒 Session {session_id} audit natijalari:\n\n"
                         f"Bu yerda faqat tizim yoki foydalanuvchi tomonidan xavfli deb topilgan "
                         f"xabarlar ko'rsatiladi.")