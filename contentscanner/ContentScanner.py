import asyncio

from .exceptions.exceptions import *
from aiohttp import ClientSession
from requests import get


class ContentScanner:

    def __init__(self, url: str, worldlist_path: str) -> None:
        self.__url_check(url)
        self.__url = url + '/'
        self.__wordlist_path: str = worldlist_path

    @staticmethod
    def __url_check(url: str) -> None:
        try:
            get(url)
        except Exception:
            raise ExceptionUrl

    def __get_words(self) -> str:
        try:
            for row in open(self.__wordlist_path, "r"):
                yield row
        except Exception:
            raise ExceptionGetWordlist

    async def __fetch(self, session: ClientSession, word: str) -> None:
        async with session.get(self.__url + word) as resp:
            if resp.status == 200:
                print(word)

    async def scan(self) -> None:
        print(" ~ Found ~ ")
        task = []
        async with ClientSession() as session:
            for word in self.__get_words():
                task.append(asyncio.ensure_future(self.__fetch(session, word)))
            await asyncio.gather(*task, return_exceptions=True)
        print(' ~ - ~ ')
