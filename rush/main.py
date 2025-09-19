from checkmate import checkmate

def main():
    # Test Case 1 (Pawn attack)
    board1 = """\
R...
.K..
..P.
....\
"""
    print("Test 1 (Pawn attack):")
    checkmate(board1)
    
    # Test Case 2 (No attack)
    board2 = """\
..
.K\
"""
    print("Test 2 (No attack):")
    checkmate(board2)
    
    # Test Case 3: Queen attack
    board3 = """\
Q...
....
....
...K\
"""
    print("Test 3 (Queen attack):")
    checkmate(board3)
    
    # Test Case 4: Bishop attack
    board4 = """\
B...
....
..K.
....\
"""
    print("Test 4 (Bishop attack):")
    checkmate(board4)
    
    # Test Case 5: No attack
    board5 = """\
....
.K..
....
....\
"""
    print("Test 5 (No attack):")
    checkmate(board5)
    
    # Test Case 6: Pawn attack
    board6 = """\
....
.K..
P...
....\
"""
    print("Test 6 (Pawn attack):")
    checkmate(board6)

    board7 = """\
....
.K..
....
.R..
"""
    print("Test 7 (Rook attack):")
    checkmate(board7)

main()