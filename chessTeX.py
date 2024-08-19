import chess
import chessboard_tool
import chess_translation_tool
from fpdf import FPDF
import re

def take_first_argument(input_string):
    # Find the index of the first whitespace
    split_index = input_string.find(' ')
    
    # If there is no whitespace, the whole string is considered the first chunk
    if split_index == -1:
        first_chunk = input_string
        remaining_chunk = ''
    else:
        # Extract the first chunk and the remaining chunk
        first_chunk = input_string[:split_index]
        remaining_chunk = input_string[split_index + 1:]
    
    # Check for curly brackets in the first chunk
    exists_curly_brackets = '{' in first_chunk or '}' in first_chunk
    
    # Strip curly brackets from the first chunk
    stripped_chunk = first_chunk.strip('{}')
    
    return stripped_chunk, remaining_chunk, exists_curly_brackets

def mass_translate_into_cell(line, initial_position='rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1', mainline= True):
    move_number=int(chessboard_tool.breakdown_fen(initial_position)[5])
    if chessboard_tool.breakdown_fen(initial_position)[1]=='w':
        move_number-=1
    position= initial_position
    next_to_last_position=''
    text = ''
    current_line='. .'
    annotation=''
    if mainline == True:
        new_move_symbol= '\n'
    elif mainline == False:
        new_move_symbol = ' '
    while len(line) !=0:
        argument, line, special_argument = take_first_argument(line)
        if special_argument== True:
            if argument=='D':
                if current_line != '. . .':
                    #write current line of text into the cell $$$
                    chessboard_tool.display(position,0,'image_for_pdf')
                    diagram = True
            elif argument[0] == 'B':
                try:
                    saved_positions
                except NameError:
                    # If it doesn't exist, create the dictionary with the key-value pair
                    saved_positions = {argument: position}
                else:
                    # If it exists, add the key-value pair to the dictionary
                    saved_positions[argument] = position
            else:
                text = text + ' '+ argument + new_move_symbol
            #other special arguments to be added here if neccesary
        elif special_argument == False:
            if argument[-2]=='?' or argument[-2]=='!':
                argument, annotation= argument[:-2], argument[-2]+argument[-1]
            if argument[-1]=='?' or argument [-1]=='!':
                argument, annotation= argument[:-1], argument[-1]
            alg_move= chess_translation_tool.descriptive_to_algebraic(argument, position).get('alg')
            next_to_last_position = chess_translation_tool.descriptive_to_algebraic(argument, position).get('original_position')
            position = chess_translation_tool.descriptive_to_algebraic(argument, position).get('position_after_move')
            if chessboard_tool.breakdown_fen(position)[1]== 'w':
                current_line= current_line + ' '+ alg_move + annotation
                move_number= int(chessboard_tool.breakdown_fen(position)[5])-1
                text = text + str(move_number) + '. ' + current_line + new_move_symbol
                current_line= '. .'
            elif chessboard_tool.breakdown_fen(position)[1] == 'b':
                current_line= alg_move + annotation
    if current_line != '. .':
        text = text + str(move_number+1) + '. ' + current_line + new_move_symbol
    return text, position, next_to_last_position

def sideline_interpreter(string,position):
    sideline=''
    sideline_level=0
    node_tracker=[position]
    current_position=position
    next_to_last_position=position
    text=''
    if chessboard_tool.breakdown_fen(position)[1]=='b':
        text=f'{chessboard_tool.breakdown_fen(position)[5]} . . . '
    while len(string) !=0:
        argument, string, comment =take_first_argument(string)
        annotation=''

        if comment == True:
            sideline = sideline + argument
            
        elif comment == False and argument[0] == '<':
            if argument[-2]=='?' or argument[-2]=='!':
                argument, annotation= argument[:-2], argument[-2]+argument[-1]
            if argument[-1]=='?' or argument[-1]=='!':
                argument, annotation= argument[:-1], argument[-1]
            sideline_level+=1
            try:
                node_tracker[sideline_level]=current_position
            except IndexError:
                node_tracker.append(current_position)
            current_position=next_to_last_position
            argument= argument[1:]
            alg_move= chess_translation_tool.descriptive_to_algebraic(argument, current_position).get('alg')
            next_to_last_position = chess_translation_tool.descriptive_to_algebraic(argument, current_position).get('original_position')
            current_position = chess_translation_tool.descriptive_to_algebraic(argument, current_position).get('position_after_move')
            if chessboard_tool.breakdown_fen(current_position)[1] == 'w':
                move_num = str(int(chessboard_tool.breakdown_fen(current_position)[5])-1)
                text = text+ f'({move_num} . . . {alg_move}{annotation} '
            elif chessboard_tool.breakdown_fen(current_position)[1] == 'b':
                move_num = chessboard_tool.breakdown_fen(current_position)[5]
                text = text+ f'({move_num}. {alg_move}{annotation} '

        elif comment == False and argument[0] == '>':
            current_position=node_tracker.pop()
            sideline_level=sideline_level-1
            text = text[:-1] + ') '

        elif comment == False and argument[0] != '<':
            if argument[-2]=='?' or argument[-2]=='!':
                argument, annotation= argument[:-2], argument[-2]+argument[-1]
            if argument[-1]=='?' or argument [-1]=='!':
                argument, annotation= argument[:-1], argument[-1]
            alg_move= chess_translation_tool.descriptive_to_algebraic(argument, current_position).get('alg')
            next_to_last_position = chess_translation_tool.descriptive_to_algebraic(argument, current_position).get('original_position')
            current_position = chess_translation_tool.descriptive_to_algebraic(argument, current_position).get('position_after_move')
            if chessboard_tool.breakdown_fen(current_position)[1] == 'w':
                move_num = str(int(chessboard_tool.breakdown_fen(current_position)[5])-1)
                text = text+ f'{alg_move}{annotation} '
            elif chessboard_tool.breakdown_fen(current_position)[1] == 'b':
                move_num = chessboard_tool.breakdown_fen(current_position)[5]
                text = text+ f'{move_num}. {alg_move}{annotation} '
    return text

