# coding=utf-8
import BeautifulSoup as bs
import requests as req
import re
import db


def processpage(url):
    content = req.request("get", url)
    soup = bs.BeautifulSoup(content.content)
    poems = soup.findAll(attrs={'class': 'sons'})
    for poem in poems:
        als = poem.findAll("a")
        link = ""
        for a in als:
            if a.get("href").startswith("/view"):
                link = a.get("href")
        try:
            processpoem("http://so.gushiwen.org"+link)
        except Exception as e:
            print e.message
            print "error:"+link
            db.error(link)



def processpoem(url):
    content = req.request("get", url)
    soup = bs.BeautifulSoup(content.content)
    title = soup.find(attrs={'class': 'shileft'}).find(attrs={'class': 'son1'}).find("h1").text
    content = soup.find(attrs={'class': 'shileft'}).find(attrs={'class': 'son2'}).findAll("p")
    dy = content[0].text.split(u"：")[1]
    writer = content[1].text.split(u"：")[1]
    inner = removeHtml(str(soup.find(attrs={'class': 'shileft'}).find(attrs={'class': 'son2'})).split(r'<p style="margin:0px; font-size:12px;line-height:160%;"><span>原文：</span></p>')[-1])
    fanyiid = soup.findAll(attrs={'class': 'son5'})[0].get("id").replace("fanyiShort", "")
    exp = req.request("get", "http://so.gushiwen.org/shiwen/ajaxfanyi.aspx?id="+fanyiid).content
    exp = removeHtml(exp)
    kid = soup.findAll(attrs={'class': 'son5'})[1].get("id")
    url = "";
    if("fanyiShort" in kid):
        kid = kid.replace("fanyiShort", "")
        url = "fanyi"
    if ("shangxiShort1" in kid):
        kid = kid.replace("shangxiShort1", "")
        url = "shangxi"
    knowledge = req.request("get", "http://so.gushiwen.org/shiwen/ajax"+url+".aspx?id=" + kid).content
    knowledge = removeHtml(knowledge)
    db.insert(title, writer, inner, exp, knowledge)
    print


def removeHtml(html):
    dr = re.compile(r'<[^>]+>', re.S)
    dd = dr.sub('', html)
    return dd