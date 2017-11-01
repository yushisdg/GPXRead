import xml.sax


class GPXHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.lon = ""
        self.lat = ""
        self.ele = ""
        self.time = ""
        self.speed = ""


    # 元素开始调用
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "trkpt":
            print("*****trkpt*****")
            lon = attributes["lon"]
            lat = attributes["lat"]
            print("lon:lat", lon+lat);

    # 元素结束调用
    def endElement(self, tag):
        if self.CurrentData == "ele":
            print("ele:", self.ele)
        elif self.CurrentData == "time":
            print("time:", self.time)
        elif self.CurrentData == "speed":
            print("speed:", self.speed)
        self.speed = ""

    # 读取字符时调用
    def characters(self, content):
        if self.CurrentData == "ele":
            self.ele = content
        elif self.CurrentData == "time":
            self.time = content
        elif self.CurrentData == "speed":
            self.speed = content


if (__name__ == "__main__"):
    # 创建一个 XMLReader
    parser = xml.sax.make_parser()
    # turn off namepsaces
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    # 重写 ContextHandler
    Handler = GPXHandler()
    parser.setContentHandler(Handler)

    parser.parse("3.gpx")