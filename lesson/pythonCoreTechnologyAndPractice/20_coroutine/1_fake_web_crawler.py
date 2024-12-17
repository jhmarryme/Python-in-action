import time


def crawl_page(url):
    print('crawling {}'.format(url))
    sleep_time = int(url.split('_')[-1])
    time.sleep(sleep_time)
    print('OK {}'.format(url))


def main(urls):
    for url in urls:
        crawl_page(url)


start = time.perf_counter()
main(['url_1', 'url_2', 'url_3', 'url_4'])
end = time.perf_counter()
print("常规爬虫运行耗时{}秒".format(end - start))
