import requests as res
import pandas as pd 
from bs4 import BeautifulSoup

# 宣告下載PDF檔案的function
def downloadPDF(group,subject,year,link):
    response = res.get(link) # 先發出第一階段的請求(網址結尾不是.pdf)(會透過java script跳轉)
    pdf_url = response.text.replace("<script language=JavaScript>top.location.href='","").replace("';</script>","") # 擷取真正的.pdf網址
    print(pdf_url)
    response = res.get(pdf_url)
    file_name = "["+year+"]["+group+"]["+subject+"].pdf"
    file_name = file_name.replace('\r','').replace('\n','')
    open('./files/'+file_name, "wb").write(response.content)


# 宣告取得總頁數的function
def getPage (url):
    r = res.get(url)
    # 利用bs4解析原始碼
    soup = BeautifulSoup(r.text,"html.parser")
    total_page = soup.find("div", class_="page").text
    total_page = total_page.replace('第 1 頁,共 ','').replace('第 0 頁,共 ','')
    #print(total_page)
    tmp = '' 
    for i in range(len(total_page)): # 字串處理
        if(total_page[i]!=' '):
            tmp+=total_page[i]
        else:
            break
    #print(tmp)
    tmp = int(tmp)
    return tmp
