import chess
import chessboard_tool
import chess_translation_tool
from fpdf import FPDF
import re

def take_first_argument(input_string):

    exists_curly_brackets=False

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
    exists_curly_brackets = '}' in first_chunk
    if exists_curly_brackets==True:
        # Strip curly brackets from the first chunk
        stripped_chunk = first_chunk.strip('{}')
    else:
        exists_curly_brackets= '{' in first_chunk
        if exists_curly_brackets==True:
            split_index = remaining_chunk.find('}')
            first_chunk= first_chunk+' '+remaining_chunk[:split_index]
            remaining_chunk=remaining_chunk[split_index + 2:]
            stripped_chunk = first_chunk.strip('{}')
        else:
            stripped_chunk=first_chunk
    
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
                annotation=''
                move_number= int(chessboard_tool.breakdown_fen(position)[5])-1
                text = text + str(move_number) + '. ' + current_line + new_move_symbol
                current_line= '. .'
            elif chessboard_tool.breakdown_fen(position)[1] == 'b':
                current_line= alg_move + annotation
                annotation=''
    if current_line != '. .':
        text = text + str(move_number+1) + '. ' + current_line + new_move_symbol
    return text, position, next_to_last_position

def sideline_interpreter(string,position):
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
            text = text + argument
            
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
        self.pdf.x, self.pdf.y=15, 20
        self.current_position='rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
        self.next_to_last_position='N/A'
        self.diagram_count=0
        self.lineheight=10
        self.pdf.set_auto_page_break(auto=False)
        self.column=-1

    def new_page(self):
        self.pdf.add_page()
        self.pdf.x,self.pdf.y= 15, 20

    def next_column(self):
        if self.column==-1:
            self.pdf.x, self.pdf.y=115,20
        elif self.column==1:
            self.new_page()
        self.column=self.column*(-1)
            

    def multiline_printer(self,string):
        lines = self.pdf.multi_cell(80,self.lineheight,string,dry_run=True,output='LINES',)
        height = len(lines)*self.lineheight
        if self.pdf.get_y()+height <=277:
            self.pdf.multi_cell(80,10,text=string)
        else:
            text_in_current_column=''
            text_in_next_column=''
            lines_printable= int((277-self.pdf.get_y())//self.lineheight)
            for i in range(lines_printable):
                text_in_current_column=text_in_current_column+lines[i]+' '
            for i in range(lines_printable,len(lines)):
                text_in_next_column= text_in_next_column+lines[i]+' '
            self.pdf.multi_cell(80,self.lineheight,text_in_current_column)
            self.next_column()

            self.pdf.multi_cell(80,self.lineheight,text_in_next_column)
        if self.pdf.get_y()>=277:
            self.next_column()
        if self.column==-1:
            self.pdf.x=15
        elif self.column==1:
            self.pdf.x=115

    def new_game(self, header=''):
        self.current_position='rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
        self.next_to_last_position='N/A'

    def mainline(self,line, position='N/A'):
        if position== 'N/A':
            position=self.current_position
        text, self.current_position, self.next_to_last_position = mass_translate_into_cell(line,position)
        lines=text.split('\n')
        if self.pdf.get_y()+(len(lines)*self.lineheight)<=277:
            self.pdf.multi_cell(80,self.lineheight,text)
        else:
            lines_printable= int((277-self.pdf.get_y())//self.lineheight)
            text_in_current_column, text_in_next_column= '', ''
            for i in range(lines_printable):
                text_in_current_column=text_in_current_column+lines[i]+'\n'
            for i in range(lines_printable,len(lines)):
                text_in_next_column= text_in_next_column+lines[i]+'\n'
            if text_in_current_column[-2:]=='\n':
                text_in_current_column=text_in_current_column[:-2]
            if text_in_next_column[-2:]=='\n':
                text_in_next_column=text_in_next_column[:-2]
            self.pdf.multi_cell(80,self.lineheight,text_in_current_column)
            self.next_column()
            self.pdf.multi_cell(80,self.lineheight,text_in_next_column)
            self.pdf.y=self.pdf.get_y()-10
        if self.pdf.get_y()>=277:
            self.next_column()
        self.pdf.y=self.pdf.get_y()-10
        if self.column==-1:
            self.pdf.x=15
        elif self.column==1:
            self.pdf.x=115

    def comment(self,string, position='N/A'):
        string= '    '+ string
        if position== 'N/A':
            position=self.current_position
        if position== 'B':
            position=self.next_to_last_position
        text = replace_dollar_contents(string, position)
        self.multiline_printer(text)
        if self.pdf.get_y()>=277:
            self.next_column()
        if self.column==-1:
            self.pdf.x=15
        elif self.column==1:
            self.pdf.x=115

    def diagram(self,position='N/A', orientation='N/A'):
        if position== 'N/A':
            position=self.current_position
        if position=='B':
            position=self.next_to_last_position
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
            self.pdf.image(path_to_image,self.pdf.x,self.pdf.y+5,image_dimensions,image_dimensions)
        else:
            self.next_column()
            self.pdf.image(path_to_image,self.pdf.x,self.pdf.y+5, image_dimensions,image_dimensions)
        if self.pdf.get_y()>=197:
            self.next_column()
        else:
            self.pdf.y=self.pdf.get_y()+90
        if self.column==-1:
            self.pdf.x=15
        elif self.column==1:
            self.pdf.x=115
        
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
    _.end_pdf('Becoming_more_Texxie_13')