from keras.layers.core import Activation, Dense
from keras.models import Sequential, load_model
from keras.optimizers import SGD
from numpy import array
import Global
import os


NORMAL_SOFTWARE_DATA = "data/normal_software/"
MALWARE_DATA = "data/malware/"


def get_inputs():
    files = None
    inputs = []
    for root, dirs, files in os.walk(NORMAL_SOFTWARE_DATA):
        pass
    #Global.mainWindow.content_widget2.progressBar.setProperty("value", 15)  # 设置进度条
    for num,a_file in enumerate(files):
        f = open(NORMAL_SOFTWARE_DATA + a_file)
        a_list = list(f.readline())
        for i in range(len(a_list)):
            a_list[i] = int(a_list[i])
        f.close()
        inputs.append(a_list)
        if num == len(files) // 5:
            Global.mainWindow.content_widget2.progressBar.setProperty("value", 30)  # 设置进度条
        if num == (len(files) // 5) * 2:
            Global.mainWindow.content_widget2.progressBar.setProperty("value", 45)  # 设置进度条
        if num == (len(files) // 5) * 3:
            Global.mainWindow.content_widget2.progressBar.setProperty("value", 60)  # 设置进度条
        if num == (len(files) // 5) * 4:
            Global.mainWindow.content_widget2.progressBar.setProperty("value",75)  # 设置进度条

    for root, dirs, files in os.walk(MALWARE_DATA):
        pass
    for a_file in files:
        f = open(MALWARE_DATA + a_file)
        a_list = list(f.readline())
        for i in range(len(a_list)):
            a_list[i] = int(a_list[i])
        f.close()
        inputs.append(a_list)
    Global.mainWindow.content_widget2.progressBar.setProperty("value", 85)  # 设置进度条
    return array(inputs)


def get_outputs():
    files = None
    outputs = []
    for root, dirs, files in os.walk(NORMAL_SOFTWARE_DATA):
        pass
    for a_file in files:
        outputs.append(0)
    for root, dirs, files in os.walk(MALWARE_DATA):
        pass
    for a_file in files:
        outputs.append(1)
    return array(outputs)


class MalwareDetectorModel:
    def __init__(self):
        super(MalwareDetectorModel, self).__init__()
        Global.mainWindow.content_widget2.progressBar.setProperty("value", 10)  # 设置进度条
        self.x_train = get_inputs()
        self.y_label = get_outputs()
        self.x_test = None
        self.model = None
        return

    def train(self):
        try:
            f = open("model.h5")
            Global.mainWindow.content_widget2.progressBar.setProperty("value", 90)  #设置进度条
        except FileNotFoundError:
            self.model = Sequential()

            self.model.add(Dense(32, init='uniform', input_dim=754))
            self.model.add(Activation('relu'))

            self.model.add(Dense(1))
            self.model.add(Activation('sigmoid'))

            sgd = SGD(lr=0.05, decay=1e-6, momentum=0.9, nesterov=True)

            self.model.compile(loss='binary_crossentropy', optimizer=sgd, metrics=["accuracy"])

            self.model.fit(self.x_train, self.y_label, batch_size=1, nb_epoch=20)
            self.model.save("model.h5")
            return
        self.model = load_model("model.h5")
        return

    def test(self, vector):
        a_list = vector
        for i in range(len(vector)):
            a_list[i] = int(vector[i])
        return self.model.predict(array([a_list])), self.model.predict_classes(array([a_list]))
