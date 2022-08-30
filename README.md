# goldensonAutoDownloader 高上公職考古題自動下載工具

## 大綱
本專案是利用Python爬蟲將(高點)高上公職網站的歷屆考古題自動下載至本機端，大幅降低下載大量考古題時所需花費的時間、操作。其中可篩選的項目是依照高點官網上所提供的篩選方式，使用者可在短時間熟悉該工具的使用方法。
  
---
### 一、開發背景
過去曾在高點補過公職，其官方網站提供各類科豐富的考古題，雖說內容完整且分類得十分清楚，但在使用者欲大量下載檔案時就會需要重複執行多次相同的步驟，官網又沒有提供如同檔案總管可以選取、全選等功能，所以我想**做一個小工具能夠一口氣下載大量的考古題檔案，不需要將枯燥的步驟一再的操作，打造一個友善的人機介面**。
### 二、使用工具
**1. BeautifulSoup 套件:** 將擷取下來的html原始碼進行切割、分析，擷取出真正需要的資料。

**2. Request 套件:** 模擬瀏覽器發出request至高點官網伺服器。

**3. py-to-exe 套件:** 將原始.py檔案打包成.exe檔案方便提供給其他需要的人使用。
### 三、程式碼簡介
**1. 篩選功能與官網相同**

   (1). 官方篩選畫面 
   ![](https://i.imgur.com/sQiLa4X.png)
   (2). 自動下載工具篩選程式碼

``` python=
#----------------使用者自訂區---------------------

# 設定搜尋條件(關鍵字/篩選方式/年份)
set_keyword = '行政'
set_year = '2022'  # 西元年 (空白代表不限制)
set_filter = 'P' # D代表以 考試類組  P代表以 考試科目 (空白代表不限制)

#----------------使用者自訂區---------------------
```
    
**2. 手動清洗、整理原始資料(Raw Data)**
``` python=
# 利用bs4解析原始碼
soup = BeautifulSoup(r.text,"html.parser")
# print(soup.prettify())

# 擷取考古題列表
exam_list = soup.find_all('tr') 
exam_list.pop(0) # 資料清洗 移除快速搜尋、標頭
exam_list.pop(0)
``` 

**3. 將下載url透過javascript跳轉至真正的.pdf網址，並下載至本機端**
``` python=
# 宣告下載PDF檔案的function
def downloadPDF(group,subject,year,link):
    response = res.get(link) # 先發出第一階段的請求(網址結尾不是.pdf)(會透過java script跳轉)
    pdf_url = response.text.replace("<script language=JavaScript>top.location.href='","").replace("';</script>","") # 擷取真正的.pdf網址
    print(pdf_url)
    response = res.get(pdf_url)
    file_name = "["+year+"]["+group+"]["+subject+"].pdf"
    file_name = file_name.replace('\r','').replace('\n','')
    open('./files/'+file_name, "wb").write(response.content)
```


### 四、完成畫面 
**1. 官方提供之考古題清單(需一個個點擊右方連結)** 
![](https://i.imgur.com/uaYAG8d.png)
**2.利用爬蟲程式自動下載至本機端結果**
![](https://i.imgur.com/wkAMdQj.png)
**3. 實際操作本系統影片(點即可查看影片)**
https://www.youtube.com/watch?v=0fN0Ja65dFk&feature=emb_logo
[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/0fN0Ja65dFk/0.jpg)](https://www.youtube.com/watch?v=0fN0Ja65dFk)
 



 
