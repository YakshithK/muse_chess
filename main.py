import numpy as np  # Module that simplifies computations on matrices
from pylsl import StreamInlet, resolve_byprop  # Module to receive EEG data
import lsl_utils  # Our own utility functions
import time # for time
import pyautogui # to make the clicks
import sys # for the windows
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget # for the windows
from PyQt5.QtGui import QFont # for the windows
import subprocess # for the switchcontrol.py 

'''0: Declaring lists and dicts of chess data'''

#0.1: make lists of files, ranks and their names
fileNames = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
rankNames = ['1', '2', '3', '4', '5', '6', '7', '8']

files = [3300, 3450, 3600, 3750, 3900, 4050, 4200, 4350]
ranks = [1375, 1225, 1075, 925, 775, 625, 475, 325]

Bfiles = files[::-1]
Branks = ranks[::-1]

#0.2: make them into lists of lists for value
tileValues = [[file, rank] for file in files for rank in ranks]
BtileValues = [[file, rank] for file in Bfiles for rank in Branks]

tileNames = [file + rank for file in fileNames for rank in rankNames]

Wtiles = {tileNames[i]: tile for i, tile in enumerate(tileValues)}
Btiles = {tileNames[i]: tile for i, tile in enumerate(BtileValues)}

#0.3: positions for where each piece would lie on           
Wpositions = {'rook':['a1', 'h1'], 'knight':['b1', 'g1'], 'bishop':['c1', 'f1'], 'queen':['d1'], 
                     'king':['e1'], 'pawn':['a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2']}

Bpositions = {'rook':['a8', 'h8'], 'knight':['b8', 'g8'], 'bishop':['c8', 'f8'], 'queen':['d8'], 
                     'king':['e8'], 'pawn':['a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7']}

specificInput = ""

movesList = []

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

'''2: A few functions for utility'''

#2.1: function to close a window using pyautogui
def closeCmd():
    pyautogui.click(x=653, y=361)
    pyautogui.hotkey('alt', 'f4')

#2.2: function to click on a piece using pyautogui
def clickPiece(clickCoords):
    pyautogui.click(x=clickCoords[0], y=clickCoords[1])


'''1: Main function move'''

def move():
    #declare all variables for functions
    global pieceInput, fileInput, rankInput, specificInput, takeInput, specificTakeInput, KQInput, pawnInput, promoInput
    pieceInput = ""
    fileInput = ""
    rankInput = ""
    specificInput = "" 
    takeInput = ""
    specificTakeInput = ""
    KQInput = ""
    pawnInput = ""
    promoInput = ""

    #declare what position dicts to use based on the colour
    if colInput == 'white': 
        tiles = Wtiles
        positions = Wpositions
        promoTile = '8'
        unPromoTile = '7'
    else:
        tiles = Btiles
        positions = Bpositions
        promoTile = '1'
        unPromoTile = '2'

    #pick what piece
    piece = pickPiece(positions)

    #get the tile the piece we inputted is at
    pieceTile = positions.get(piece)

    #if there's only of that piece, select the only one, else make a window for that
    if len(pieceTile) == 1:
        specificPiece = pieceTile[0]
        
    else:
        specificPiece = getSpecificPiece(pieceTile)
    
    #specific coordinates for the screen
    pieceCoords = tiles.get(specificPiece)
    clickPiece(pieceCoords)
    

    #queen, rook and bishops use a file/rank system to move
    if piece == 'queen' or piece == 'rook' or piece == 'bishop':

        #pick what rank to move to 
        fileInput = filePick()

        #pick what file to move to
        rankInput = pickRank()

        move = fileInput + rankInput
        moveCoords = tiles.get(move)
        clickPiece(moveCoords)
    elif piece == 'pawn':
        #working with a pawn
        
        moveCoords = pieceCoords
        z = pieceCoords[1]
        moveCoords[1] = pieceCoords[1] - 150

        #this was the window to pick if you want to take a piece or not
        takeInput = take()
        
        if takeInput == 'take':

            x = pieceCoords[0]
            moveCoords[0] = x - 150     
            z = moveCoords[1]
            y = [x+150, z]

            #movelist has all the possible moves it can do
            moveList = [moveCoords, y]
            move = takeSpecificPiece(moveList, colInput, positions)

        elif takeInput == 'move':

            #when the pawn is on its first turn, it can move twice 
            if z == 1225:
                x = pieceCoords[0]
                y = pieceCoords[1]

                pc = [x, y]
                pc1 = [x, y-150]

                moveList = [pc, pc1]
                move = pawnMove(moveList, tiles, positions)
                if move == '':
                #if there are no possible moves, just keep the same move and repeat the process
                    move = specificPiece
                movesList.append(move)

                moveCoords = tiles.get(move)
                clickPiece(moveCoords)
            else:
                #basic for lop system to find the only tile a pawn can to (only up)
                clickPiece(moveCoords)
                for key, val in tiles.items():
                    if val == moveCoords:
                        if key not in movesList:
                            if all(key not in positions for positions in positions.values()):
                                move = key
                                movesList.append(move)
        
        #if a piece is gonna get promoted
        if move[1] == promoTile:
            a = move[0]
            move = 'promo'

            promoInput = Promote()

            #pick which piece you want to promote to
            if promoInput == 'queen':
                moveCoords = tiles.get(a+'1')
            elif promoInput == 'knight':
                moveCoords = tiles.get(a+'2')
            elif promoInput == 'bishop':
                moveCoords = tiles.get(a+'3')
            elif promoInput == 'rook':
                moveCoords = tiles.get(a+'4')
            clickPiece(moveCoords)

    #moving a king
    elif piece == 'king':
        x = pieceCoords[0]
        y = pieceCoords[1]

        pc = [x+150, y]
        pc1 = [x-150, y]
        pc2 = [x, y+150]
        pc3 = [x, y-150]
        pc4 = [x+150, y+150]
        pc5 = [x+150, y-150]
        pc6 = [x-150, y+150]
        pc7 = [x-150, y-150]

        moveList = [pc, pc1, pc2, pc3, pc4, pc5, pc6, pc7]

        if pieceCoords == [3900, 1375]:
            #castling
            pc8 = [3600, 1375]
            pc9 = [4200, 1375]
            moveList.append(pc8)
            moveList.append(pc9)
        pc10 = [x, y]

        moveList.append(pc10)
        move = moveKing_Knight(moveList, pieceCoords, tiles, positions)

        if move == '':
            move = specificPiece

        moveCoords = tiles.get(move)
        clickPiece(moveCoords)
    #moving a knight
    elif piece == 'knight': 
        x = pieceCoords[0]
        y = pieceCoords[1]

        pc = [x+300, y+150]
        pc1 = [x+300, y-150]
        pc2 = [x-300, y+150]
        pc3 = [x-300, y-150]
        pc4 = [x+150, y+300]
        pc5 = [x-150, y+300]
        pc6 = [x+150, y-300]
        pc7 = [x-150, y-300]

        moveList = [pc, pc1, pc2, pc3, pc4, pc5, pc6, pc7]
        move = moveKing_Knight(moveList, pieceCoords, tiles, positions)

        if move == '':
            move = specificPiece


        moveCoords = tiles.get(move)
        clickPiece(moveCoords)
    #updating positions with the piece to be remembered next move
    value = positions[piece]
    index = value.index(specificPiece) 
    #updating the promotion 
    if move == 'promo':
        value.remove(a+unPromoTile)
        value = positions[promoInput]
        value.append(a+promoTile)
    else:
        value[index] = move 


