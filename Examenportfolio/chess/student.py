

class Piece:
    def __init__(self, code):
        self.code=code          #everytime we generate a piece we give it a code (Piece(Qw) )
    
    def get_code(self):         
        return self.code
    
    def get_kind(self):
        return self.code[0]
    
    def get_player(self):
        return self.code[1]
    
    def __repr__(self):
        return self.code
    

    
class Board:
    def __init__(self):
        self.positions = {}
        self.load_all_positions()
        
    def put_piece_on_position(self, piece, position):
        self.positions[position]= piece             #make a key in the dict positions, the key is the poisition and the value is the piece object

    def get_piece_by_position(self, position):
        return self.positions.get(position, None)
    
    def load_all_positions(self):
        for col in "abcdefgh":
            self.put_piece_on_position(Piece("pw"), f"{col}2")
            self.put_piece_on_position(Piece("pb"), f"{col}7")

        # Rooks
        self.put_piece_on_position(Piece("Rw"), "a1")
        self.put_piece_on_position(Piece("Rw"), "h1")
        self.put_piece_on_position(Piece("Rb"), "a8")
        self.put_piece_on_position(Piece("Rb"), "h8")

        # Knights
        self.put_piece_on_position(Piece("Nw"), "b1")
        self.put_piece_on_position(Piece("Nw"), "g1")
        self.put_piece_on_position(Piece("Nb"), "b8")
        self.put_piece_on_position(Piece("Nb"), "g8")

        # Bishops
        self.put_piece_on_position(Piece("Bw"), "c1")
        self.put_piece_on_position(Piece("Bw"), "f1")
        self.put_piece_on_position(Piece("Bb"), "c8")
        self.put_piece_on_position(Piece("Bb"), "f8")

        # Queens
        self.put_piece_on_position(Piece("Qw"), "d1")
        self.put_piece_on_position(Piece("Qb"), "d8")

        # Kings
        self.put_piece_on_position(Piece("Kw"), "e1")
        self.put_piece_on_position(Piece("Kb"), "e8")
        
    #not used but same logic as save_state    
    def display_board_state(self):
        # Loop through rows in reverse order (8 to 1) to display from top to bottom like a chessboard
        for row in range(8, 0, -1):
            print(f"{row}:", end=" ")  # row number, e.g., "8: ", "7: ", etc.

            # Loop through columns 'a' to 'h' (left to right)
            for col in "abcdefgh":     
                pos = f"{col}{row}"  # create position string like "a8", "b7", etc.
                piece = self.get_piece_by_position(pos)  # variable named piece holds Piece object from current position

                if piece:
                    # If there is a piece, print its 2-character code (like 'wP' or 'bK')
                    # Pad to 2 spaces using '<2' for alignment, followed by a vertical separator '|'
                    print(f"{piece.get_code():<2} |", end=" ")
                else:
                    # If no piece is present at this position, print empty spaces for alignment
                    print("   |", end=" ")

            print()  # new line after each row to move to the next row on the board


        # Column headers
        print("   ", end="")  # indent to line up with row numbers
        for col in "abcdefgh":
            print(f" {col}   ", end="")  # 1 space before, 2 after → total 4
        print()  # newline

    def move_piece(self, start_pos, end_pos):
        piece = self.get_piece_by_position(start_pos)   # variable named piece holds Piece object from current position
        if piece is None:
            raise ValueError(f"No piece at {start_pos}")

        piece_to_take = self.get_piece_by_position(end_pos) #variable holds Piece object from position we want to go to
     
        if piece_to_take is None or piece.get_player() != piece_to_take.get_player():   # Check for friendly piece
            self.put_piece_on_position(piece, end_pos)  # Move the piece
            del self.positions[start_pos]
        else:
            raise ValueError("Illegal move: cannot move to friendly territory")

    def process_movements(self, movements):         
        for move in movements:
            self.move_piece(move[0], move[1])

    def read_movement_file(self, filename):
        movements = []
        with open(filename, "r", encoding="UTF-8") as file:
            for line in file:
                start, end =line.split('-')
                movements.append((start.strip(), end.strip()))
        return movements
    
    def save_state(self, file_name):
        with open(file_name, 'w', encoding='utf-8') as file:
            board_str = ""       # Build the board as a string
            for row in range(8, 0, -1):
                board_str += f"{row}: "
                for col in "abcdefgh":
                    pos = f"{col}{row}"
                    piece = self.get_piece_by_position(pos)
                    if piece:
                        board_str += f"{piece.get_code():<2} | "
                    else:
                        board_str += "   | "
                board_str += "\n"
            
            # Add column headers at the bottom
            board_str += "   "  # indent
            for col in "abcdefgh":
                board_str += f" {col}   "
            board_str += "\n"

            file.write(board_str)
        
board=Board()

def process_chess_moves(movement_file_name, output_file_name):
    moves = board.read_movement_file(movement_file_name)
    board.process_movements(moves)
    board.save_state(output_file_name)
    
        
        
process_chess_moves("Examenportfolio\\chess\\movements.txt", "Examenportfolio\\chess\\output.txt")
board.display_board_state
