from xml.dom.minidom import parse
import xml.dom.minidom
import psycopg2
import uuid
import os





def readGpxDate(fileName):
    # 使用minidom解析器打开 XML 文档
    DOMTree = xml.dom.minidom.parse(fileName)
    collection = DOMTree.documentElement
    # 在集合中获取所有点
    trkpts = collection.getElementsByTagName("trkpt")
    # 打印每个点的详细信息
    track_fid=str(uuid.uuid1()).replace('-','');  #随机生成一个唯一的Id
    print(track_fid);
    totalSql="";
    for trkpt in trkpts:
       print ("*****trkpt*****")
       lon="";
       lat="";
       if trkpt.hasAttribute("lon"):
          print ("lon: %s" % trkpt.getAttribute("lon"));
          lon=trkpt.getAttribute("lon");
       if trkpt.hasAttribute("lon"):
           print("lat: %s" % trkpt.getAttribute("lat"))
           lat=trkpt.getAttribute("lat");
       ele = trkpt.getElementsByTagName('ele')[0].childNodes[0].data;
       print ("Type: %s" % ele)
       time = trkpt.getElementsByTagName('time')[0].childNodes[0].data;
       print ("time: %s" % time);
       speed = trkpt.getElementsByTagName('speed')[0].childNodes[0].data;
       print ("speed: %s" % speed);
       sql="INSERT INTO track_points_python ( track_fid, ele, time, speed, lon, lat) VALUES ('"+track_fid+"',"+ele+",'"+time+"',"+speed+",'"+lon+"','"+lat+"');"
       print(sql);
       totalSql=totalSql+sql;
    conn = psycopg2.connect(database="superpower", user="postgres", password="123456", host="localhost", port="5432");
    cur = conn.cursor();
    try:
        cur.execute(totalSql);
    except Exception as e:
        print(e);
    conn.commit();
    cur.close();
    conn.close();


def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        print(root) #当前目录路径
        print(dirs) #当前路径下所有子目录
        print(files) #当前路径下所有非目录子文件
        for fileName in files:
            filePath=root+"//"+fileName;
            print(filePath);
            readGpxDate(filePath);

file_name("F://track")
#readGpxDate("3.gpx");