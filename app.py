# import modules
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget, QLabel, QPushButton,QVBoxLayout,QHBoxLayout
from random import choice
# Main App object and settings
app=QApplication([])
main_windo=QWidget()
main_windo.setWindowTitle("Random Word Maker")
main_windo.resize(300,200)

# Create all app objects
title=QLabel("Random Keyword")

text1=QLabel("?")
text2=QLabel("?")
text3=QLabel("?")


button1=QPushButton("click me")
button2=QPushButton("click me")
button3=QPushButton("click me")

my_words=['hello','good','bye','test','python','happy','sad']

# All Design Here

master_layout=QVBoxLayout()

row1=QHBoxLayout()
row2=QHBoxLayout()
row3=QHBoxLayout()

row1.addWidget(title, alignment=Qt.AlignCenter)

row2.addWidget(text1, alignment=Qt.AlignCenter)

row2.addWidget(text2, alignment=Qt.AlignCenter)

row2.addWidget(text3, alignment=Qt.AlignCenter)


row3.addWidget(button1)
row3.addWidget(button2)
row3.addWidget(button3)


master_layout.addLayout(row1)
master_layout.addLayout(row2)
master_layout.addLayout(row3)

main_windo.setLayout(master_layout)
# Add functions // creation function

def random_word1():
    word=choice(my_words)
    text1.setText(word)

def random_word2():
    word=choice(my_words)
    text2.setText(word)

def random_word3():
    word=choice(my_words)
    text3.setText(word)
# Events
button1.clicked.connect(random_word1)
button2.clicked.connect(random_word2)
button3.clicked.connect(random_word3)


# Show\Run owr app

main_windo.show()
app.exec_()