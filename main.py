import numpy as np  # Module that simplifies computations on matrices
from pylsl import StreamInlet, resolve_byprop  # Module to receive EEG data
import lsl_utils  # Our own utility functions
import chess_utils # another set of functions made by me

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

    elif colInput == 'black':
        tiles = Btiles
        positions = Bpositions
        promoTile = '1'
        unPromoTile = '2'

    #pick what piece
    piece = chess_utils.pickPiece(positions)

    #get the tile the piece we inputted is at
    pieceTile = positions.get(piece)

    #if there's only of that piece, select the only one, else make a window for that
    if len(pieceTile) == 1:
        specificPiece = pieceTile[0]
        
    else:
        specificPiece = chess_utils.getSpecificPiece(pieceTile)
    
    #specific coordinates for the screen
    pieceCoords = tiles.get(specificPiece)
    chess_utils.clickPiece(pieceCoords)
    

    #queen, rook and bishops use a file/rank system to move
    if piece == 'queen' or piece == 'rook' or piece == 'bishop':

        #pick what rank to move to 
        fileInput = chess_utils.filePick()

        #pick what file to move to
        rankInput = chess_utils.pickRank()

        move = fileInput + rankInput
        moveCoords = tiles.get(move)
        chess_utils.clickPiece(moveCoords)
    elif piece == 'pawn':
        #working with a pawn
        
        moveCoords = pieceCoords
        z = pieceCoords[1]
        moveCoords[1] = pieceCoords[1] - 150

        #this was the window to pick if you want to take a piece or not
        takeInput = chess_utils.take()
        
        if takeInput == 'take':

            x = pieceCoords[0]
            moveCoords[0] = x - 150     
            z = moveCoords[1]
            y = [x+150, z]

            #movelist has all the possible moves it can do
            moveList = [moveCoords, y]
            move = chess_utils.takeSpecificPiece(moveList, colInput, positions)

        elif takeInput == 'move':

            #when the pawn is on its first turn, it can move twice 
            if z == 1225:
                x = pieceCoords[0]
                y = pieceCoords[1]

                pc = [x, y]
                pc1 = [x, y-150]

                moveList = [pc, pc1]
                move = chess_utils.pawnMove(moveList, colInput, positions)
                if move == '':
                #if there are no possible moves, just keep the same move and repeat the process
                    move = specificPiece
                movesList.append(move)

                moveCoords = tiles.get(move)
                chess_utils.clickPiece(moveCoords)
            else:
                #basic for lop system to find the only tile a pawn can to (only up)
                chess_utils.clickPiece(moveCoords)
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

            promoInput = chess_utils.Promote()

            #pick which piece you want to promote to
            if promoInput == 'queen':
                moveCoords = tiles.get(a+'1')
            elif promoInput == 'knight':
                moveCoords = tiles.get(a+'2')
            elif promoInput == 'bishop':
                moveCoords = tiles.get(a+'3')
            elif promoInput == 'rook':
                moveCoords = tiles.get(a+'4')
            chess_utils.clickPiece(moveCoords)

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
        move = chess_utils.moveKing_Knight(moveList, colInput, pieceCoords, positions)

        if move == '':
            move = specificPiece

        moveCoords = tiles.get(move)
        chess_utils.clickPiece(moveCoords)
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
        move = chess_utils.moveKing_Knight(moveList, colInput, pieceCoords, positions)

        if move == '':
            move = specificPiece


        moveCoords = tiles.get(move)
        chess_utils.clickPiece(moveCoords)
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
    colInput = chess_utils.colour()

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