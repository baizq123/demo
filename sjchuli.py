import json

import pandas as pd
import folium
import os

def yuan():
    da = pd.read_excel(r"D:\project\jw.xls")
    p_name = list(da["收费广场名称"])
    lng = list(da["经度"])              #经度
    lat = list(da["纬度"])              #纬度
    id = list(da["收费广场编号"])         #编号
    neir = list(zip(p_name,lat,lng))  # 内容列表[名称，维度，经度]
    dic = dict(zip(id,neir))
    return dic
#
#
def wai():
    da = pd.read_excel(r"D:\project\wai.xls")
    p_name = list(da["城市"])
    lng = list(da["经度"])              #经度
    lat = list(da["维度"])              #纬度
    neir = list(zip(lat,lng))
    dic = dict(zip(p_name,neir))
    return dic

# os.chdir('./数据可视化/数据可视化/采集结果2.1')
# dirs = os.listdir(".")
#
# shuju = []
# for i in dirs:
#     data = pd.read_csv(i)
#     data = data.dropna()
#     pm_jin = list(data["ENTOLL_LANE_ID"])
#     pm_chu = list(data["EXTOLL_LANE_ID"])
#     pm_city = list(data["TRANS_REMARKS"])
#     pm_num = list(data["NUMS"]>0)
#     new_nei = list(zip(pm_num,pm_jin,pm_chu,pm_city))
#     shuju.append(new_nei)

# id = list(yuan().keys())
# numbs = []
# for i in id:
#     aa = 0
#     for j in shuju:
#         for k in j:
#             if k[1][:-3]==i or k[2][:-3]==i:
#                 aa += k[0]
#     numbs.append([i,aa])
#
# idd = list(wai().keys())
# bb = 0
# for i in idd:
#     aa = 0
#     for j in shuju:
#         for k in j:
#             if k[1][:-3]==i:
#                 continue
#             elif i in k[3]:
#                 aa += k[0]
#             else:
#                 bb += k[0]
#     numbs.append([i, aa])
def oooo(file):
    with open(rf"D:\project\{file}","r",encoding='utf-8') as f:
        aaa = f.readlines()
        return aaa

def listttt(aaa):
    num1 = []
    for i in aaa:
        kk = i.split(',')
        if int(kk[1])==0:
            continue
        num1.append(int(kk[1]))
    return num1


def maxx(num,listt):
    listt.sort()
    # ping = m2//10  # 100//10= 10
    ping = len(listt)//10
    if num in listt[0:ping]:  # 0-10
        return 300
    elif num in listt[ping:ping*2]: # 10-20
        return 400
    elif num in listt[ping*2:ping*3]:
        return 500
    elif num in listt[ping*3:ping*4]:
        return 600
    elif num in listt[ping*4:ping*5]:
        return 700
    elif num in listt[ping*5:ping*6]:
        return 800
    elif num in listt[ping*6:ping*7]:
        return 900
    elif num in listt[ping*7:ping*8]:
        return 1000
    elif num in listt[ping*8:ping*9]:
        return 1100
    else:
        return 1200

with open('city.json','r') as ff:
    bb = json.load(ff)


def tuu(a,b,c):
    for i in a:
        kk = i.split(',')
        if int(kk[1].replace('\n',''))==0:
            continue
        for j in bb.keys():
            if kk[0] == j:
                folium.Circle(location=bb[j],
                                  popup=kk[0],
                                  radius=maxx(int(kk[1].replace('\n','')),b),
                                  color="#FF0000",
                                  tooltip=kk[0]+str(int(kk[1].replace('\n',''))),
                                  fill=True,fill_color="#FF0000",fill_opacity=1.2).add_child(c)
                    # break
                # print(int(kk[1].replace('\n','')))
            elif kk[0] in j:
                folium.Circle(location=bb[j][1:],
                              popup=bb[j][0],
                              radius=maxx(int(kk[1].replace('\n','')),b),
                              color="#FF0000",
                              tooltip=bb[j][0]+str(int(kk[1].replace('\n',''))),
                              fill=True,fill_color="#FF0000",fill_opacity=1.2
                              ).add_child(c)
                break

