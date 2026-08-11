class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            row_clean = [num for num in row if num != "."]
            if len(row_clean) != len(set(row_clean)):
                return False

        cols = list(map(list, zip(*board)))

        for col in cols:
            col_clean = [num for num in col if num != "."]
            if len(col_clean) != len(set(col_clean)):
                return False

        hashmap = {}

        for i in range(len(board)):
            for j in range(len(board[0])):
                hashmap[(i//3, j//3)] = hashmap.get((i//3, j//3), [])
                hashmap[(i//3, j//3)].append(board[i][j])   

        for subgrid in hashmap.values():
            clean_list = [num for num in subgrid if num != "."]
            if len(clean_list) != len(set(clean_list)):
                return False

        return True    