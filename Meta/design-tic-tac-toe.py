class TicTacToe:

    def __init__(self, n: int):

        self.n = n

        self.h_1,self.h_2 = collections.defaultdict(set),collections.defaultdict(set)
        self.v_1,self.v_2 = collections.defaultdict(set),collections.defaultdict(set)
        self.diagonal_1,self.diagonal_2 = set(),set()
        self.anti_diagonal_1,self.anti_diagonal_2 = set(),set()
        

    def detect_win(self,r,c,player):

        if player == 1:
            if len(self.h_1[r]) == self.n:
                return 1
            elif len(self.v_1[c])==self.n:
                return 1
            elif len(self.diagonal_1)==self.n:
                return 1
            elif len(self.anti_diagonal_1)==self.n:
                return  1
            
        if player == 2:
            if len(self.h_2[r]) == self.n:
                return 2
            elif len(self.v_2[c])==self.n:
                return 2
            elif len(self.diagonal_2)==self.n:
                return 2
            elif len(self.anti_diagonal_2)==self.n:
                return 2

        return 0


        

    def move(self, row: int, col: int, player: int) -> int:

        if player == 1:

            self.h_1[row].add((row,col))
            self.v_1[col].add((row,col))
            if row==col:
                self.diagonal_1.add((row,col))
            if row+col == self.n-1:
                self.anti_diagonal_1.add((row,col))

            return self.detect_win(row,col,player)

        
        elif player == 2:

            self.h_2[row].add((row,col))
            self.v_2[col].add((row,col))
            if row==col:
                self.diagonal_2.add((row,col))
            if row+col == self.n-1:
                self.anti_diagonal_2.add((row,col))

            return self.detect_win(row,col,player)



        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
