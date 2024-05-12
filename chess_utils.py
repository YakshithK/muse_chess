import time # for time
import pyautogui # to make the clicks
import sys # for the windows
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget # for the windows
from PyQt5.QtGui import QFont # for the windows
import subprocess # for the switchcontrol.py 

app = QApplication(sys.argv)

'''1: Making functions and classes for the input windows'''

#1.1: function to pick what piece to move
def pickPiece(positions):

    closeCmd()

    process = subprocess.Popen("start cmd /k python switchcontrol.py", shell=True)
    process.wait()
    time.sleep(1.5)
    
    class PiecePickerWindow(QMainWindow):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("Piece Picker")
            self.central_widget = QWidget()
            self.setCentralWidget(self.central_widget)
            layout = QVBoxLayout(self.central_widget)
            
            for piece in positions.keys():
                button = QPushButton(piece)             
                font = QFont()
                font.setPointSize(40)
                button.setFont(font)
                button.setFixedSize(650, 110)
                button.clicked.connect(lambda checked, name=piece: self.handle_button_click(name))
                layout.addWidget(button)
        
            self.setGeometry(4821, 332, 675, 900)
        
        def handle_button_click(self, character):
            global pieceInput
            pieceInput += character
            self.close()
            
        def keyPressEvent(self, event):
            global pieceInput
            if event.key() == 16777220:
                pieceInput += self.focusWidget().text()
                self.close()

    piece_picker_window = PiecePickerWindow()
    piece_picker_window.show()
    app.exec_()

    return pieceInput

#1.2: function to pick what file to move to
def filePick(fileNames):

    closeCmd()

    process = subprocess.Popen("start cmd /k python switchcontrol.py", shell=True)
    process.wait()
    time.sleep(1.5)

    class FilePickerWindow(QMainWindow):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("File Picker")
            self.central_widget = QWidget()
            self.setCentralWidget(self.central_widget)
            layout = QVBoxLayout(self.central_widget)
            
            for file_name in fileNames:
                button = QPushButton(file_name)
                font = QFont()
                font.setPointSize(40)
                button.setFont(font)
                button.setFixedSize(650, 110)
                button.clicked.connect(lambda checked, name=file_name: self.handle_button_click(name))
                layout.addWidget(button)
        
            self.setGeometry(4821, 332, 675, 900)

        def handle_button_click(self, character):
            global fileInput
            fileInput += character
            self.close()

        def keyPressEvent(self, event):
            global fileInput
            if event.key() == 16777220:
                fileInput += self.focusWidget().text()
                self.close()

    piece_picker_window = FilePickerWindow()
    piece_picker_window.show()
    app.exec_()

    return fileInput

#1.2.5: function to pick what rank to move to
def pickRank(rankNames):

    closeCmd()

    process = subprocess.Popen("start cmd /k python switchcontrol.py", shell=True)
    process.wait()
    time.sleep(1.5)
    
    class RankPickerWindow(QMainWindow):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("Rank Picker")
            self.central_widget = QWidget()
            self.setCentralWidget(self.central_widget)
            layout = QVBoxLayout(self.central_widget)
            
            for rank_name in rankNames:
                button = QPushButton(rank_name)
                font = QFont()
                font.setPointSize(40)
                button.setFont(font)
                button.setFixedSize(650, 110)
                button.clicked.connect(lambda checked, name=rank_name: self.handle_button_click(name))
                layout.addWidget(button)
        
            self.setGeometry(4821, 332, 675, 900)

        def handle_button_click(self, character):
            global rankInput
            rankInput += character
            self.close()

        def keyPressEvent(self, event):
            global rankInput
            if event.key() == 16777220: 
                rankInput += self.focusWidget().text()
                self.close()
    piece_picker_window = RankPickerWindow()
    piece_picker_window.show()
    app.exec_()

    return rankInput

