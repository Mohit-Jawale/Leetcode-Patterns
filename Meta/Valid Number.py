class Solution:
    def isNumber(self, s: str) -> bool:

        if len(s)==0:
                return False

        def checknum(s,isdecimal):

            if len(s)==0:
                return False

            freq = collections.defaultdict(int)

            for i in range(len(s)):
                freq[s[i]] +=1
            
            isnumeric = False
         
    
            for key,value in freq.items():

                if key!=['e','E'] and key.isalpha():
                    return False
                elif key not in ['-','.','+'] and not key.isalnum():
                    return False

                elif key.isdigit():
                    isnumeric = True

                elif key in ['-','.','+'] and value>1:
                    return False
            
            if '-' in freq: 
          
                if s[0]=='-' and isnumeric:
                    pass
                else:
                    return False
              
            if '+' in freq : 
                if s[0]=='+' and isnumeric:
                    pass
                else:
                    return False
                     
            if '.' in freq and ('-' in freq or '+' in freq): 

                if (s[0]=='-' or s[0]=='+') and isnumeric:
                    pass
                else:
                    return False
            if ('.' in freq or '+' in freq or '-' in freq ) and not isnumeric:
                return False
            
            if isdecimal:
                if ('.' in freq and isnumeric):
                    return False
            return True
            

        nums = re.split(r'[eE]',s)
        print(nums)

        if len(nums)>2:
            return False
        if len(nums)==2:
            return checknum(nums[0],False) and checknum(nums[1],True)
        if len(nums)==1:
            return checknum(nums[0],False)
            


        
        

        
        
