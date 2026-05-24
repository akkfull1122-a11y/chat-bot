from aiogram import BaseMiddleware
from aiogram.types import Message
from cachetools import TTLCache
import logging

class ThrottlingMiddleware(BaseMiddleware):
    def __init__(self, rate_limit: int = 2):
        self.cache = TTLCache(maxsize=10000, ttl=rate_limit)

    async def __call__(self, handler, event: Message, data: dict):
        if event.from_user.id in self.cache:
            # Spam aniqlandi, rate limit
            return 
        self.cache[event.from_user.id] = True
        return await handler(event, data)