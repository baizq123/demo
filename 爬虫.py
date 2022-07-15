#!/usr/bin/python3
# --coding:utf-8--
# @Author:baizq

import requests
import re

def fangwen(bod,key,page):
    url = "https://www.ncbi.nlm.nih.gov/protein"
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'max-age=0',
        'content-length': '4582',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'ncbi_sid=3A7F7AFB229C2FB1_0008SID; _ga=GA1.2.746779974.1646904124; _gid=GA1.2.2024456447.1646904124; QSI_SI_0HhBb7Qmlxy2ZIF_intercept=true; WebEnv=12oshPu5yf6a5JTS6ngQsMaEg0d9xkd7499xLNtmj2Rk3%403A7F7AFB229C2FB1_0008SID; ncbi_pinger=N4IgDgTgpgbg+mAFgSwCYgFwgMIFEAcAIgOwCCAQgIwBM1pp1ArFQAxvvuWWFuPUB0AWzjUAzCAA0IAK4A7ADYB7AIapZUAB4AXTKGqYQUWVugAvSSHFZIirVGSyLAFgOpFAYwDO0wRcYGLADZXD29fKWIDRC1BeQt8A2oWCwBOVygAM2VpeR0pLgNKC0orEDFAlgT8lyxPKGUId0Ri4KxleTj8yKws+TrihJ72/qkkgzwiMipaeiZWDg4uHhY+IRFxUaKsIxMoUwwbOwcMNy8fDAA5AHkL3AtaAwB3Z/5ZdwAjZFf5QVfkRH4AHNFDB7mksJQUmMpKJkhDKskYVsQJDoZZ9PCnIjLKVeiNLDUQCZpFALKJBiAyeCQIwUoEnEUpFiDIFiNQGc5Six+KJGPxsU5CXIlKp1NpnP4sNjGKVUdLCbTGTTWiAGWkpIxuiBsYFkRV8P4AL6GoA',
        'origin': 'https://www.ncbi.nlm.nih.gov',
        'referer': 'https://www.ncbi.nlm.nih.gov/protein',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
    }
    data = f"term={bod}&EntrezSystem2.PEntrez.Protein.Sequence_PageController.PreviousPageName=results&EntrezSystem2.PEntrez.Protein.Sequence_Facets.FacetsUrlFrag=filters%3D&EntrezSystem2.PEntrez.Protein.Sequence_Facets.FacetSubmitted=false&EntrezSystem2.PEntrez.Protein.Sequence_Facets.BMFacets=&EntrezSystem2.PEntrez.Protein.Sequence_ResultsPanel.Sequence_DisplayBar.sPresentation=docsum&EntrezSystem2.PEntrez.Protein.Sequence_ResultsPanel.Sequence_DisplayBar.sPageSize=20&EntrezSystem2.PEntrez.Protein.Sequence_ResultsPanel.Sequence_DisplayBar.sSort=none&EntrezSystem2.PEntrez.Protein.Sequence_ResultsPanel.Sequence_DisplayBar.FFormat=docsum&EntrezSystem2.PEntrez.Protein.Sequence_ResultsPanel.Sequence_DisplayBar.FSort=&coll_start=41&EntrezSystem2.PEntrez.Protein.Sequence_ResultsPanel.Sequence_DisplayBar.Db=protein&EntrezSystem2.PEntrez.Protein.Sequence_ResultsPanel.Sequence_DisplayBar.QueryKey=1&EntrezSystem2.PEntrez.Protein.Sequence_ResultsPanel.Sequence_DisplayBar.CurrFilter=all&EntrezSystem2.PEntrez.Protein.Sequence_ResultsPanel.Sequence_DisplayBar.ResultCount=23608&EntrezSystem2.PEntrez.Protein.Sequence_ResultsPanel.Sequence_DisplayBar.ViewerParams=&EntrezSystem2.PEntrez.Protein.Sequence_ResultsPanel.Sequence_DisplayBar.FileFormat=docsum&EntrezSystem2.PEntrez.Protein.Sequence_ResultsPanel.Sequence_DisplayBar.LastPresentation=docsum&EntrezSystem2.PEntrez.Protein.Sequence_ResultsPanel.Sequence_DisplayBar.Presentation=docsum&EntrezSystem2.PEntrez.Protein.Sequence_ResultsPanel.Sequence_DisplayBar.PageSize=20&EntrezSystem2.PEntrez.Protein.Sequence_ResultsPanel.Sequence_DisplayBar.LastPageSize=20&EntrezSystem2.PEntrez.Protein.Sequence_ResultsPanel.Sequence_DisplayBar.Sort=&EntrezSystem2.PEntrez.Protein.Sequence_ResultsPanel.Sequence_DisplayBar.LastSort=&EntrezSystem2.PEntrez.Protein.Sequence_ResultsPanel.Sequence_DisplayBar.FileSort=&EntrezSystem2.PEntrez.Protein.Sequence_ResultsPanel.Sequence_DisplayBar.Format=&EntrezSystem2.PEntrez.Protein.Sequence_ResultsPanel.Sequence_DisplayBar.LastFormat=&EntrezSystem2.PEntrez.Protein.Sequence_ResultsPanel.Sequence_DisplayBar.PrevPageSize=20&EntrezSystem2.PEntrez.Protein.Sequence_ResultsPanel.Sequence_DisplayBar.PrevPresentation=docsum&EntrezSystem2.PEntrez.Protein.Sequence_ResultsPanel.Sequence_DisplayBar.PrevSort=&CollectionStartIndex=1&EntrezSystem2.PEntrez.Protein.Sequence_ResultsPanel.Sequence_ResultsController.ResultCount=23608&EntrezSystem2.PEntrez.Protein.Sequence_ResultsPanel.Sequence_ResultsController.RunLastQuery=&EntrezSystem2.PEntrez.Protein.Sequence_ResultsPanel.Sequence_ResultsController.AccnsFromResult=&EntrezSystem2.PEntrez.Protein.Sequence_ResultsPanel.Entrez_Pager.cPage=3&EntrezSystem2.PEntrez.Protein.Sequence_ResultsPanel.Entrez_Pager.CurrPage={page}&EntrezSystem2.PEntrez.Protein.Sequence_ResultsPanel.Entrez_Pager.cPage=3&EntrezSystem2.PEntrez.Protein.Sequence_ResultsPanel.Sequence_DisplayBar.sPresentation2=docsum&EntrezSystem2.PEntrez.Protein.Sequence_ResultsPanel.Sequence_DisplayBar.sPageSize2=20&EntrezSystem2.PEntrez.Protein.Sequence_ResultsPanel.Sequence_DisplayBar.sSort2=none&EntrezSystem2.PEntrez.Protein.Sequence_ResultsPanel.Sequence_DisplayBar.FFormat2=docsum&EntrezSystem2.PEntrez.Protein.Sequence_ResultsPanel.Sequence_DisplayBar.FSort2=&coll_start2=41&EntrezSystem2.PEntrez.Protein.Sequence_ResultsPanel.Sequence_MultiItemSupl.Taxport.TxView=list&EntrezSystem2.PEntrez.Protein.Sequence_ResultsPanel.Sequence_MultiItemSupl.Taxport.TxListSize=5&EntrezSystem2.PEntrez.Protein.Sequence_ResultsPanel.Sequence_MultiItemSupl.RelatedDataLinks.rdDatabase=rddbto&EntrezSystem2.PEntrez.Protein.Sequence_ResultsPanel.Sequence_MultiItemSupl.RelatedDataLinks.DbName=protein&EntrezSystem2.PEntrez.Protein.Sequence_ResultsPanel.Discovery_SearchDetails.SearchDetailsTerm={bod}%5BAll+Fields%5D&EntrezSystem2.PEntrez.Protein.Sequence_ResultsPanel.HistoryDisplay.Cmd=PageChanged&EntrezSystem2.PEntrez.DbConnector.Db=protein&EntrezSystem2.PEntrez.DbConnector.LastDb=protein&EntrezSystem2.PEntrez.DbConnector.Term={bod}&EntrezSystem2.PEntrez.DbConnector.LastTabCmd=&EntrezSystem2.PEntrez.DbConnector.LastQueryKey={key}&EntrezSystem2.PEntrez.DbConnector.IdsFromResult=&EntrezSystem2.PEntrez.DbConnector.LastIdsFromResult=&EntrezSystem2.PEntrez.DbConnector.LinkName=&EntrezSystem2.PEntrez.DbConnector.LinkReadableName=&EntrezSystem2.PEntrez.DbConnector.LinkSrcDb=&EntrezSystem2.PEntrez.DbConnector.Cmd=PageChanged&EntrezSystem2.PEntrez.DbConnector.TabCmd=&EntrezSystem2.PEntrez.DbConnector.QueryKey=&p%24a=EntrezSystem2.PEntrez.Protein.Sequence_ResultsPanel.Entrez_Pager.Page&p%24l=EntrezSystem2&p%24st=protein"
    res = requests.post(url,data=data,headers=headers)
    return res.text


