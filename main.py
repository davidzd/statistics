# coding=utf-8
from bs4 import BeautifulSoup
import random
import urllib2
import threading


def get_random_ppt(url_list):
    index = 'http://www.docin.com/'
    soup = BeautifulSoup(urllib2.urlopen(url_list[random.choice(url_list.keys())]).read(), "html.parser")
    ppt_list = soup.find_all("dd", {"class": "title"})
    rannum= random.randint(0, len(ppt_list) - 1)
    print rannum
    ppt_select = ppt_list[rannum]
    print ppt_select.text, index + ppt_select.a.get('href')


def starter(n):
    index = 'http://www.docin.com/'
    response = urllib2.urlopen(index + 'list.html')
    soup = BeautifulSoup(response.read(), "html.parser")

    url_list = dict()
    tags = soup.find(id='tabList').find_all('a')

    for tag in tags:
        url_list[tag.get_text()] = tag.get('href')
    result_url = []
    threads = []
    for i in range(n):
        threads.append(threading.Thread(target=get_random_ppt, args=(url_list, )))
    for thread in threads:
        thread.start()


starter(10)
