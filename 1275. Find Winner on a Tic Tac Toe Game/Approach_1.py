class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        grid=[[""]*3 for _ in range(3)] 
        for i in range(0,len(moves),2):
            grid[moves[i][0]][moves[i][1]]="x"
            for j in range(1,len(moves),2):
                grid[moves[j][0]][moves[j][1]]="o"
        if grid[0]==["x","x","x"] or grid[1]==["x","x","x"] or grid[2]==["x","x","x"] or grid[0][0]==grid[1][1]==grid[2][2]=="x" or grid[0][2]==grid[1][1]==grid[2][0]=="x":
                return "A"
        if grid[0]==["o","o","o"] or grid[1]==["o","o","o"] or grid[2]==["o","o","o"] or grid[0][0]==grid[1][1]==grid[2][2]=="o" or grid[0][2]==grid[1][1]==grid[2][0]=="o":
                return "B"
        for i in range(3):
            if grid[0][i]==grid[1][i]==grid[2][i]=="x":
                return "A"
            if grid[0][i]==grid[1][i]==grid[2][i]=="o":
                return "B"
        if len(moves)==9:
            return "Draw"
        return "Pending"
