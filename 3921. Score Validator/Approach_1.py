class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:
        score=counter=0
        i=0
        while i<len(events):
            if "0"<=events[i]<="6":
                score+=int(events[i])
            if events[i]=="W":
                counter+=1
                if counter==10:
                    break
            if events[i]=="WD" or events[i]=="NB":
                score+=1 
            i+=1
        return [score,counter]