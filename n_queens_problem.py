def solve_n_queens(n):
    # Create an empty chessboard
    board = [[0 for _ in range(n)] for _ in range(n)]
    
    def is_valid(row, col):
        # Check if there is any queen in the same column
        for i in range(row):
            if board[i][col] == 1:
                return False
        
        # Check if there is any queen in the upper left diagonal
        i = row - 1
        j = col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 1:
                return False
            i -= 1
            j -= 1
        
        # Check if there is any queen in the upper right diagonal
        i = row - 1
        j = col + 1
        while i >= 0 and j < n:
            if board[i][j] == 1:
                return False
            i -= 1
            j += 1
        
        # If all checks passed, return True
        return True
    
    def backtrack(row):
        # If all queens are placed, print the solution
        if row == n:
            for i in range(n):
                print(board[i])
            print()
        
        # Try placing the queen in each column of the current row
        for col in range(n):
            if is_valid(row, col):
                # Place the queen
                board[row][col] = 1
                
                # Recursively backtrack to the next row
                backtrack(row+1)
                
                # Remove the queen (backtrack)
                board[row][col] = 0
    
    # Start backtracking from the first row
    backtrack(0)
solve_n_queens(8)

          
    