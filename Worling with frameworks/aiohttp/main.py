import aiohttp
import asyncio
import aiofiles


async def file_sender(file_name=None):
    async with aiofiles.open(file_name, 'rb') as f:
        chunk = await f.read(64 * 1024)
        while chunk:
            yield chunk
            chunk = await f.read(64 * 1024)


async def main():
    async with aiohttp.ClientSession("http://httpbin.org") as session:
        async with session.post('/post', data=file_sender('text.txt')) as resp:
            async for chunk in resp.content.iter_chunked(500):
                print(chunk, end='')


async def day2():
    async with aiohttp.ClientSession('http://example.com') as session:
        payload = b'GIF89a\x01\x00\x01\x00\x00\xff\x00,\x00\x00'\
                  b'\x00\x00\x01\x00\x01\x00\x00\x02\x00;'
        headers = {'content-type': 'image/gif'}
        async with session.post('/image', data=payload, headers=headers) as resp:
            print(resp)

asyncio.run(day2())