listoflists = []  

colInput = ""

class Band:
    Delta = 0
    Theta = 1
    Alpha = 2
    Beta = 3


""" EXPERIMENTAL PARAMETERS """
# Modify these to change aspects of the signal processing

# Length of the EEG data buffer (in seconds)
# This buffer will hold last n seconds of data and be used for calculations
BUFFER_LENGTH = 5

# Length of the epochs used to compute the FFT (in seconds)
EPOCH_LENGTH = 1

# Amount of overlap between two consecutive epochs (in seconds)
OVERLAP_LENGTH = 0.8

# Amount to 'shift' the start of each next consecutive epoch
SHIFT_LENGTH = EPOCH_LENGTH - OVERLAP_LENGTH

# Index of the channel(s) (electrodes) to be used
# 0 = left ear, 1 = left forehead, 2 = right forehead, 3 = right ear
INDEX_CHANNEL = [0]

CLASS = 0

if __name__ == "__main__":

    """ 1. CONNECT TO EEG STREAM """

    # Search for active LSL streams
    print('Looking for an EEG stream...')
    streams = resolve_byprop('type', 'EEG', timeout=2)
    if len(streams) == 0:
        raise RuntimeError('Can\'t find EEG stream.')

    # Set active EEG stream to inlet and apply time correction
    print("Start acquiring data")
    inlet = StreamInlet(streams[0], max_chunklen=12)
    eeg_time_correction = inlet.time_correction()

    # Get the stream info and description
    info = inlet.info()
    description = info.desc()

    # Get the sampling frequency
    # This is an important value that represents how many EEG data points are
    # collected in a second. This influences our frequency band calculation.
    # for the Muse 2016, this should always be 256
    fs = int(info.nominal_srate())

    """ 2. INITIALIZE BUFFERS """

    # Initialize raw EEG data buffer
    eeg_buffer = np.zeros((int(fs * BUFFER_LENGTH), 1))
    filter_state = None  # for use with the notch filter

    # Compute the number of epochs in "buffer_length"
    n_win_test = int(np.floor((BUFFER_LENGTH - EPOCH_LENGTH) /
                              SHIFT_LENGTH + 1))

    # Initialize the band power buffer (for plotting)
    # bands will be ordered: [delta, theta, alpha, beta]
    band_buffer = np.zeros((n_win_test, 4))

    """ 3. GET DATA """

    # The try/except structure allows to quit the while loop by aborting the
    # script with <Ctrl-C>
    print('Press Ctrl-C in the console to break the while loop.')
    colInput = colour()

    try:
        # The following loop acquires data, computes band powers, and calculates neurofeedback metrics based on those band powers
        while True:
            """ 3.1 ACQUIRE DATA """
            # Obtain EEG data from the LSL stream
            eeg_data, timestamp = inlet.pull_chunk(
                timeout=1, max_samples=int(SHIFT_LENGTH * fs))

            # Only keep the channel we're interested in
            ch_data = np.array(eeg_data)[:, INDEX_CHANNEL]

            # Update EEG buffer with the new data
            eeg_buffer, filter_state = lsl_utils.update_buffer(
                eeg_buffer, ch_data, notch=True,
                filter_state=filter_state)

            """ 3.2 COMPUTE BAND POWERS """
            # Get newest samples from the buffer
            data_epoch = lsl_utils.get_last_data(eeg_buffer,
                                             EPOCH_LENGTH * fs)
            
            list0 = []
            data = data_epoch[-1]
            list0.append(data[-1])
            ch_data = np.array(eeg_data)[:, 1]

            listoflists.append(list0)
            if len(listoflists) >= 2:
                latest = listoflists[-1]
                secondlatest = listoflists[-2]
                spike = latest[0] - secondlatest[0]
                if spike >= 100:
                    move()
    except KeyboardInterrupt:
        print('Closing!')