import asyncio
import time


async def fetch_file():
    print('Starting to fetch a file')
    await asyncio.sleep(2)
    print('Fetching file completed')


async def main():
    print('Starting main')
    await asyncio.gather(
        fetch_file(),
        fetch_file(),
        fetch_file()
    )
    print('Main completed')


start = time.time()

asyncio.run(main())

end = time.time()

print('Execution time is ', end - start)
