import requests
import re
import csv
import random
import datetime

import time

page_num = 1
now_time = datetime.datetime.now()
now_time = now_time.strftime('%Y%m%d')

start_url = [
    'https://www.amazon.com/s/ref=sr_pg_' + str(
        page_num) + '?rh=n%3A2335752011%2Cn%3A%212335753011%2Cn%3A7072561011%2Cp_89%3AHuawei&page=' + str(
        page_num) + '&ie=UTF8&qid=1544060985&ajr=3',
    'https://www.amazon.com/s/ref=sr_pg_' + str(
        page_num) + '?fst=as%3Aoff&rh=n%3A2335752011%2Cn%3A%212335753011%2Cn%3A7072561011%2Cn%3A2407749011%2Cp_89%3ASamsung&page=' + str(
        page_num) + '&bbn=2407749011&ie=UTF8&qid=1544077676&ajr=3',

]


# 设置请求头
def randHeader():
    head_connection = ['Keep-Alive', 'close']
    head_accept = ['text/html, application/xhtml+xml, */*']
    head_accept_language = ['zh-CN,fr-FR;q=0.5', 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3']
    head_user_agent = ['Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
                       'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.95 Safari/537.36',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; rv:11.0) like Gecko)',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070309 Firefox/2.0.0.3',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070803 Firefox/1.5.0.12',
                       'Opera/9.27 (Windows NT 5.2; U; zh-cn)',
                       'Mozilla/5.0 (Macintosh; PPC Mac OS X; U; en) Opera 8.0',
                       'Opera/8.0 (Macintosh; PPC Mac OS X; U; en)',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.12) Gecko/20080219 Firefox/2.0.0.12 Navigator/9.0.0.6',
                       'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Win64; x64; Trident/4.0)',
                       'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0)',
                       'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET4.0C; .NET4.0E)',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Maxthon/4.0.6.2000 Chrome/26.0.1410.43 Safari/537.1 ',
                       'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET4.0C; .NET4.0E; QQBrowser/7.3.9825.400)',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0 ',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.92 Safari/537.1 LBBROWSER',
                       'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; BIDUBrowser 2.x)',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/3.0 Safari/536.11']

    header = {
        'Connection': head_connection[0],
        'Accept': head_accept[0],
        'Accept-Language': head_accept_language[1],
        'User-Agent': head_user_agent[random.randrange(0, len(head_user_agent))]
    }
    return header


# 某品牌每个手机的URL

def get_phone_url_list(url):
    # url = 'https://www.amazon.com/s/ref=sr_pg_1?rh=n%3A2335752011%2Cn%3A%212335753011%2Cn%3A7072561011%2Cp_89%3AHuawei'
    header = randHeader()
    response = requests.get(url, headers=header, timeout=20)
    result = response.text  # hesder判断编码   UTF-8
    # print(result)
    reg = r'data-asin="(.*?)"'
    phone_url_list = re.findall(reg, result, re.S)  # 得到一个列表
    # reg1 = r'<a href="https://www.amazon.com/dp/(.*?)/ref'
    # other_url = re.findall(reg1,result)
    # print(other_url)
    s = 'https://www.amazon.com/dp/'
    for i in range(len(phone_url_list)):
        phone_url_list[i] = s + phone_url_list[i]
    # print(phone_url_list)
    return phone_url_list


# 每台手机所有类别   不同颜色....
'''
def get_phone_all_url(url):
    header = randHeader()
    response = requests.get(url,headers=header,timeout=20)
    result = response.text  # hesder判断编码   UTF-8
    reg = r'data-defaultAsin="(.*?)"'
    phone_all_url_list = re.findall(reg, result, re.S)
    for i in phone_all_url_list:
        if i == '':
            phone_all_url_list.remove('')
        else:continue
    s = 'https://www.amazon.com/dp/'
    if phone_all_url_list:
        for i in range(len(phone_all_url_list)):
            phone_all_url_list[i] = s + phone_all_url_list[i]
    else:
        phone_all_url_list.append(url)
    print(phone_all_url_list)
    return phone_all_url_list
'''


