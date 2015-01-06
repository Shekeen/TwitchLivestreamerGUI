# -*- coding: utf-8 -*-

import os
import sys
import livestreamer
from PyQt5 import QtWidgets


class TwitchGUI(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(TwitchGUI, self).__init__(parent)

        self.setWindowTitle('Livestreamer Twitch GUI')

        self.channelName = QtWidgets.QLineEdit()
        self.qualityChooser = QtWidgets.QComboBox()
        self.runButton = QtWidgets.QPushButton('Launch stream!')

        self.runButton.setEnabled(False)

        channelInputLayout = QtWidgets.QHBoxLayout()
        channelInputLayout.addWidget(QtWidgets.QLabel('Twitch channel name:'))
        channelInputLayout.addWidget(self.channelName)

        mainLayout = QtWidgets.QVBoxLayout()
        mainLayout.addLayout(channelInputLayout)
        mainLayout.addWidget(self.qualityChooser)
        mainLayout.addWidget(self.runButton)

        self.channelName.editingFinished.connect(self.getChannelInfo)
        self.runButton.clicked.connect(self.launchLivestreamer)

        self.setLayout(mainLayout)

    def getChannelInfo(self):
        url = 'twitch.tv/%s' % self.channelName.text()
        streams = livestreamer.streams(url)
        self.qualityChooser.addItems(streams.keys())
        self.qualityChooser.setCurrentIndex(0)
        self.runButton.setEnabled(True)

    def launchLivestreamer(self):
        url = 'twitch.tv/%s' % self.channelName.text()
        quality = self.qualityChooser.currentText()
        command = 'livestreamer %s %s' % (url, quality)
        os.system(command)


def main():
    app = QtWidgets.QApplication(sys.argv)
    screen = TwitchGUI()
    screen.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
