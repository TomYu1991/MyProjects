import requests
from bs4 import BeautifulSoup
import xlwt



if __name__=='__main__':
    numbers = []
    for dateNum in range(10001,10153):
        numbersChild=[]
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36'
        }
        res = requests.get('http://kaijiang.500.com/shtml/dlt/%s.shtml' %dateNum, headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')
        ball_red = soup.find_all('li', 'ball_red')
        ball_blue = soup.find_all('li', 'ball_blue')
        numbersChild.append(dateNum)
        for red in ball_red:
            numbersChild.append(red.text)
        for blue in ball_blue:
            numbersChild.append(blue.text)
        numbers.append(numbersChild)
        # print(numbers)
        print('第%s期开奖结果解析成功...' %dateNum)
    i=1
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet('2010')
    sheet.write(0,0,'期数')
    sheet.write(0,1,'红区-1')
    sheet.write(0,2,'红区-2')
    sheet.write(0,3,'红区-3')
    sheet.write(0,4,'红区-4')
    sheet.write(0,5,'红区-5')
    sheet.write(0,6,'蓝区-1')
    sheet.write(0,7,'蓝区-2')
    for number in numbers:
        sheet.write(i,0,number[0])
        sheet.write(i,1,number[1])
        sheet.write(i,2,number[2])
        sheet.write(i,3,number[3])
        sheet.write(i,4,number[4])
        sheet.write(i,5,number[5])
        sheet.write(i,6,number[6])
        sheet.write(i,7,number[7])
        i+=1
        print('第%s行数据插入成功...' %i)
    print('所有数据插入成功...')
    workbook.save('d:/2010年大乐透开奖结果.xls')