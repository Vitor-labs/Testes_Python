import asyncio
import time


def coroutine():
    start = time.time()
    print('inicio')
    yield
    end = time.time()
    print('fim')