def guolv(html):
    ids = []
    pat = re.compile(r'<div class="rprtnum nohighlight">(.*?)<div class="rprt">')
    items = pat.findall(html)
    for i in items:
        if "H37Rv" in i:
            id = re.findall('link_uid=(.*?)&', i, re.S)
            ids.append(id[0])
    return ids

def neirong(id):
    url = f"https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?id={id}&db=protein&report=fasta&extrafeat=null&conwithfeat=on&hide-cdd=on&retmode=html&withmarkup=on&tool=portal&log$=seqview&maxdownloadsize=1000000"
    headers = {
          'accept':'*/*',
          'accept-encoding':'gzip, deflate, br',
          'accept-language':'zh-CN,zh;q=0.9',
          'cookie':'ncbi_sid=3A7F7AFB229C2FB1_0008SID; _ga=GA1.2.746779974.1646904124; _gid=GA1.2.2024456447.1646904124; QSI_SI_0HhBb7Qmlxy2ZIF_intercept=true; entrezSort=protein:; WebEnv=1d30w5A1j-QWkBwm5jTJWtPsNhzhX_Pr7Lz5razOx6jAs%403A7F7AFB229C2FB1_0008SID; ncbi_pinger=N4IgDgTgpgbg+mAFgSwCYgFwgMIFEAcAIgEIBM+AjKaQII0BsA7MRQAzsccUCcALO/VwA6ALZxSvEAF8gA==',
          'ncbi-phid':'CE8DB28122AA67B1000000000194006E.m_24.02',
          'referer':'https://www.ncbi.nlm.nih.gov/protein/AAB07804.1?report=fasta',
          'sec-ch-ua':'"Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
          'sec-ch-ua-mobile':'?0',
          'sec-ch-ua-platform':'"Windows"',
          'sec-fetch-dest':'empty',
          'sec-fetch-mode':'cors',
          'sec-fetch-site':'same-origin',
          'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'}
    res = requests.get(url,headers=headers)
    return res.text

def save(key_1,id,nr):
    with open('aaaaa.txt','a',encoding='utf-8') as f:
        f.write(key_1+"    "+"H37Rv"+"    "+id+"    "+nr+"\n")





# 前面的函数都不用动，
#   1. yiliao这个列表中按格式写上你需要的药材名
#   2. 药材名后面对应的数字，等会我教你在哪看
#   3. 想要爬取几页的数据只需要更改数字10，目前的代码是爬取前9页

yiliao = {"MtrA":1,"MtrB":2}
for i,j in yiliao.items():
    for k in range(1,10):
        html = fangwen(i,j,k)
        id = guolv(html)
        if id == []:
            continue
        for kk in id:
            nr = neirong(kk)
            save(i,kk,nr)