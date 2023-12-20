# -*- coding: utf-8 -*-
# @Author: JogFeelingVI
# @Date:   2023-12-16 16:04:18
# @Last Modified by:   JogFeelingVI
# @Last Modified time: 2023-12-18 10:43:52

from asyncio import as_completed
import html
from io import TextIOWrapper
import urllib.request, time, threading, re, queue, concurrent.futures

urls = [
    'http://www.python.org/', 'https://www.baidu.com',
    'https://www.google.com', 'https://sspai.com', 'https://www.appinn.com'
]


def thpool_craw():
    with concurrent.futures.ThreadPoolExecutor() as tpool:
        futs = {}
        # html = tpool.map(gethood, urls)
        # htmls = zip(urls, html)
        # for u, h in htmls:
        #     print(f'Http test {u} {len(h)}')
        htms = []
        for u in urls:
            fut = tpool.submit(gethood, u)
            futs[fut] = u
        for f in concurrent.futures.as_completed(futs):
            u = futs[f]
            h = f.result()
            htms.append((u, h))
            print(f'URL {u} {len(h)}')
        futs = {}
        for u, h in htms:
            f = tpool.submit(pares, h)
            futs[f] = u

        for f in concurrent.futures.as_completed(futs):
            u = futs[f]
            links = f.result()
            print(f'URL {u} links {len(links)}')


def do_gethood(uq: queue.Queue, pq: queue.Queue):
    while True:
        url = uq.get()
        html = gethood(url=url)
        pq.put((url, html))
        print(
            f'U {threading.current_thread().name} UQ {uq.qsize()} PQ {pq.qsize()}'
        )
        time.sleep(3)
        if uq.empty():
            break
    print(f'UQ {threading.current_thread().name} is END {time.time()}')


def do_pares(pq: queue.Queue, fp: TextIOWrapper):
    stime = []
    count_zone = 0
    while True:
        if pq.empty():
            stime.append(time.time())
            sts = stime[-2:]
            if sts.__len__() == 2:
                zone = sts[1] - sts[0]
                if zone < 1.01:
                    count_zone += 1
                    print(f'{threading.current_thread().name} is {count_zone}')
                if count_zone > 5:
                    break
            time.sleep(1)
            continue
        count_zone = 0
        stime.clear()
        u, h = pq.get()
        fp.write(f'link for {u} {time.time()}\n{"="*32}\n')
        href = pares(h)
        if href != None:
            for link in href:
                fp.write(f'{link}\n')
            print(
                f'P {threading.current_thread().name} PQ {pq.qsize()} URL {u} link {len(href)}'
            )
        time.sleep(3)


def do_wallking():
    uq = queue.Queue()
    pq = queue.Queue()
    for u in urls:
        uq.put(u)

    for idx in range(3):
        t = threading.Thread(target=do_gethood,
                             args=(uq, pq),
                             name=f'thr-{idx}')
        t.start()
    fp = open('02_links.log', '+w')
    for idx in range(2):
        t = threading.Thread(target=do_pares, args=(pq, fp), name=f'thw-{idx}')
        t.start()


def gethood(url: str):
    with urllib.request.urlopen(url=url) as fr:
        return fr.read().decode('utf-8')


def pares(html: str):
    '''
    <a href="https://www.appinn.com/chatgpt-guides/">ChatGPT 指南</a>
    '''
    href_link = []
    link = re.compile(r'<a(.*)a>')
    href = re.compile(r'(http|https)://([a-zA-Z0-9:./#-?]+)')
    if html == None or html == '':
        return None
    link_m = link.findall(html)
    for lm in link_m:
        href_m = href.findall(lm)
        for hm in href_m:
            h, m = hm
            href_link.append(f'{h}://{m}')
    print(f'Find href counts {href_link.__len__()}')
    return href_link


def mu_thread():
    print('wallking in thread')
    stime = time.time()
    thr = []
    for u in urls:
        thr.append(threading.Thread(target=gethood, args=(u, )))
    for t in thr:
        t.start()
    for t in thr:
        t.join()
    print(f'gethood wallking time use thread {time.time() - stime:.4f}')


def code():
    print("Hello, World!")
    stime = time.time()
    for u in urls:
        html = gethood(url=u)
        pares(html)
    print(f'gethood wallking time {time.time() - stime:.4f}')


if __name__ == "__main__":
    #code()
    #mu_thread()
    thpool_craw()