def gui():
    m1 = folium.FeatureGroup(name="工作日合计", control=True)
    m2 = folium.FeatureGroup(name="工作日货车", control=True)
    m3 = folium.FeatureGroup(name="工作日客车", control=True)
    m4 = folium.FeatureGroup(name="工作日专车", control=True)
    # m5 = folium.FeatureGroup(name="货一", control=True)
    # m6 = folium.FeatureGroup(name="货二", control=True)
    # m7 = folium.FeatureGroup(name="货三", control=True)
    # m8 = folium.FeatureGroup(name="货四", control=True)
    # m9 = folium.FeatureGroup(name="货五", control=True)
    # m10 = folium.FeatureGroup(name="货六", control=True)
    # m11 = folium.FeatureGroup(name="专车", control=True)
    mmm = folium.Map(location=[39.9,116.3],zoom_start=10,
                    tiles=None,
                    attr='高德地图')
    a = oooo("zhou_zong_hou.txt")
    b = listttt(a)
    for i in a:
        kk = i.split(',')
        if int(kk[1].replace('\n', '')) == 0:
            continue
        for j in bb.keys():
            if kk[0] == j:
                folium.Circle(location=bb[j],
                              popup=kk[0],
                              radius=maxx(int(kk[1].replace('\n', '')), b),
                              color="#B8860B",
                              tooltip=kk[0] + str(int(kk[1].replace('\n', ''))),
                              fill=True, fill_color="#B8860B", fill_opacity=1.2).add_to(m1)
                # print(int(kk[1].replace('\n','')))
            elif kk[0] in j:
                folium.Circle(location=bb[j][1:],
                              popup=bb[j][0],
                              radius=maxx(int(kk[1].replace('\n', '')), b),
                              color="#B8860B",
                              tooltip=bb[j][0] + str(int(kk[1].replace('\n', ''))),
                              fill=True, fill_color="#B8860B", fill_opacity=1.2
                              ).add_to(m1)
                break
    a = oooo("zhou_huo_hou.txt")
    b = listttt(a)
    for i in a:
        kk = i.split(',')
        if int(kk[1].replace('\n', '')) == 0:
            continue
        for j in bb.keys():
            if kk[0] == j:
                folium.Circle(location=bb[j],
                              popup=kk[0],
                              radius=maxx(int(kk[1].replace('\n', '')), b),
                              color="#B8860B",
                              tooltip=kk[0] + str(int(kk[1].replace('\n', ''))),
                              fill=True, fill_color="#B8860B", fill_opacity=1.2).add_to(m2)
                # break
                # print(int(kk[1].replace('\n','')))
            elif kk[0] in j:
                folium.Circle(location=bb[j][1:],
                              popup=bb[j][0],
                              radius=maxx(int(kk[1].replace('\n', '')), b),
                              color="#B8860B",
                              tooltip=bb[j][0] + str(int(kk[1].replace('\n', ''))),
                              fill=True, fill_color="#B8860B", fill_opacity=1.2
                              ).add_to(m2)
                break
    a = oooo("zhou_ke_hou.txt")
    b = listttt(a)
    for i in a:
        kk = i.split(',')
        if int(kk[1].replace('\n', '')) == 0:
            continue
        for j in bb.keys():
            if kk[0] == j:
                folium.Circle(location=bb[j],
                              popup=kk[0],
                              radius=maxx(int(kk[1].replace('\n', '')), b),
                              color="#B8860B",
                              tooltip=kk[0] + str(int(kk[1].replace('\n', ''))),
                              fill=True, fill_color="#B8860B", fill_opacity=1.2).add_to(m3)
                # break
                # print(int(kk[1].replace('\n','')))
            elif kk[0] in j:
                folium.Circle(location=bb[j][1:],
                              popup=bb[j][0],
                              radius=maxx(int(kk[1].replace('\n', '')), b),
                              color="#B8860B",
                              tooltip=bb[j][0] + str(int(kk[1].replace('\n', ''))),
                              fill=True, fill_color="#B8860B", fill_opacity=1.2
                              ).add_to(m3)
                break
    a = oooo("zhou_zhuan_hou.txt")
    b = listttt(a)
    for i in a:
        kk = i.split(',')
        if int(kk[1].replace('\n', '')) == 0:
            continue
        for j in bb.keys():
            if kk[0] == j:
                folium.Circle(location=bb[j],
                              popup=kk[0],
                              radius=maxx(int(kk[1].replace('\n', '')), b),
                              color="#B8860B",
                              tooltip=kk[0] + str(int(kk[1].replace('\n', ''))),
                              fill=True, fill_color="#B8860B", fill_opacity=1.2).add_to(m4)
                # break
                # print(int(kk[1].replace('\n','')))
            elif kk[0] in j:
                folium.Circle(location=bb[j][1:],
                              popup=bb[j][0],
                              radius=maxx(int(kk[1].replace('\n', '')), b),
                              color="#B8860B",
                              tooltip=bb[j][0] + str(int(kk[1].replace('\n', ''))),
                              fill=True, fill_color="#B8860B", fill_opacity=1.2
                              ).add_to(m4)
                break
    # a = oooo("ke2_hou.txt")
    # b = listttt(a)
    # for i in a:
    #     kk = i.split(',')
    #     if int(kk[1].replace('\n', '')) == 0:
    #         continue
    #     for j in bb.keys():
    #         if kk[0] == j:
    #             folium.Circle(location=bb[j],
    #                           popup=kk[0],
    #                           radius=maxx(int(kk[1].replace('\n', '')), b),
    #                           color="#FF0000",
    #                           tooltip=kk[0] + str(int(kk[1].replace('\n', ''))),
    #                           fill=True, fill_color="#FF0000", fill_opacity=1.2).add_to(m2)
    #             # break
    #             # print(int(kk[1].replace('\n','')))
    #         elif kk[0] in j:
    #             folium.Circle(location=bb[j][1:],
    #                           popup=bb[j][0],
    #                           radius=maxx(int(kk[1].replace('\n', '')), b),
    #                           color="#FF0000",
    #                           tooltip=bb[j][0] + str(int(kk[1].replace('\n', ''))),
    #                           fill=True, fill_color="#FF0000", fill_opacity=1.2
    #                           ).add_to(m2)
    #             break
    # a = oooo("ke3_hou.txt")
    # b = listttt(a)
    # for i in a:
    #     kk = i.split(',')
    #     if int(kk[1].replace('\n', '')) == 0:
    #         continue
    #     for j in bb.keys():
    #         if kk[0] == j:
    #             folium.Circle(location=bb[j],
    #                           popup=kk[0],
    #                           radius=maxx(int(kk[1].replace('\n', '')), b),
    #                           color="#FF0000",
    #                           tooltip=kk[0] + str(int(kk[1].replace('\n', ''))),
    #                           fill=True, fill_color="#FF0000", fill_opacity=1.2).add_to(m3)
    #             # break
    #             # print(int(kk[1].replace('\n','')))
    #         elif kk[0] in j:
    #             folium.Circle(location=bb[j][1:],
    #                           popup=bb[j][0],
    #                           radius=maxx(int(kk[1].replace('\n', '')), b),
    #                           color="#FF0000",
    #                           tooltip=bb[j][0] + str(int(kk[1].replace('\n', ''))),
    #                           fill=True, fill_color="#FF0000", fill_opacity=1.2
    #                           ).add_to(m3)
    #             break
    # a = oooo("huo1_hou.txt")
    # b = listttt(a)
    # for i in a:
    #     kk = i.split(',')
    #     if int(kk[1].replace('\n', '')) == 0:
    #         continue
    #     for j in bb.keys():
    #         if kk[0] == j:
    #             folium.Circle(location=bb[j],
    #                           popup=kk[0],
    #                           radius=maxx(int(kk[1].replace('\n', '')), b),
    #                           color="#FF0000",
    #                           tooltip=kk[0] + str(int(kk[1].replace('\n', ''))),
    #                           fill=True, fill_color="#FF0000", fill_opacity=1.2).add_to(m5)
    #             # break
    #             # print(int(kk[1].replace('\n','')))
    #         elif kk[0] in j:
    #             folium.Circle(location=bb[j][1:],
    #                           popup=bb[j][0],
    #                           radius=maxx(int(kk[1].replace('\n', '')), b),
    #                           color="#FF0000",
    #                           tooltip=bb[j][0] + str(int(kk[1].replace('\n', ''))),
    #                           fill=True, fill_color="#FF0000", fill_opacity=1.2
    #                           ).add_to(m5)
    #             break
    # a = oooo("huo2_hou.txt")
    # b = listttt(a)
    # for i in a:
    #     kk = i.split(',')
    #     if int(kk[1].replace('\n', '')) == 0:
    #         continue
    #     for j in bb.keys():
    #         if kk[0] == j:
    #             folium.Circle(location=bb[j],
    #                           popup=kk[0],
    #                           radius=maxx(int(kk[1].replace('\n', '')), b),
    #                           color="#FF0000",
    #                           tooltip=kk[0] + str(int(kk[1].replace('\n', ''))),
    #                           fill=True, fill_color="#FF0000", fill_opacity=1.2).add_to(m6)
    #             # break
    #             # print(int(kk[1].replace('\n','')))
    #         elif kk[0] in j:
    #             folium.Circle(location=bb[j][1:],
    #                           popup=bb[j][0],
    #                           radius=maxx(int(kk[1].replace('\n', '')), b),
    #                           color="#FF0000",
    #                           tooltip=bb[j][0] + str(int(kk[1].replace('\n', ''))),
    #                           fill=True, fill_color="#FF0000", fill_opacity=1.2
    #                           ).add_to(m6)
    #             break
    # a = oooo("huo4_hou.txt")
    # b = listttt(a)
    # for i in a:
    #     kk = i.split(',')
    #     if int(kk[1].replace('\n', '')) == 0:
    #         continue
    #     for j in bb.keys():
    #         if kk[0] == j:
    #             folium.Circle(location=bb[j],
    #                           popup=kk[0],
    #                           radius=maxx(int(kk[1].replace('\n', '')), b),
    #                           color="#FF0000",
    #                           tooltip=kk[0] + str(int(kk[1].replace('\n', ''))),
    #                           fill=True, fill_color="#FF0000", fill_opacity=1.2).add_to(m8)
    #             # break
    #             # print(int(kk[1].replace('\n','')))
    #         elif kk[0] in j:
    #             folium.Circle(location=bb[j][1:],
    #                           popup=bb[j][0],
    #                           radius=maxx(int(kk[1].replace('\n', '')), b),
    #                           color="#FF0000",
    #                           tooltip=bb[j][0] + str(int(kk[1].replace('\n', ''))),
    #                           fill=True, fill_color="#FF0000", fill_opacity=1.2
    #                           ).add_to(m8)
    #             break
    # a = oooo("huo5_hou.txt")
    # b = listttt(a)
    # for i in a:
    #     kk = i.split(',')
    #     if int(kk[1].replace('\n', '')) == 0:
    #         continue
    #     for j in bb.keys():
    #         if kk[0] == j:
    #             folium.Circle(location=bb[j],
    #                           popup=kk[0],
    #                           radius=maxx(int(kk[1].replace('\n', '')), b),
    #                           color="#FF0000",
    #                           tooltip=kk[0] + str(int(kk[1].replace('\n', ''))),
    #                           fill=True, fill_color="#FF0000", fill_opacity=1.2).add_to(m9)
    #             # break
    #             # print(int(kk[1].replace('\n','')))
    #         elif kk[0] in j:
    #             folium.Circle(location=bb[j][1:],
    #                           popup=bb[j][0],
    #                           radius=maxx(int(kk[1].replace('\n', '')), b),
    #                           color="#FF0000",
    #                           tooltip=bb[j][0] + str(int(kk[1].replace('\n', ''))),
    #                           fill=True, fill_color="#FF0000", fill_opacity=1.2
    #                           ).add_to(m9)
    #             break
    # a = oooo("zhuan_hou.txt")
    # b = listttt(a)
    # for i in a:
    #     kk = i.split(',')
    #     if int(kk[1].replace('\n', '')) == 0:
    #         continue
    #     for j in bb.keys():
    #         if kk[0] == j:
    #             folium.Circle(location=bb[j],
    #                           popup=kk[0],
    #                           radius=maxx(int(kk[1].replace('\n', '')), b),
    #                           color="#FF0000",
    #                           tooltip=kk[0] + str(int(kk[1].replace('\n', ''))),
    #                           fill=True, fill_color="#FF0000", fill_opacity=1.2).add_to(m11)
    #             # break
    #             # print(int(kk[1].replace('\n','')))
    #         elif kk[0] in j:
    #             folium.Circle(location=bb[j][1:],
    #                           popup=bb[j][0],
    #                           radius=maxx(int(kk[1].replace('\n', '')), b),
    #                           color="#FF0000",
    #                           tooltip=bb[j][0] + str(int(kk[1].replace('\n', ''))),
    #                           fill=True, fill_color="#FF0000", fill_opacity=1.2
    #                           ).add_to(m11)
    #             break


    folium.TileLayer(tiles="http://map.geoq.cn/ArcGIS/rest/services/ChinaOnlineStreetPurplishBlue/MapServer/tile/{z}/{y}/{x}",attr="default",name="分车型图").add_to(mmm)
    mmm.add_child(m1)
    mmm.add_child(m2)
    mmm.add_child(m3)
    mmm.add_child(m4)
    folium.LayerControl(collapsed=False).add_to(mmm)
    mmm.save(r"D:\project\2021年mtc节假日图.html")

