import requests
import urllib
import time

page_n = 1
for url_n in range(1, 3):
    url = 'http://www.todayhumor.co.kr/board/list.php?table=bestofbest&page={0}'\
        .format(url_n)

    head = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0 rv:11.0) like Gecko'
    }

    site = requests.get(url, headers=head)
    html = site.text

    link_s = []
    title_s = []

    pos0 = html.find('list_ad')
    html=html[pos0+1:]

    for link_n in range(5):
        pos = html.find('view list_tr_humordata')
        html = html[pos+1:]
        pos1 = html.find('subject')
        html = html[pos1+1:]

        pos2 = html.find('a href="')
        pos3 = html.find('" target')
        link = html[pos2+8:pos3]
        link = 'http://www.todayhumor.co.kr' + link
        html = html[pos3+1:]

        pos4 = html.find('top">')
        pos5 = html.find('</a><span')
        title = html[pos4+5:pos5]
        html = html[pos5+1:]

        link_s.append(link)
        title_s.append(title)
    #print(link_s, title_s)

    title_n = 0
    for url in link_s:
        head = {
        'User-Agnet':'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0 rv:11.0) like Gecko'
        }

        site = requests.get(url, headers=head)
        html = site.text

        pos1 = html.find('viewContent')
        pos2 = html.find('--viewContent--')
        html = html[pos1:pos2]

        cnt = 0
        while (1):
            pos1 = html.find('src="')
            if pos1 <1: break
            html = html[pos1+1:]

            pos2 = html.find('http:')
            pos3 = html.find('.jpg')
            if pos3 < 0:
                pos3 = html.find('.png')
            img = html[pos2:pos3+4]
            html = html[pos3+1:]

            fname = './OHU/{0}page_{1}_{2}.jpg'.format(page_n, title_s[title_n], cnt)

            try:
                print(img)
                urllib.request.urlretrieve(img, fname)
                cnt+=1
            except Exception as e:
                print(img, fname, e)
            time.sleep(3)

        title_n += 1
        time.sleep(1)
        print('링크 닫음')
    page_n += 1
    time.sleep(1)
    print('페이지 닫음')