# 得到手机的信息
def get_phone_config(url):
    header = randHeader()
    response = requests.get(url, headers=header, timeout=20)
    result = response.text  # hesder判断编码   UTF-8
    reg0 = r'''<th class="comparison_image_title_cell" role="columnheader">
                    <div class="a-row a-spacing-top-micro">
                        <center>
                             <img alt=".*?" src="(.*?)" id="comparison_image">
                        </center>'''
    Img = re.findall(reg0, result)
    # 手机的尺寸
    reg = r'''<span class="a-size-base a-color-base">Screen Size</span>
                    </th>
                    

                    <td class="comparison_baseitem_column">
                     
                        
                            
                            
                                 <span class="a-size-base a-color-base">(.*?)</span>
                            
                        
                    </td>'''
    screen_size = re.findall(reg, result)
    reg1 = r'''<span class="a-size-base a-color-base">Item Dimensions</span>
                    </th>
                    

                    <td class="comparison_baseitem_column">
                     
                        
                            
                            
                                 <span class="a-size-base a-color-base">(.*?)</span>'''
    Dimensions = re.findall(reg1, result)
    # 手机价格
    reg2 = r'<span id="priceblock_ourprice" class="a-size-medium a-color-price">(.*?)</span>'
    Price = re.findall(reg2, result)
    # 手机的名称，亚马逊网站商品的名称
    reg3 = r'''<span id="productTitle" class="a-size-large">
                
                    
                    
                

                
                    
                    
                        (.*?)
                    
                

                
                    
                    
                
            </span>'''
    phone_name = re.findall(reg3, result)

    reg4 = r'''<span class="a-size-base a-color-base">Item Weight</span>
                    </th>
                    

                    <td class="comparison_baseitem_column">
                     
                        
                            
                            
                                 <span class="a-size-base a-color-base">(.*?)</span>'''
    Weight = re.findall(reg4, result)

    reg5 = r'''<span class="a-size-base a-color-base">Operating System</span>
                    </th>
                    

                    <td class="comparison_baseitem_column">
                     
                        
                            
                            
                                 <span class="a-size-base a-color-base">(.*?)</span>'''
    System = re.findall(reg5, result)

    print(Img[0], phone_name, url, Price, screen_size, Dimensions, Weight, System)
    return {'IMG': Img[0], 'phone_name': phone_name, 'URL': url, 'Price_' + now_time: Price, 'screen_size': screen_size,
            'Dimensions': Dimensions, 'Weight': Weight, 'System': System}


# 写入表头
def write_csv_headers(path, csv_headers):
    with open(path, 'a', encoding='gb18030', newline='') as f:
        f_csv = csv.DictWriter(f, csv_headers)
        f_csv.writeheader()


# 写入行
def write_csv_rows(path, csv_headers, rows):
    with open(path, 'a', encoding='gb18030', newline='') as f:
        f_csv = csv.DictWriter(f, csv_headers)
        if type(rows) == type({}):
            f_csv.writerow(rows)
        else:
            f_csv.writerows(rows)


# 得到某品牌手机的页数
def get_pages(url):
    # url = 'https://www.amazon.cn/s/ref=sr_pg_1?rh=n%3A2016116051%2Cn%3A%212016117051%2Cn%3A664978051%2Cn%3A665002051%2Cp_89%3ASamsung+%E4%B8%89%E6%98%9F'
    header = randHeader()
    response = requests.get(url, headers=header, timeout=20)
    result = response.text  # hesder判断编码   UTF-8
    # print(result)
    # reg = r'<span class="pagnRA1"> <span id="pagnNextString">(.*?)</span>'
    # page_next = re.findall(reg,result)                          #下一页的标签按钮

    # reg_now_page = r'<span class="pagnCur">(.*?)</span>'        #实际的最后一页
    # last_page = re.findall(reg_now_page,result)

    reg1 = r'<span class="pagnDisabled">(.*?)</span>'  # 显示的最后一页
    pages = re.findall(reg1, result)
    # print(pages)
    return pages


# 主函数
def main(phone_names, phone_url):
    page_num = 1
    csv_filename = 'AMAZON ' + phone_names + '.csv'
    CSV_headers = ['IMG', 'phone_name', 'URL', 'Price_' + now_time, 'screen_size', 'Dimensions', 'Weight', 'System']
    write_csv_headers(csv_filename, CSV_headers)
    if len(get_pages(phone_url)):
        pages = get_pages(phone_url)
        pages = int(pages[0])
        while (page_num <= pages):
            for i in get_phone_url_list(phone_url):
                write_csv_rows(csv_filename, CSV_headers, get_phone_config(i))
                # for j in get_phone_all_url(i):
                # write_csv_rows(csv_filename,CSV_headers,get_phone_config(j))
            page_num = page_num + 1
    else:
        for i in get_phone_url_list(phone_url):
            write_csv_rows(csv_filename, CSV_headers, get_phone_config(i))
            # for j in get_phone_all_url(i):
            # write_csv_rows(csv_filename,CSV_headers,get_phone_config(j))
            time.sleep(1)


'''
for i in get_phone_url_list():
    for j in phone_all_url(i):
        get_phone_config(j)
'''

if __name__ == '__main__':
    # print(start_url[1])
    # main('Huawei',start_url[0])  #Huawei
    main('Samsung', start_url[1])  # Samsung