gui()




def gui_dan():
    da = pd.read_excel(r"D:\project\首发能源-油站经纬度.xls")
    p_name = list(da["油站"])
    lng = list(da["高德经度"])  # 经度
    lat = list(da["高德纬度"])  # 纬度
    neir = list(zip(lat, lng))  # 内容列表[名称，维度，经度]
    dic = dict(zip(p_name, neir))
    mmm = folium.Map(location=[39.9,116.3],zoom_start=10,tiles=None,attr="default",name="高德")
    for i,j in dic.items():
        # folium.Circle(location=j,
        #               popup=i,
        #               radius=600,
        #               color="#B8860B",
        #               tooltip=i,
        #               fill=True, fill_color="#B8860B", fill_opacity=1.2).add_to(mmm)
        folium.Marker(location=j,
                      popup=i,
                      # radius=600,
                      # color="#B8860B",
                      tooltip=i,
                      title=i,
                      # fill=True, fill_color="#B8860B", fill_opacity=1.2
                      ).add_to(mmm)
    folium.TileLayer(tiles="http://map.geoq.cn/ArcGIS/rest/services/ChinaOnlineStreetPurplishBlue/MapServer/tile/{z}/{y}/{x}",attr="default",name="油站分布图").add_to(mmm)
    folium.LayerControl(collapsed=False).add_to(mmm)
    mmm.save("油站1.html")
