#보건복지부 코로나 감염 현황
#2019부터 최근까지의 확진자수 시각화 & 지역별 확진자 분석?
import requests
import json
import xmltodict
import xml.etree.ElementTree as ET
import pandas as pd
import matplotlib.pyplot as plt

url_base = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson'
url_serviceKey = 'pX0Y2of8ZbhIipYRljRHmP3C2ClLB1x0oV98xwPX7WSYiKBpW7CS1e0BOnK/ZkfWQeEgghLzR58zDVYkA8l/Dg=='
page_No = '1000' #페이지 수
numOfRows = '1' #한 페이지 결과 수
startCreateDt = '20200101'
endCreateDt = '20210103'

url = url_base + '?serviceKey={0}&pageNo={1}&numOfRows={2}&startCreateDt={3}&endCreateDt={4}'\
      .format(url_serviceKey, page_No, numOfRows, startCreateDt, endCreateDt)

req = requests.get(url).content

#외부 모듈을 이용한 xml파싱 -> json
xml = xmltodict.parse(req)
#Json = json.loads(json.dumps(xml, indent=3))
data = xml['response']['body']['items']['item']
df = pd.DataFrame(data)
##df.head()
##df.info() #df.dtype

df = df.astype({'decideCnt' : 'int', 'examCnt': 'int', 'deathCnt': 'int'})

df = df.drop_duplicates(['stateDt']) #중복제거
#print(df.head)
df['date'] = df['stateDt']
df['date'] = pd.to_datetime(df['date']) #시계열 지정 ???????
df.set_index('date')

df2 = df[['date', 'decideCnt', 'examCnt', 'deathCnt']]
df2 = df2.sort_values(by='date') #diff() 사용해 날짜 오름차순 정렬
df2['daily_decideCnt'] = df2['decideCnt'].diff()
print(df2.head(30))

df2.plot('date', ['daily_decideCnt'])
plt.show()


# for d in Json:
#     data = d['response']['body']['items']['item']
#     df = pd.DateFrame(data)

#내부 모듈을 이용한 xml파싱
#root = ET.fromstring(req) #문자열에서 xml을 파싱한다
# for i in root.iter('createDt'): #문서 전체의 엘리먼트를 가져옴
#     print(i.tag, i.text) i.attrib, 이건 무슨값??