#1.3: function to choose if you want to take with your pawn or move
def take():

    closeCmd()

    process = subprocess.Popen("start cmd /k python switchcontrol.py", shell=True)
    process.wait()
    time.sleep(1.5)

    class Taker(QMainWindow):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("Take or Move")
            self.central_widget = QWidget()
            self.setCentralWidget(self.central_widget)
            layout = QVBoxLayout(self.central_widget)
            
            x = ['take', 'move']

            for i in x:
                button = QPushButton(i)
                font = QFont()
                font.setPointSize(40)
                button.setFont(font)
                button.setFixedSize(650, 440)
                button.clicked.connect(lambda checked, name=i: self.handle_button_click(name))
                layout.addWidget(button)
        
            self.setGeometry(4821, 332, 675, 900)

        def handle_button_click(self, character):
            global takeInput
            takeInput += character
            self.close()

        def keyPressEvent(self, event):
            global takeInput
            if event.key() == 16777220: 
                takeInput += self.focusWidget().text()
                self.close()

    piece_picker_window = Taker()
    piece_picker_window.show()
    app.exec_()

    return takeInput

#1.4: window to promote pawn
def Promote():

    closeCmd()

    process = subprocess.Popen("start cmd /k python switchcontrol.py", shell=True)
    process.wait()
    time.sleep(1.5)

    class Promote(QMainWindow):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("Promote to what?")
            self.central_widget = QWidget()
            self.setCentralWidget(self.central_widget)
            layout = QVBoxLayout(self.central_widget)
            
            x = ['queen', 'knight', 'rook', 'bishop']

            for i in x:
                button = QPushButton(i)
                font = QFont()
                font.setPointSize(40)
                button.setFont(font)
                button.setFixedSize(650, 220)
                button.clicked.connect(lambda checked, name=i: self.handle_button_click(name))
                layout.addWidget(button)
        
            self.setGeometry(4821, 332, 675, 900)

        def handle_button_click(self, character):
            global promoInput
            promoInput += character
            self.close()

        def keyPressEvent(self, event):
            global promoInput
            if event.key() == 16777220: 
                promoInput += self.focusWidget().text()
                self.close()

    piece_picker_window = Promote()
    piece_picker_window.show()
    app.exec_()

    return promoInput

#1.5: window to input which colour you're playing as
def colour():

    process = subprocess.Popen("start cmd /k python switchcontrol.py", shell=True)
    process.wait()
    time.sleep(1.5)

    class Colour(QMainWindow):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("Which Color are you?")
            self.central_widget = QWidget()
            self.setCentralWidget(self.central_widget)
            layout = QVBoxLayout(self.central_widget)
            
            x = ['white', 'black']

            for i in x:
                button = QPushButton(i)
                font = QFont()
                font.setPointSize(40)
                button.setFont(font)
                button.setFixedSize(650, 440)
                button.clicked.connect(lambda checked, name=i: self.handle_button_click(name))
                layout.addWidget(button)
        
            self.setGeometry(4821, 332, 675, 900)

        def handle_button_click(self, character):
            global colInput
            colInput += character
            self.close()

        def keyPressEvent(self, event):
            global colInput
            if event.key() == 16777220: 
                colInput += self.focusWidget().text()
                self.close()

    piece_picker_window = Colour()
    piece_picker_window.show()
    app.exec_()

    return colInput

#1.6: function to input the specific piece to move (only if there are two of the piece eg. pawns and knights)
def getSpecificPiece(pieces):
        
    buttonHeight = round(880/len(pieces))
    
    closeCmd()

    process = subprocess.Popen("start cmd /k python switchcontrol.py", shell=True)
    process.wait()
    time.sleep(1.5)

    class SpecificPiece(QMainWindow):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("Which one?")
            self.central_widget = QWidget()
            self.setCentralWidget(self.central_widget)
            layout = QVBoxLayout(self.central_widget)

            for i in pieces:
                button = QPushButton(i)
                font = QFont()
                font.setPointSize(50)
                button.setFont(font)
                button.setFixedSize(650, buttonHeight)
                button.clicked.connect(lambda checked, name=i: self.handle_button_click(name))
                layout.addWidget(button)
        
            self.setGeometry(4821, 332, 675, 900)

        def handle_button_click(self, character):
            global specificInput
            specificInput += character
            self.close()

        def keyPressEvent(self, event):
            global specificInput
            if event.key() == 16777220: 
                specificInput += self.focusWidget().text()
                self.close()

    piece_picker_window = SpecificPiece()
    piece_picker_window.show()
    app.exec_()

    return specificInput

