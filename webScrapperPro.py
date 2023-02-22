from selenium import webdriver
from bs4 import BeautifulSoup
import csv
import time

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars" 
browser = webdriver.Chrome("C:/Users/drbis/Downloads/chromedriver_win32/chromedriver")
browser.get(START_URL)
time.sleep(10)
 
def scrape():
    headers=["Proper name","Distance","Mass","Radius","Luminosity"]
    star_data=[]
    for i in range(0,522):
        soup = BeautifulSoup(browser.page_source,"html.parser")
        for tr_tag in soup.find_all("tr",attrs={"class","brightestStar"}):
            th_tags=tr_tag.find_all("th")
            temp_list=[]
            for index,th_tag in enumerate(th_tags):
                if index==0:
                    temp_list.append(th_tag.find_all("a")[0].contents[0])

                else:
                    try:
                        temp_list.append(th_tag.contents[0])
                    except:
                        temp_list.append("")

            star_data.append(temp_list)  
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    with open("scrapper1.csv","w",encoding="utf-8") as f:
        csvwriter = csv.writer(f)                  
        csvwriter.writerow(headers)
        csvwriter.writerow(star_data)
scrape()                          
    
   
     
