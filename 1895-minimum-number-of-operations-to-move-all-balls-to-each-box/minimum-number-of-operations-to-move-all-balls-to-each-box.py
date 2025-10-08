class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        r = []
        for i,x in enumerate(boxes):
            counto = 0
            for j,y in enumerate(boxes):
                if y == "1":
                    counto += abs(i-j)
            r.append(counto)
        return r


