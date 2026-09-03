class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # null is represented by a dot 
        # each row must contain 1-9 without duplicates
        for row in board:
            num_list = []
            # constraints say only 1-9 or .
            for item in row:
                if item.isdigit():
                    num_list.append(item)
            num_set = set(num_list)
            if len(num_list) != len(num_set):
                print("row is bad")
                return False
        

        # each column must contain 1-9 without duplicates
        for i in range(len(board[0])):
            num_list = []
            for j in range(len(board)):
                item = board[j][i]
                if item.isdigit():
                    num_list.append(item)
            num_set = set(num_list)
            if len(num_list) != len(num_set):
                print("col is bad")
                return False
                

        # each of the nine 3x3 subboxes must contain 1-9 without duplicates
        # what are the locations of each of the center boxes
        # 1, 1   1, 4.   1, 7
        # 4, 1.  4, 4.   4, 7
        # 7, 1.  7, 4.   7, 7
        
        # how can I iterate to get there

        i = 0
        j = 0
        for i in range(1, 10, 3):
            for j in range(1, 10, 3):
                # i and j are correct
                # need to search that box plus 8 others
                # create a directions array
                directions = [[-1,-1], [-1,0], [-1,1], [0,-1], [0,1], [0,0], [1,1], [1,0], [1,-1]]
                num_list = []
                for x_d, y_d in directions:
                    new_x = j + x_d
                    new_y = i + y_d
                    item = board[new_x][new_y]
                    if item.isdigit():
                        print(f"Item: {item}")
                        num_list.append(item)
                    num_set = set(num_list)
                print(num_set, num_list)
                if len(num_list) != len(num_set):
                    print("sub-box is bad")
                    return False

        # return true
        return True