from aiogram import Router, Bot
from aiogram.filters import CommandStart
from aiogram.types import Message, FSInputFile, ChatJoinRequest
from tgbot.keyboards.inline import keyboard
import time
user_router = Router()


@user_router.message(CommandStart())
async def user_start(message: Message, bot: Bot):
    await message.reply("Швидке привітання")
    time.sleep(2)
    # await message.answer_video(FSInputFile('IMG_0285.MOV'))

    await message.answer_video('BAACAgIAAxkBAANmZTzzyymVnBgvq6jHYfOE2GVbGFwAAo4zAAIWn-lJ7WFetEonofQwBA')
    # await bot.send_message(chat_id='6256621695', text='test')
    time.sleep(2)
    await message.reply( text='Виберіть професії ⏳',
                           reply_markup=keyboard)
@user_router.chat_join_request()
async def chat_join_request(join_request: ChatJoinRequest, bot: Bot):
    await bot.send_message(join_request.user_chat_id, 'Швидке привітання !')
    time.sleep(2)
    await join_request.approve()
    await bot.send_video(join_request.user_chat_id,'BAACAgIAAxkBAANmZTzzyymVnBgvq6jHYfOE2GVbGFwAAo4zAAIWn-lJ7WFetEonofQwBA')
    time.sleep(2)
    await bot.send_message(join_request.user_chat_id, text='Виберіть професії ⏳',
        reply_markup=keyboard)
