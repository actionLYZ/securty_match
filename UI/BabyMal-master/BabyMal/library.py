import autoit
import os
import time
from Keras import *
import Global

APIS = "data/apis.txt"


def get_process_name(filename):
    pos1 = filename.rfind('\\')
    pos2 = filename.rfind('/')
    return filename[max(pos1, pos2) + 1:]


def call_softsnoop(filename):
    autoit.run("softsnoop/SoftSnoop.exe " + filename, "", autoit.properties.SW_HIDE)
    time.sleep(5)
    autoit.process_close(get_process_name(filename))
    time.sleep(1)
    autoit.process_close("SoftSnoop.exe")
    time.sleep(1)
    return


class Analyzer:
    def __init__(self, name):
        super(Analyzer, self).__init__()
        self.name = name
        self.model = MalwareDetectorModel()
        self.model.train()
        return

    def dynamic_analyze(self):
        # call_softsnoop(self.name)
        # autoit.run("Merge.exe", "", autoit.properties.SW_HIDE)
        # os.popen("Merge.exe")
        with open("softsnoop/OutFiles/result.txt") as f:
            vector = list(f.readline())
        for i in range(len(vector)):
            vector[i] = int(vector[i])
        # vector = to_vector("softsnoop/OutFiles/api.txt")
        value, result = self.model.test(vector)
        # os.remove("softsnoop/OutFiles/api.txt")
        #Global.mainWindow.content_widget2.progressBar.setProperty("value", 99)  # 设置进度条
        return value[0][0], result[0][0]

    def static_analyze(self):

        return


def load_apis():
    with open(APIS) as f:
        contents = f.readlines()
        for i in range(len(contents)):
            pos = contents[i].index(' ')
            contents[i] = (contents[i])[:pos]
    return contents


def compare_api(contents, contents_index, line):
    pos = line.index(' ')
    line = line[:pos]
    if line == contents[contents_index]:
        flag = True
    else:
        flag = False
    return flag


def to_vector(path):
    apis = load_apis()
    vector = list(range(len(apis)))
    flag = None
    with open(path, 'r') as f:
        iter_file = f.readlines()
        for contentsIndex in range(len(apis)):
            for line in range(len(iter_file)):
                flag = compare_api(apis, contentsIndex, iter_file[line])
                if flag:
                    vector[contentsIndex] = '1'
                    break
            if not flag:
                vector[contentsIndex] = '0'
    return vector

