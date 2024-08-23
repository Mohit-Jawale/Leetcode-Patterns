class Solution:
    def maximumSwap(self, num: int) -> int:

        s = (str(num))
        numsList = []
        for i in s:
            numsList.append(i)
    
        sortedList = sorted(numsList,reverse=True)
        

        for index,value in enumerate(numsList):

            if value == sortedList[index]:
                continue
            else:
                swapIndex = "".join(numsList[index:]).rfind(str(sortedList[index]))
         
                numsList[index],numsList[swapIndex+index] = numsList[swapIndex+index],numsList[index]
                return int("".join(numsList))
        
        
        return int("".join(numsList))
