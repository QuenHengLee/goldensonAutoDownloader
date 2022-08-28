import requests as res
import pandas as pd 
from bs4 import BeautifulSoup
from  functions import downloadPDF,getPage

# 設定搜尋條件(關鍵字/篩選方式/年份)
set_keyword = '行政'
set_year = ''  # 西元年 (空白代表不限制)
set_filter = 'P' # D代表以 考試類組  P代表以 考試科目 (空白代表不限制)
#---------------------

# 第一頁連結(為了找出總頁數用)
initial_url = 'http://goldensun.get.com.tw/exam/List.aspx?iPageNo=1&sFilter='+set_keyword+'&sFilterDate='+set_year+'&sFilterType='+set_filter
# initial_url = 'http://goldensun.get.com.tw/exam/List.aspx?iPageNo=1&sFilter=%e8%b3%87%e8%a8%8a&sFilterType=0'
total_page = getPage(initial_url) # 呼叫擷取總頁數function

# 迴圈執行多頁
for i in range(1,total_page+1):
    print("目前位於第:"+str(i)+"頁")
    page = str(i)
    url = 'http://goldensun.get.com.tw/exam/List.aspx?iPageNo='+page+'&sFilter='+set_keyword+'&sFilterDate='+set_year+'&sFilterType='+set_filter
    print(url)
    print(url)
    r = res.get(url)

    # 利用bs4解析原始碼
    soup = BeautifulSoup(r.text,"html.parser")
    # print(soup.prettify())

    # 擷取考古題列表
    exam_list = soup.find_all('tr') 
    #print(exam_list)
    exam_list.pop(0) # 資料清洗 移除快速搜尋、標頭
    exam_list.pop(0)

    # # 建立datafrmae存放考古題
    # df = pd.DataFrame(columns = ['index','group','subject','year','link'])


    # 針對每一考古題(列)進行處理
    for exam in exam_list:
        ex_info = exam.find_all('td') # 將各個tr中許多td分割
        # print(ex_info)
        index = BeautifulSoup(ex_info[0].text,"html.parser").text
        group = BeautifulSoup(ex_info[1].text,"html.parser").text
        subject = BeautifulSoup(ex_info[2].text,"html.parser").text
        year = BeautifulSoup(ex_info[3].text,"html.parser").text
        link = 'http://goldensun.get.com.tw/exam/' + ex_info[4].find('a').get('href').replace('./','')

        # # 將考古題新增至dataframe
        # df = df.append({'index':index, 'group':group, 'subject':subject, 'year':year, 'link':link}, ignore_index=True)

        print('編號:'+index)
        print('類組:'+group)
        print('科目:'+subject)
        print('年度:'+year)
        print('連結:'+link)
        #downloadPDF(group,subject,year,link)
        print('--------------------')

    
#print(df)
# print(exam_list[0].find_all('td'))



# 擷取所有連結
# for link in soup.find_all('a'):
#     print(link.get('href'))