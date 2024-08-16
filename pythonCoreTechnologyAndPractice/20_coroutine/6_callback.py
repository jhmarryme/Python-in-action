import asyncio


async def crawl_page(url):
    print('crawling {}'.format(url))
    sleep_time = int(url.split('_')[-1])
    await asyncio.sleep(sleep_time)
    return 'OK {}'.format(url)


async def main(urls):
    tasks = [asyncio.create_task(crawl_page(url)) for url in urls]
    for task in tasks:
        # 对 task 对象调用 add_done_callback() 函数，即可绑定特定回调函数
        # 可以通过 future.result() 来获取协程函数的返回值
        task.add_done_callback(lambda future: print('result: ', future.result()))
    await asyncio.gather(*tasks)


asyncio.run(main(['url_1', 'url_2', 'url_3', 'url_4']))
