import time
import sys
import requests
from lxml import etree


def fanyi(q):
    
    url='http://m.youdao.com/dict?le=eng&q='+q
    res=requests.get(url)
    res=res.text
#print(res)
    res=etree.HTML(res)
    tran1=res.xpath('//ul/li/text()')
    trans=res.xpath('//p/text()')
    if trans[0]=='您是不是要找：':
        
        tran= trans[2]
    else:
        
        tran=trans[1]
    tran3=res.xpath('//a[@class="clickable"]/text()')
    del tran1[0]
    del tran1[0]
    del tran1[0]
    del tran1[0]


    trant0=''
    if len(tran)>=1:
        
        trant0=tran[-1]
        if len(trant0)==1:
            
            trant0=''

    trant=''
    if len(tran1)>=1:
        
        trant=tran1[-1]
    trant1=''
    if len(tran3)>=1:
        trant1=tran3[-1]
    return trant0+trant+trant1


