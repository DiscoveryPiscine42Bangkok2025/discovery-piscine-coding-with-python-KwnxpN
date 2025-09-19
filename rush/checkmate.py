def find_king(board):
    """Find the position of the King on the board"""
    lines = board.strip().split('\n')
    for row in range(len(lines)):
        for col in range(len(lines[row])):
            if lines[row][col] == 'K':
                return row, col
    return None

def is_valid_position(row, col, board_lines):
    """Check if position is within board bounds"""
    return 0 <= row < len(board_lines) and 0 <= col < len(board_lines[0])

def check_pawn_attack(king_row, king_col, board_lines):
    """Check if King is attacked by a Pawn"""
    # Pawns attack diagonally upward (from King's perspective)
    pawn_positions = [
        (king_row + 1, king_col - 1),  # Bottom-left diagonal
        (king_row + 1, king_col + 1)   # Bottom-right diagonal
    ]
    
    for row, col in pawn_positions:
        if is_valid_position(row, col, board_lines):
            if board_lines[row][col] == 'P':
                return True
    return False

def check_rook_attack(king_row, king_col, board_lines):
    """Check if King is attacked by a Rook"""
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up
    
    for dr, dc in directions:
        row, col = king_row + dr, king_col + dc
        while is_valid_position(row, col, board_lines):
            piece = board_lines[row][col]
            if piece == 'R':
                return True
            elif piece != '.' and piece != ' ':
                break  # Path blocked by another piece
            row, col = row + dr, col + dc
    return False

def check_bishop_attack(king_row, king_col, board_lines):
    """Check if King is attacked by a Bishop"""
    directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]  # Diagonals
    
    for dr, dc in directions:
        row, col = king_row + dr, king_col + dc
        while is_valid_position(row, col, board_lines):
            piece = board_lines[row][col]
            if piece == 'B':
                return True
            elif piece != '.' and piece != ' ':
                break  # Path blocked by another piece
            row, col = row + dr, col + dc
    return False

def check_queen_attack(king_row, king_col, board_lines):
    """Check if King is attacked by a Queen (combines Rook and Bishop moves)"""
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0),  # Rook moves
                  (1, 1), (1, -1), (-1, 1), (-1, -1)]  # Bishop moves
    
    for dr, dc in directions:
        row, col = king_row + dr, king_col + dc
        while is_valid_position(row, col, board_lines):
            piece = board_lines[row][col]
            if piece == 'Q':
                return True
            elif piece != '.' and piece != ' ':
                break  # Path blocked by another piece
            row, col = row + dr, col + dc
    return False

def checkmate(board):
    """Main function to check if King is in check"""
    try:
        # Handle empty or invalid input
        if not board or not board.strip():
            print("Fail")
            return
        
        lines = board.strip().split('\n')
        
        # Check if board is square and valid
        if not lines:
            print("Fail")
            return
            
        board_size = len(lines)
        for line in lines:
            if len(line) != board_size:
                print("Fail")
                return
        
        # Find the King
        king_pos = find_king(board)
        if not king_pos:
            print("Fail")
            return
        
        king_row, king_col = king_pos
        
        # Check all possible attacks
        if (check_pawn_attack(king_row, king_col, lines) or
            check_rook_attack(king_row, king_col, lines) or
            check_bishop_attack(king_row, king_col, lines) or
            check_queen_attack(king_row, king_col, lines)):
            print("Success")
        else:
            print("Fail")
            
    except Exception:
        print("Fail")