def replace_dollar_contents(input_string,position):
    # This regex finds all instances of text within $...$
    pattern = r'\$(.*?)\$'
    
    # Function to apply to each match
    def replacer(match):
        # Extract the content between the dollar symbols
        content = match.group(1)
        # Process the content with the dynamic_replace function
        return sideline_interpreter(content,position)
    
    # Use re.sub to replace each match in the string with the processed content
    result = re.sub(pattern, replacer, input_string)
    
    return result

class Throw_stuff_onto_the_pdf:

    def begin_pdf(self):
        self.pdf= FPDF()
        self.pdf.add_page()
        self.pdf.set_font('Times',size=12)
        self.x, self.y=15, 20
        self.current_position='rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
        self.next_to_last_position='N/A'
        self.diagram_count=0

    def new_page(self):
        self.pdf.add_page()
        self.pdf.x,self.pdf.y= 15, 20

    def next_column(self):
        if self.pdf.x == 15:
            self.pdf.x = 115
            self.pdf.y = 20
        elif self.pdf.x == 115:
            self.new_page()

    def new_game(self, header=''):
        self.current_position='rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
        self.next_to_last_position='N/A'

    def mainline(self,line, position='N/A'):
        orig_coord = self.pdf.x
        if position== 'N/A':
            position=self.current_position
        text, self.current_position, self.next_to_last_position = mass_translate_into_cell(line,position)
        self.pdf.multi_cell(80,10,text=text)
        if self.y <277:
            self.x=orig_coord
        else:
            self.next_column()
        #Need some code to break up this into multiple pages/columns if necessary$$$$$$$

    def comment(self,string, position='N/A'):
        orig_coord = self.pdf.x
        if position== 'N/A':
            position=self.next_to_last_position
        text = replace_dollar_contents(string, position)
        self.pdf.multi_cell(80,10,text=text)
        if self.y <277:
            self.x=orig_coord
        else:
            self.next_column()
        #Need something to break up this into multiple pages/columns if necessary$$$$$$$

    def diagram(self,position='N/A', orientation='N/A'):
        orig_coord=self.pdf.x
        if position== 'N/A':
            position=self.current_position
        if orientation == 'N/A':
            if chessboard_tool.breakdown_fen(self.current_position)[1]== 'w':
                orientation=0
            elif chessboard_tool.breakdown_fen(self.current_position)[1]== 'b':
                orientation=1
        chessboard_tool.display(position,orientation,f'image_for_pdf{str(self.diagram_count)}')
        path_to_image= f'Diagrams/image_for_pdf{str(self.diagram_count)}.png'
        self.diagram_count+=1
        image_dimensions=80
        if self.pdf.get_y()<197:
            self.pdf.image(path_to_image,self.x,self.pdf.get_y()-5,image_dimensions,image_dimensions)
        else:
            self.next_column()
            self.pdf.image(path_to_image,self.x,self.y, image_dimensions,image_dimensions)
        if self.y <197:
            self.x=orig_coord
            self.pdf.y += 80
        else:
            self.next_column()
        #If you want, maybe add some text under the diagram (Figure X.X.XXXX Blah blah blah) to make it look professional
        #Make sure theres enough space on the column/page for a diagram$$$$$$$

    def end_pdf(self,doc_name='generic_pdf'):
        self.pdf.output(f'PDFs/{doc_name}.pdf')


#testing
if __name__ == '__main__' and 1 == 1:
    _ = Throw_stuff_onto_the_pdf()
    _.begin_pdf()
    _.mainline('P-K4 P-K4')
    _.diagram()
    _.mainline('Q-R5 N-QB3 B-B4')
    _.diagram()
    _.mainline(('P-KN3 '#3
                'Q-B3 P-B4 '
                'PxP PxP '
                'Q-R5 K-K2 '
                'Q-B7 K-Q3 '
                'P-Q4 PxP '
                'B-KN5 N-R3?? '))
    _.diagram()
    _.comment('This is a blunder because Black missed $QxB <Q-B3? BxQ > Q-Q5 K-K2$ and instead White wins on the next move.')
    _.mainline('Q-Q5')
    _.diagram()
    _.end_pdf('Becoming_more_Texxie_12')