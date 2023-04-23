import asyncio

async def diz_oi_demorado():
    print('Oi', end=' ', flush=True)
    await asyncio.sleep(2)
    print('Todos')


if __name__ == '__main__':
    # diz_oi()
    event_loop1 = asyncio.get_event_loop()
    event_loop1.run_until_complete(diz_oi_demorado())
    event_loop1.close()