#1.7: function to take a specific piece for pawns
def takeSpecificPiece(coords, tiles, positions):

    takeTiles = []
    for i in coords:
        for k, v in tiles.items():
            if v == i:
                if all(k not in positions for positions in positions.values()):
                    takeTiles.append(k)

    buttonHeight = round(880/len(takeTiles))

    class takeSpecificPiece(QMainWindow):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("Take which one?")
            self.central_widget = QWidget()
            self.setCentralWidget(self.central_widget)
            layout = QVBoxLayout(self.central_widget)

            for i in takeTiles:
                button = QPushButton(i)
                font = QFont()
                font.setPointSize(40)
                button.setFont(font)
                button.setFixedSize(650, buttonHeight)
                button.clicked.connect(lambda checked, name=i: self.handle_button_click(name))
                layout.addWidget(button)
        
            self.setGeometry(4821, 332, 675, 900)

        def handle_button_click(self, character):
            global specificTakeInput
            specificTakeInput += character
            self.close()

        def keyPressEvent(self, event):
            global specificTakeInput
            if event.key() == 16777220: 
                specificTakeInput += self.focusWidget().text()
                self.close()

    piece_picker_window = takeSpecificPiece()
    piece_picker_window.show()
    app.exec_()

    return specificTakeInput

#1.8: function to move king or knight
def moveKing_Knight(coords, pieceCoords, tiles, positions):

    for key, value in tiles.items():
        if value == pieceCoords:
            ogPiece = key

    takeTiles = []
    valList = []
    for i in coords:
        for key, val in tiles.items():
            if val == i:
                if val not in valList:
                    if all(key not in positions for positions in positions.values()):
                        takeTiles.append(key)
        
    closeCmd()

    process = subprocess.Popen("start cmd /k python switchcontrol.py", shell=True)
    process.wait()
    time.sleep(1.5)
    
    buttonHeight = round(880/len(takeTiles))

    class moveKQ(QMainWindow):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("Move where?")
            self.central_widget = QWidget()
            self.setCentralWidget(self.central_widget)
            layout = QVBoxLayout(self.central_widget)

            for i in takeTiles:
                button = QPushButton(i)
                font = QFont()
                font.setPointSize(40)
                button.setFont(font)
                button.setFixedSize(650, buttonHeight)
                button.clicked.connect(lambda checked, name=i: self.handle_button_click(name))
                layout.addWidget(button)
        
            self.setGeometry(4821, 332, 675, 900)

        def handle_button_click(self, character):
            global KQInput
            KQInput += character
            self.close()

        def keyPressEvent(self, event):
            global KQInput
            if event.key() == 16777220: 
                KQInput += self.focusWidget().text()
                self.close()

    piece_picker_window = moveKQ()
    piece_picker_window.show()
    app.exec_()
    return KQInput

#1.9: function to move your pawn
def pawnMove(coords, tiles, positions):

    takeTiles = []
    valList = []
    for i in coords:
        for key, val in tiles.items():
            if val == i:
                if val not in valList:
                    if all(key not in positions for positions in positions.values()):
                        takeTiles.append(key)

    buttonHeight = round(880/len(takeTiles))

    closeCmd()

    process = subprocess.Popen("start cmd /k python switchcontrol.py", shell=True)
    process.wait()
    time.sleep(1.5)

    class movePawn(QMainWindow):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("Move where?")
            self.central_widget = QWidget()
            self.setCentralWidget(self.central_widget)
            layout = QVBoxLayout(self.central_widget)

            for i in takeTiles:
                button = QPushButton(i)
                font = QFont()
                font.setPointSize(40)
                button.setFont(font)
                button.setFixedSize(650, buttonHeight)
                button.clicked.connect(lambda checked, name=i: self.handle_button_click(name))
                layout.addWidget(button)
        
            self.setGeometry(4821, 332, 675, 900)

        def handle_button_click(self, character):
            global pawnInput
            pawnInput += character
            self.close()

        def keyPressEvent(self, event):
            global pawnInput
            if event.key() == 16777220: 
                pawnInput += self.focusWidget().text()
                self.close()

    piece_picker_window = movePawn()
    piece_picker_window.show()
    app.exec_()

    return pawnInput

'''2: A few functions and variables for utility'''

#2.1: function to close a window using pyautogui
def closeCmd():
    pyautogui.click(x=653, y=361)
    pyautogui.hotkey('alt', 'f4')

#2.2: function to click on a piece using pyautogui
def clickPiece(clickCoords):
    pyautogui.click(x=clickCoords[0], y=clickCoords[1])
