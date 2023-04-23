import asyncio

async def diz_oi():
    print('Oi...')


if __name__ == '__main__':
    # diz_oi()
    event_loop1 = asyncio.get_event_loop()
    event_loop1.run_until_complete(diz_oi())
    event_loop1.close()
