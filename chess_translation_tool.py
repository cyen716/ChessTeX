import chess
import chess.pgn
import re
from chessboard_tool import is_valid_fen as ivf
import chessboard_tool
import chess_project_defNs

special_moves=['Castles', 'e.p.']
#this chunk translates individual moves from descriptive to algebraic

def chop(dex_move, delimiter):
    return re.split(delimiter,dex_move)

def descriptive_to_algebraic(dex_move,position):
    #Check that the position is in FEN format
    if ivf(position) == False:
        pass

    else:
        board=chess.Board(position)

        original_position=position

        #this chunk just so we don't have NoneType error later
        fix_rank_ambiguity, fix_file_ambiguity, fix_initial_square_ambiguity, fix_target_square_ambiguity, fix_capture_ambiguity =False, False, False, False, False
        moved_already=False
        promo_piece=''
        move=''


    #this chunk determines whose turn it is
        if chessboard_tool.breakdown_fen(position)[1] == 'w':
            my_pieces, their_pieces = 'WHITE', 'BLACK'
        elif chessboard_tool.breakdown_fen(position)[1] == 'b':
            my_pieces, their_pieces = 'BLACK', 'WHITE'

        if dex_move in special_moves:
            if dex_move=='Castles':
                #Castle algorithm
                if my_pieces=='WHITE':
                    initial_squares=['e1']
                    target_squares=['c1','g1']
                if my_pieces=='BLACK':
                    initial_squares=['e8']
                    target_squares=['c8','g8']

            elif dex_move=='e.p.':
                #e.p. algorithm
                target_squares=[chessboard_tool.breakdown_fen(position)[3]]

                if my_pieces=='WHITE':
                    #just looking for anything on the fifth rank and acting as if it can e.p.
                    initial_squares=['a5','b5','c5','d5','e5','f5','g5','h5']
                if my_pieces=='BLACK':
                    initial_squares=['a4','b4','c4','d4','e4','f4','g4','h4']

            move=''
            for i in initial_squares:
                for j in target_squares:
                    if i !=j:
                        potential_move=chess.Move.from_uci(i+j)
                        if potential_move in board.legal_moves:
                            move=potential_move
            
            if move=='':
                print('NO_SUCH_MOVE_ERROR')
            else:
                algebraic_move=board.san(move)
                board.push(move)
                moved_already=True

        elif '=' in dex_move:
            promo_piece=dex_move[-1].lower()
            dex_move=dex_move[:-2]

        if 'x' in dex_move and moved_already==False:
            #Capture algorithm
            capture = r'x'
            chopped_move =chop(dex_move,capture)
            X=chopped_move[0]
            Y=chopped_move[1]

            if '(' in X:
                #if there is a specific square the piece comes from this takes care of it
                outside_before, inside_and_after = X.split('(', 1)
                inside, outside_after = inside_and_after.split(')', 1)
                X = outside_before.strip() + " " + outside_after.strip()
                fix_initial_square_ambiguity=True
            
            if '(' in Y:
                #if there is a specific square the piece comes from this takes care of it
                outside_before, inside_and_after = Y.split('(', 1)
                inside, outside_after = inside_and_after.split(')', 1)
                Y = outside_before.strip() + " " + outside_after.strip()
                fix_target_square_ambiguity=True

            if len(X) == 1:
                moving_piece_name = chess_project_defNs.Piece_dict.get(X)

            elif len(X) == 2 or len(X) == 3:
                #This is an incomplete way of solving the ambiguity problem
                if X[-1].isdigit():
                    fix_rank_ambiguity=True
                    moving_piece_name = chess_project_defNs.Piece_dict.get(X[-2])
                    initial_rank = int(X[-1])
                elif X[-1].isalpha():
                    fix_file_ambiguity=True
                    moving_piece_name = chess_project_defNs.Piece_dict.get(X[-1])
                    if moving_piece_name!='PAWN':
                        wing = X[:-1]
                    elif moving_piece_name == 'PAWN':
                        wing = 'N/A'
                        initial_file=chess_project_defNs.File_to_num_dict.get(X[:-1])

                elif moving_piece_name.isdigit():
                    fix_rank_ambiguity=True
                    initial_rank=moving_piece_name
                    moving_piece_name=chess_project_defNs.Piece_dict.get(X[-2])
            
            if len(Y) == 1:
                eaten_piece_name = chess_project_defNs.Piece_dict.get(Y)

            elif len(Y) == 2 or len(Y) == 3:
                fix_capture_ambiguity=True
                #This is an incomplete way of solving the ambiguity problem
                target_file=chess_project_defNs.File_to_num_dict.get(Y[:-1])
                eaten_piece_name = chess_project_defNs.Piece_dict.get(Y[-1])

            moving_piece, eaten_piece = getattr(chess,moving_piece_name), getattr(chess,eaten_piece_name)
            moving_color, eaten_color= getattr(chess,my_pieces), getattr(chess,their_pieces)
            initial_square_indices, target_square_indices= list(board.pieces(moving_piece,moving_color)), list(board.pieces(eaten_piece,eaten_color))
            
            if fix_file_ambiguity==True:
                if wing=='Q':
                    if (initial_square_indices[0]%8)<(initial_square_indices[1]%8):
                        initial_square_indices=[initial_square_indices[0]]
                    else:
                        initial_square_indices=[initial_square_indices[1]]
                elif wing=='K':
                    if (initial_square_indices[0]%8)<(initial_square_indices[1]%8):
                        initial_square_indices=[initial_square_indices[1]]
                    else:
                        initial_square_indices=[initial_square_indices[0]]
                elif wing=='N/A':
                    dummy_list=[]
                    for i in initial_square_indices:
                        if i%8 in initial_file:
                            dummy_list.append(i)
                    initial_square_indices=dummy_list.copy

            if fix_rank_ambiguity==True:
                if my_pieces=='WHITE':
                    if initial_square_indices[0]<(initial_rank-1)*8 or initial_square_indices[0]>(initial_rank*8)-1:
                        initial_square_indices=[initial_square_indices[1]]
                    else:
                        initial_square_indices=[initial_square_indices[0]]
                elif my_pieces=='BLACK':
                    if initial_square_indices[0]<((9-initial_rank)-1)*8 or initial_square_indices[0]>((9-initial_rank)*8)-1:
                        initial_square_indices=[initial_square_indices[1]]
                    else:
                        initial_square_indices=[initial_square_indices[0]]
            
            if fix_capture_ambiguity==True:
                potential_target_square_indices=target_square_indices.copy()
                target_square_indices=[]
                for i in potential_target_square_indices:
                    if (i+1)%8 in target_file:
                        target_square_indices.append(i)

            initial_squares, target_squares= [chess.square_name(i) for i in initial_square_indices], [chess.square_name(i) for i in target_square_indices]
            
            if fix_initial_square_ambiguity==True:
                if my_pieces== 'WHITE':
                    initial_file=inside[-1]
                elif my_pieces== 'BLACK':
                    initial_file=str(9-int(inside[-1]))
                potential_initial_squares_1= [i+ initial_file for i in chess_project_defNs.File_dict.get(inside[:-1])]
                potential_initial_squares_2= initial_squares.copy()
                initial_squares=[]
                for i in potential_initial_squares_1:
                    if i in potential_initial_squares_2:
                        initial_squares.append(i)

            if fix_target_square_ambiguity==True:
                if my_pieces== 'WHITE':
                    target_file=inside[-1]
                elif my_pieces== 'BLACK':
                    target_file=str(9-int(inside[-1]))
                potential_target_squares_1= [i+ target_file for i in chess_project_defNs.File_dict.get(inside[:-1])]
                potential_target_squares_2= target_squares.copy()
                target_squares=[]
                for i in potential_target_squares_1:
                    if i in potential_target_squares_2:
                        target_squares.append(i)
            move=''
            for i in initial_squares:
                for j in target_squares:
                    if i !=j:
                        potential_move=chess.Move.from_uci(i+j+promo_piece)
                        if potential_move in board.legal_moves:
                            move=potential_move
            
            if move=='':
                print('NO_SUCH_MOVE_ERROR')
            else:
                algebraic_move=board.san(move)
                board.push(move)
                moved_already=True

        if '-' in dex_move and moved_already==False:
            #non-capture algorithm
            dash = r'-'
            chopped_move =chop(dex_move,dash)
            X=chopped_move[0]
            Y=chopped_move[1]

            if '(' in X:
                #if there is a specific square the piece comes from this takes care of it
                outside_before, inside_and_after = X.split('(', 1)
                inside, outside_after = inside_and_after.split(')', 1)
                X = outside_before.strip() + " " + outside_after.strip()
                fix_initial_square_ambiguity=True
            
            if len(X) == 1:
                moving_piece_name = chess_project_defNs.Piece_dict.get(X)

            elif len(X) == 2 or len(X) == 3:
                #This is an incomplete way of solving the ambiguity problem
                if X[-1].isdigit():
                    fix_rank_ambiguity=True
                    moving_piece_name = chess_project_defNs.Piece_dict.get(X[-2])
                    initial_rank = int(X[-1])
                elif X[-1].isalpha():
                    fix_file_ambiguity=True
                    moving_piece_name = chess_project_defNs.Piece_dict.get(X[-1])
                    wing = X[:-1]

            if Y[-1].isdigit():
                target_files=chess_project_defNs.File_dict.get(Y[:-1])
                if my_pieces=='WHITE':
                    target_rank=Y[-1]
                else:
                    target_rank=str(9-int(Y[-1]))
            else:
                target_files=chess_project_defNs.File_dict.get(Y[0])
                if my_pieces=='WHITE':
                    target_rank='1'
                else:
                    target_rank='8'
            moving_piece = getattr(chess, moving_piece_name)
            moving_color= getattr(chess, my_pieces)
            initial_square_indices= list(board.pieces(moving_piece, moving_color))
            #This chunk fixes situations where two of the same piece can move to a square
            #Code must be rewritten if there are more than two 
            #SIKE!!! Let's just ignore those situations
            if fix_file_ambiguity==True:
                if wing=='Q':
                    if (initial_square_indices[0]%8)<(initial_square_indices[1]%8):
                        initial_square_indices=[initial_square_indices[0]]
                    else:
                        initial_square_indices=[initial_square_indices[1]]
                elif wing=='K':
                    if (initial_square_indices[0]%8)<(initial_square_indices[1]%8):
                        initial_square_indices=[initial_square_indices[1]]
                    else:
                        initial_square_indices=[initial_square_indices[0]]

            if fix_rank_ambiguity==True:
                if my_pieces=='WHITE':
                    if initial_square_indices[0]<(initial_rank-1)*8 or initial_square_indices[0]>(initial_rank*8)-1:
                        initial_square_indices=[initial_square_indices[1]]
                    else:
                        initial_square_indices=[initial_square_indices[0]]
                elif my_pieces=='BLACK':
                    if initial_square_indices[0]<((9-initial_rank)-1)*8 or initial_square_indices[0]>((9-initial_rank)*8)-1:
                        initial_square_indices=[initial_square_indices[1]]
                    else:
                        initial_square_indices=[initial_square_indices[0]]

            initial_squares= [chess.square_name(i) for i in initial_square_indices]
            target_squares= [i + target_rank for i in target_files]

            if fix_initial_square_ambiguity==True:
                if my_pieces== 'WHITE':
                    initial_file=inside[-1]
                elif my_pieces== 'BLACK':
                    initial_file=str(9-int(inside[-1]))
                potential_initial_squares_1= [i+ initial_file for i in chess_project_defNs.File_dict.get(inside[:-1])]
                potential_initial_squares_2= initial_squares.copy()
                initial_squares=[]
                for i in potential_initial_squares_1:
                    if i in potential_initial_squares_2:
                        initial_squares.append(i)

            for i in initial_squares:
                for j in target_squares:
                    if i !=j:
                        potential_move=chess.Move.from_uci(i+j+promo_piece)
                        if potential_move in board.legal_moves:
                            move=potential_move
            if move=='':
                print('NO_SUCH_MOVE_ERROR')
            else:
                algebraic_move=board.san(move)
                board.push(move)
                moved_already=True
            
        return {'alg': algebraic_move, 'position_after_move': board.fen(), 'original_position': original_position }