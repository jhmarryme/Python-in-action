import concurrent.futures
import time

import requests


def download_one(url):
    resp = requests.get(url)
    print("read {} from {}".format(len(resp.content), url))


# 并行版
def download_all_futures_parallel(sites):
    # 并行使用ProcessPoolExecutor, 并发使用ThreadPoolExecutor
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(download_one, sites)


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
    download_all_futures_parallel(sites)
    end_time = time.perf_counter()
    print("并行版下载了{}个网站，耗时{}".format(len(sites), end_time - start_time))
