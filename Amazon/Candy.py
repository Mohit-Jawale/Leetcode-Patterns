class Solution:
    def candy(self, ratings: List[int]) -> int:

        ## 3 children
        ### rating [1,0,2]

        ### [1,1,1] this is first condition or min- >(children)
        ### [2,1,2] - > 5
        ### if they have same rating its fine to have less candies byu more than one
       #### [1,2,5,5,10,9,8,100].   stack []
       ###  [1,2,3,1,3,2,1,2]
       ### stack,greedy.-> o(N) o(N)
       
       ### monotonic decreasing
        # [10,9]
        # stack = []

        # ans = [1]*len(ratings)

        # for index,rate in enumerate(ratings):

        #     # if index!=0 and ratings[index-1]==ratings[index]:
        #     #     continue
        #     ##neighbour is grt
        #     if index<len(ratings)-1 and not stack and ratings[index]<ratings[index+1]:
        #         ans[index+1]= ans[index]+1
        #     elif index<len(ratings)-1 and not stack and ratings[index]==ratings[index+1]:
        #         continue
        #     elif index<len(ratings)-1 and ratings[index]>ratings[index+1]:
        #         stack.append((rate,index))
        #     else:
        #         stack.append((rate,index))
        #         count = 1
        #         while stack:
        #             r,idx = stack.pop()
        #             ans[idx] = count
        #             count+=1
                
        #         if ans[idx-1]>ans[idx]:
        #             ans[idx]= ans[idx-1]+1
                
        
        # if ratings[len(ratings)-1]>ratings[len(ratings)-2]:
        #     ans[len(ratings)-1] = ans[len(ratings)-2]+1
        # print(ans)
        # return sum(ans)

        sum = 0
        n = len(ratings)
        left2right = [1] * n
        right2left = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                left2right[i] = left2right[i - 1] + 1
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                right2left[i] = right2left[i + 1] + 1
        for i in range(n):
            sum += max(left2right[i], right2left[i])
        return sum
                
            


            
            


       
        

        
