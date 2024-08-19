import asyncio
import time

import aiohttp


# 异步网页下载
async def download_one(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            print("read {} from {}".format(resp.content_length, url))


async def download_all(sites):
    tasks = [asyncio.create_task(download_one(site)) for site in sites]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    sites = [
        'http://www.dapenti.com/blog/readforwx.asp?name=xilei&id=143655',
        'http://www.dapenti.com/blog/readforwx.asp?name=xilei&id=143656',
        'http://www.dapenti.com/blog/readforwx.asp?name=xilei&id=143657',
        'http://www.dapenti.com/blog/readforwx.asp?name=xilei&id=143658',
        'http://www.dapenti.com/blog/readforwx.asp?name=xilei&id=143659',
        'http://www.dapenti.com/blog/readforwx.asp?name=xilei&id=143660',
        'http://www.dapenti.com/blog/readforwx.asp?name=xilei&id=143661',
        'http://www.dapenti.com/blog/readforwx.asp?name=xilei&id=143662'
    ]
    start_time = time.perf_counter()
    asyncio.run(download_all(sites))
    end_time = time.perf_counter()
    print("异步版下载了{}个网站，耗时{}".format(len(sites), end_time - start_time))
