# 시작전 구글과 tistory 로그인!

import requests
from bs4 import BeautifulSoup

import time
import re
import pandas as pd

import pyautogui as pg
import keyboard
import clipboard
import time
import random
import csv





headers = {'User-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"}
url = "https://www.11st.co.kr/browsing/BestSeller.tmall?method=getBestSellerMain&cornerNo=1"
res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, 'lxml')
food_list = soup.find('div', class_="best_prd_box").find_all('li')




max_n = 2
cur_n = 0
file_name = 'auto_blog\history.csv'
keyword = None

history_list = []
with open(file_name, 'r', newline='', encoding='utf-8') as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        history_list.append(row[0])

while cur_n < max_n:
    try:
            
        # 랜덤으로 생성 names과 urls로 구분

        num = random.randint(0,30)
        urls =[]
        names = []
        for food in food_list[num:num+10]:
            urls.append(food.a['href'])
            names.append(food.p.text.strip())

        # 전처리

        refined_name = []
        for i in names:
            bucket =[]
            for j in i.split():
                if j[0].isalpha() and len(j) > 1:
                    bucket.append(j)
            refined_name.append(' '.join(bucket))


        # 사진이 없을 경우 다른 상품으로 대체
        for i in range(10):

            today_name = refined_name[i]
            today_url = urls[i]

            res = requests.get(today_url)
            soup = BeautifulSoup(res.text, 'html.parser')
            keyword = soup.find('meta', attrs={'name':'keyword'})['content'].strip().split('>')[-1]

            # '기타' 문자 제거
            parts = keyword.split()
            if "기타" in parts:
                parts.remove("기타")
                keyword = " ".join(parts)
            else:
                pass
            
            # 최근 5개의 글과 중복될 경우 스킵
            if keyword in history_list[-5]:
                continue

            # 나무위키 이용
            res = requests.get(f'https://namu.wiki/w/{keyword}',headers=headers)
            soup = BeautifulSoup(res.text, 'html.parser')

            if soup.find('img', class_='vIrqy6Di'):

                if soup.find('img', class_='vIrqy6Di')['alt'] == '다른 뜻 아이콘':
                    print('사진 없음')
                    continue

                print(keyword)

                try: 
                    img = 'https:' + soup.find('img', class_='vIrqy6Di')['data-src']
                    print(img)
                    print('done')
                    break

                except Exception as e:
                    print(e, 'haha')
                    continue
            else:
                continue

        print(1)
        # 크롬이미지 확인 및 선택
        chrome = pg.locateOnScreen('auto_blog\images\chrome.png',confidence = 0.8)
        pg.click(chrome)

        loading = None
        while not loading:
            loading = pg.locateOnScreen('auto_blog\images\loading.png',confidence = 0.8)
            time.sleep(0.3)

        # gpt이미지
        gpt = pg.locateOnScreen('auto_blog\images\chatgpt.png',confidence = 0.8)
        pg.click(gpt)

        print(2)
        # 화면 크기 150%
        start = None
        while not start:
            start = pg.locateOnScreen('auto_blog\images\start.png',confidence = 0.8)
            time.sleep(0.3)

        time.sleep(random.uniform(0.5,0.8))

        pg.click(start)

        time.sleep(random.uniform(1,2))
        print(3)
        # 질문
        text = f'({today_name})이 것의 메인 재료로 블로그 글을 작성해줘 (제목: )과 (본문: )형식으로 나누고 효능과 부작용 기타 지식 해시태그를 1500자 분량으로 적어줘'
        clipboard.copy(text)
        pg.hotkey('ctrl','v')
        pg.press('enter')

        # 대답이 나올 때까지 대기
        where = None
        while not where:
            where = pg.locateOnScreen('auto_blog\images\done.png',confidence = 0.8)
            time.sleep(0.5)

        # 상단 이동
        print(4)
        pg.click(x=1058, y=339)
        time.sleep(0.5)
        pg.press('home')
        time.sleep(5)

        copy = None
        while not copy:
            copy = pg.locateOnScreen('auto_blog\images\copy.png', confidence = 0.8)
            time.sleep(0.3)

        pg.click(copy)

        text = clipboard.paste()
        print(5)
        # 제목, 타이틀, 해시태그 지정
        try:
            title = re.search(r'제목: "(.*)"', text).group(1)
        except:
            title = re.search(r'제목: (.*)', text).group(1)
        match = re.search(r'본문:(.*)', text, re.DOTALL)

        if match:
            content, hashtag = match.group(1).split('#', 1)
            hashtag = '#'+hashtag
            hashtag = hashtag[:hashtag.rfind('#')-1]
            content = content[:content.rfind('.')+1]

        time.sleep(3) 
        print(6)

        # t story url
        clipboard.copy('https://jamis.tistory.com/manage/newpost/?type=post&returnURL=%2Fmanage%2Fposts%2F')

        # 새 창 열기
        pg.click(pg.locateOnScreen('auto_blog\images\\new_tab.png', confidence=0.9))
        time.sleep(random.uniform(0.5,0.7))

        pg.hotkey('ctrl','v')

        time.sleep(random.uniform(0.3,0.7))

        pg.press('enter')

        time.sleep(random.uniform(0.8,1))
        print(7)

        # 작성 중이던 것이 있는가
        time.sleep(1)
        if pg.locateOnScreen('auto_blog\images\cancle.png', confidence=0.9):
            pg.click(pg.locateOnScreen('auto_blog\images\cancle.png', confidence=0.9))

        time.sleep(random.uniform(0.3,0.7))


        pg.press('tab')

        # 새 창 열기
        pg.click(pg.locateOnScreen('auto_blog\images\\new_tab.png', confidence=0.9))
        time.sleep(random.uniform(0.5,0.7))

        clipboard.copy(img)
        pg.hotkey('ctrl', 'v')
        pg.press('enter')

        time.sleep(random.uniform(0.5,0.7))

        pg.click(x=989, y=601)
        time.sleep(0.1)
        print(8)
        pg.hotkey('ctrl', 'c')
        time.sleep(0.1)

        pg.hotkey('ctrl', 'w')
        time.sleep(0.1)

        pg.hotkey('ctrl', 'v')
        time.sleep(2)

        pg.click(pg.locateOnScreen('auto_blog\images\explain.png', confidence=0.9))
        clipboard.copy(keyword+' (나무위키)')
        pg.hotkey('ctrl', 'v')
        pg.press('enter')

        time.sleep(random.uniform(0.5,0.7))


        pg.press('tab')

        # 해시태그 작성
        clipboard.copy(hashtag)
        pg.hotkey('ctrl', 'v')

        # 카테고리 설정
        pg.click(pg.locateOnScreen('auto_blog\images\category.png', confidence=0.9))
        time.sleep(random.uniform(0.5,0.7))

        pg.click(pg.locateOnScreen('auto_blog\images\\food.png', confidence=0.9))
        time.sleep(random.uniform(0.5,0.7))
        print(9)

        # 마크다운 설정
        pg.click(pg.locateOnScreen('auto_blog\images\select_mode.png', confidence=0.9))
        time.sleep(random.uniform(0.5,0.7))
        pg.click(pg.locateOnScreen('auto_blog\images\select_markdown.png', confidence=0.9))
        time.sleep(random.uniform(0.5,0.7))
        pg.click(pg.locateOnScreen('auto_blog\images\ok.png', confidence=0.9))
        time.sleep(random.uniform(0.5,0.7))


        # 작성 탭으로 이동
        for _ in range(4):
            pg.press('tab')
            time.sleep(0.2)

        # 타이틀 작성
        clipboard.copy(title)
        pg.hotkey('ctrl', 'v')

        for _ in range(2):
            pg.press('tab')
            time.sleep(0.4)
        pg.press('end')
        pg.press('enter')
        pg.press('enter')

        print(10)
        # 컨텐츠 작성
        clipboard.copy(content)
        pg.hotkey('ctrl', 'v')
        pg.press('tab')

        time.sleep(random.uniform(0.3,0.7))

        # 작성 완료 버튼
        pg.click(pg.locateOnScreen('auto_blog\images\complete.png', confidence=0.9))
        time.sleep(random.uniform(0.3,0.7))

        # 태그 설정
        pg.click(pg.locateOnScreen('auto_blog\images\\no_select.png', confidence=0.9))
        time.sleep(random.uniform(0.3,0.7))
        pg.click(pg.locateOnScreen('auto_blog\images\lifeinfo.png', confidence=0.9))
        time.sleep(random.uniform(0.3,0.7))

        # 발행 완료
        pg.click(pg.locateOnScreen('auto_blog\images\\final.png', confidence=0.9))
        time.sleep(random.uniform(0.3,0.7))
        print(11)
    except Exception as e:
        print(e)
        cur_n += 1
        print(cur_n)
        continue

    
    # 작업이 완료되면 history에 저장, 같은 글을 다시 쓰지 않기 위해

    with open(file_name, 'a', newline='', encoding='utf-8') as f:
        csv_writer = csv.writer(f)
        if keyword is not None:
            csv_writer.writerow([f'{keyword}'])
