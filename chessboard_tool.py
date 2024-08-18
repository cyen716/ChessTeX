from PIL import Image, ImageDraw, ImageFont
import numpy as np
import re

#Note to self: do I want to use FEN or just a numpy array for storing positions?
#ANSWER: Why not support both?
#Note to self: chessboard should probably be flippable

#this chunk of code is just there to get the directory, maybe delete it when done?
#Nah actually don't it's useful
import os
print("Current Working Directory:", os.getcwd())

import chess

def is_valid_fen(fen_string):
    try:
        # Create a board from the FEN string
        testboard = chess.Board(fen_string)
        return True  # If no exception is raised, it's a valid FEN
    except ValueError:
        return False  # If a ValueError is raised, it's not valid


def is_valid_Array_position(position):
    valid_pieces={'K','Q','B','R','N','P','k','q','b','r','n','p','null'}
    response= True
    if position.shape != (8,8):
        response= False
    for i in range(8):
        for j in position[i]:
            if j not in valid_pieces:
                response=False
    return(response)            

def position_input(position):
#determines the format the position is stored in
    if isinstance(position, np.ndarray) == True and is_valid_Array_position(position) == True:
        return "Array"
    elif isinstance(position, str) == True and is_valid_fen(position)== True:
        return "FEN"
    else:
        return "INVALID"

def breakdown_fen(FEN):
    return tuple(FEN.split())

#note to self: need to factor in flipping the chessboard later
def display(position, orientation, filename='generic'):
    #start by creating a blank chessboard
    border = 25
    square_size = 60
    chessboard = Image.new('RGB', (8*square_size + 2*border, 8*square_size + 2*border), 'gray')
    draw = ImageDraw.Draw(chessboard)
    for row in range(8):
        for col in range(8):
            top_left = (col * square_size + border, row * square_size + border) 
            bottom_right = ((col + 1) * square_size +border, (row + 1) * square_size +border) 
            if (row + col) % 2 == 0:
                draw.rectangle([top_left, bottom_right], fill='white')
            else:
                draw.rectangle([top_left, bottom_right], fill=(173,216,230))
    #Update this when you have the time
    pieces = {
    'K': Image.open('Chesspieces/whiteking60.png'),
    'Q': Image.open('Chesspieces/whitequeen60.png'),
    'R': Image.open('Chesspieces/whiterook60.png'),
    'B': Image.open('Chesspieces/whitebishop60.png'),
    'N': Image.open('Chesspieces/whiteknight60.png'),
    'P': Image.open('Chesspieces/whitepawn60.png'),
    'k': Image.open('Chesspieces/blackking60.png'),
    'q': Image.open('Chesspieces/blackqueen60.png'),
    'r': Image.open('Chesspieces/blackrook60.png'),
    'b': Image.open('Chesspieces/blackbishop60.png'),
    'n': Image.open('Chesspieces/blackknight60.png'),
    'p': Image.open('Chesspieces/blackpawn60.png')
    }

    #This chunk of code for the coordinates of the chessboard
    #coordinates done!!
    ranks = ["1","2","3","4","5","6","7","8"]
    files = ["a","b","c","d","e","f","g","h"]

    font_size=20
    font = ImageFont.truetype("arial.ttf", font_size)
    left_coord = (border*0.5-0.25*font_size,border*0.5+square_size*0.5)
    right_coord = (border*1.5+square_size*8-0.25*font_size,border*0.5+square_size*0.5)
    top_coord = (border+square_size*0.5-0.25*font_size,border*0.5-font_size*0.5)
    bottom_coord = (border+square_size*0.5-0.25*font_size,border*1.5+square_size*8-font_size*0.5)
    
    if orientation == 0:
        for i in reversed(ranks):
            draw.text(left_coord,i,font=font,fill="black")
            draw.text(right_coord,i,font=font,fill="black")
            #Note to self: figure out why tuples have to be added this way
            left_coord=tuple(np.add(left_coord,(0,square_size)))
            right_coord=tuple(np.add(right_coord,(0,square_size)))
        for j in files:
            draw.text(top_coord,j,font=font,fill="black")
            draw.text(bottom_coord,j,font=font,fill="black")
            #Note to self: figure out why tuples have to be added this way
            top_coord=tuple(np.add(top_coord,(square_size,0)))
            bottom_coord=tuple(np.add(bottom_coord,(square_size,0)))
    else:
        for i in ranks:
            draw.text(left_coord,i,font=font,fill="black")
            draw.text(right_coord,i,font=font,fill="black")
            #Note to self: figure out why tuples have to be added this way
            left_coord=tuple(np.add(left_coord,(0,square_size)))
            right_coord=tuple(np.add(right_coord,(0,square_size)))
        for j in reversed(files):
            draw.text(top_coord,j,font=font,fill="black")
            draw.text(bottom_coord,j,font=font,fill="black")
            #Note to self: figure out why tuples have to be added this way
            top_coord=tuple(np.add(top_coord,(square_size,0)))
            bottom_coord=tuple(np.add(bottom_coord,(square_size,0)))

    if position_input(position) == "Array":
        for square_location, piece in np.ndenumerate(position):
            if piece != 'null' and piece in pieces:
                if orientation == 0:
                    x,y = square_location
                    top_left= (x*square_size + border, y*square_size + border) 
                    chessboard.paste(pieces[piece],top_left,pieces[piece])
                else:
                    x,y = tuple(np.subtract((7,7),square_location))
                    top_left= (x*square_size +border, y*square_size +border) 
                    chessboard.paste(pieces[piece],top_left,pieces[piece])
    elif position_input(position) == "FEN":
        piece_config, active_player, castling_rights, ep_square, halfmove, fullmove = breakdown_fen(position)
        rank_config = piece_config.split("/")
        if orientation == 0:
            for i in range(8):
                x=0
                rank=list(rank_config[i])
                for j in rank:
                    if j in pieces:
                        top_left= (x*square_size +border, i*square_size +border) 
                        chessboard.paste(pieces[j],top_left,pieces[j])
                        x=x+1
                    else:
                        x=x+int(j)
        else:
            for i in range(8):
                x=7
                rank=list(rank_config[i])
                for j in rank:
                    if j in pieces:
                        top_left= (x*square_size +border, (7-i)*square_size+ border) 
                        chessboard.paste(pieces[j],top_left,pieces[j])
                        x=x-1
                    else:
                        x=x-int(j)
    else:
        print("Invalid position!")
    #Change the file name down here
    diagram_directory=f'Diagrams/{filename}.png'
    chessboard.save(diagram_directory)

if __name__ == '__main__':
    display('rnbqkbnr/ppp1pppp/8/3p4/4P3/8/PPPP1PPP/RNBQKBNR w KQkq d6 0 2',0,'kliphort')