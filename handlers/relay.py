from aiogram import Router, F, Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from states.chat import ChatStates
from utils.auto_delete import add_to_delete_queue, delete_previous_messages

router = Router()

@router.message(ChatStates.in_chat, F.content_type.in_({'text', 'photo', 'video', 'voice', 'document', 'sticker'}))
async def relay_message(message: Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    partner_id = data.get("partner_id")
    session_id = data.get("session_id")
    
    if not partner_id:
        return await message.answer("Suhbatdosh topilmadi yoki chat yakunlangan.")

    # 1. Oldingi xabarlarni tozalash (Clean UI)
    await delete_previous_messages(bot, message.from_user.id, state)

    # 2. Xabarni sherigiga anonim jo'natish (copy_message orqali ID va username yashiriladi)
    try:
        sent_msg = await message.send_copy(chat_id=partner_id)
        
        # 3. Vaqtincha xabarlarni saqlash (Auto-delete logikasi uchun)
        await add_to_delete_queue(state, message.message_id)
        await add_to_delete_queue(state, sent_msg.message_id, is_partner=True)

        # 4. Moderatsiya va Audit uchun bazaga yozish (background task sifatida ishlashi tavsiya etiladi)
        # await db.save_message_log(session_id, message.from_user.id, sent_msg.message_id, message.content_type)
        
    except Exception as e:
        await message.answer("Xabar yetkazilmadi. Balki suhbatdosh botni bloklagan.")
        await state.clear()