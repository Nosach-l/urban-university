import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for i in range(5):
        await asyncio.sleep((i+1) / power)

        print(f'Силач {name} поднял шар №{i + 1}')
    print(f'Силач {name} закончил соревнования')


async def start_tournament():
    strongmen_1 = asyncio.create_task(start_strongman('Pasha', 3))
    strongmen_2 = asyncio.create_task(start_strongman('Denis', 4))
    strongmen_3 = asyncio.create_task(start_strongman('Apollo', 5))
    await strongmen_1
    await strongmen_2
    await strongmen_3


asyncio.run(start_tournament())
