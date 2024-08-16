import time

import requests


# 单线程版下载
def download_one(url):
    resp = requests.get(url)
    print("read {} from {}".format(len(resp.content), url))


def download_all(sites):
    for site in sites:
        download_one(site)


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
    download_all(sites)
    end_time = time.perf_counter()
    print("单线程版下载了{}个网站，耗时{}".format(len(sites), end_time - start_time))
