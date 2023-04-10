from img_crawling import *
import threading

def Ohu(count):
    count += 1
    print(count)
    
    page_n = 0
    for page_n in range(1,3):
        url = 'http://www.todayhumor.co.kr/board/list.php?table=bestofbest&page={0}'\
            .format(page_n)
        c1 = TEXT(url)

        c1.text_ver()

        link_s = []
        title_s = []
    
        c1.text_find('list_ad')
    
        for link_n in range(5):
            #c1.text_find('view list_tr_humordata', 'subject', 2)
            c1.text_find('view list_tr_humordata')
            c1.text_find('subject')
            
            link = c1.text_core('a href="', '" target', 8)
            link = 'http://www.todayhumor.co.kr' + link

            title = c1.text_core('top">', '</a><span', 5)

            link_s.append(link)
            title_s.append(title)
        #print(link_s, title_s)

        title_n = 0
        for url in link_s:
            c2 = TEXT(url)
            c2.text_ver()

            c2.html = c2.text_core('viewContent', '--viewContent--',0,0,0)

            cnt = 0
            while (1):
                if c2.html.find('src="') < 0: break
                c2.html = c2.html[3:]

                img = c2.text_core('http:', '"')
               #### if img in ''

                fname = 'OHU/{0}page_{1}_{2}.jpg'.format(page_n, title_s[title_n], cnt)
                i = IMG_SAVE(img, fname)
                i.img_save()
                cnt += 1
                delay(2)

            title_n += 1
            delay(3)
            print('링크 닫음')
        page_n += 1
        delay(1)
        print('페이지 닫음')
        

    if  count < 1000:
        timer = threading.Timer(10, Ohu, args=[count])
        timer.start()

print('starting timer~')
Ohu(0)