# gui_dan()

# def gui_tu():
#     a = {"客一":"ke1_hou.txt","客二":"ke2_hou.txt","客三":"ke3_hou.txt","客四":"ke4_hou.txt","专车":"zhuan_hou.txt","货一":"huo1_hou.txt","货二":"huo2_hou.txt","货三":"huo3_hou.txt","货四":"huo4_hou.txt","货五":"huo5_hou.txt","货六":"huo6_hou.txt"}
#     for i in list(a.keys()):
#         exec("""i = folium.FeatureGroup(name="i", control=True)""")
#     mmm = folium.Map(location=[39.9,116.3],zoom_start=10,
#                     tiles=None,
#                     attr='高德地图')
#     for i,j in a.items():
#         a = oooo(j)
#         b = listttt(a)
#         exec("""for i in a:
#                     kk = i.split(',')
#                     if int(kk[1]) == 0:
#                         continue
#                     for j in bb.keys():
#                         if kk[0] == j:
#                             folium.Circle(location=bb[j],
#                                           popup=kk[0],
#                                           radius=maxx(int(kk[1]), b),
#                                           color="#FF0000",
#                                           tooltip=kk[0] + str(int(kk[1])),
#                                           fill=True, fill_color="#FF0000", fill_opacity=1.2).add_to(i)
#                             # break
#                             # print(int(kk[1]))
#                         elif kk[0] in j:
#                             folium.Circle(location=bb[j][1:],
#                                           popup=bb[j][0],
#                                           radius=maxx(int(kk[1]), b),
#                                           color="#FF0000",
#                                           tooltip=bb[j][0] + str(int(kk[1])),
#                                           fill=True, fill_color="#FF0000", fill_opacity=1.2
#                                           ).add_to(i)
#                             break""")
#     folium.TileLayer(tiles="https://wprd01.is.autonavi.com/appmaptile?x={x}&y={y}&z={z}&lang=zh_cn&size=1&scl=1&style=8&ltype=11",attr="default",name="高德地图").add_to(mmm)
#     # for i in list(a.keys()):
#     #     exec("mmm.add_child(i)")
#     folium.LayerControl(collapsed=False).add_to(mmm)
#     mmm.save("abc.html")

# gui_tu()