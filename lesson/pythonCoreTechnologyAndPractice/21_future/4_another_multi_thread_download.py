import concurrent.futures
import time

import requests


def download_one(url):
    resp = requests.get(url)
    print("read {} from {}".format(len(resp.content), url))
    return 'OK {}'.format(url)


# another多线程版下载
def download_all_futures(sites):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        to_do = []
        # to_do = [executor.submit(download_one, site) for site in sites]
        for site in sites:
            future = executor.submit(download_one, site)
            to_do.append(future)
        for future in concurrent.futures.as_completed(to_do):
            print(future.result())


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
    download_all_futures(sites)
    end_time = time.perf_counter()
    print("another多线程版下载了{}个网站，耗时{}".format(len(sites), end_time - start_time))
