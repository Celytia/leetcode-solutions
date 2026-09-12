class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates)==2:
            return True
        dx=coordinates[1][0]-coordinates[0][0]
        dy=coordinates[1][1]-coordinates[0][1]
        for i in range(2,len(coordinates)):
            if (coordinates[i][1]-coordinates[0][1])*dx!=(coordinates[i][0]-coordinates[0][0])*dy:
                return False
        return True