class Solution:
    def validIPAddress(self, queryIP: str) -> str:

        if '.' in queryIP :
            queryIPLIST = queryIP.split('.')

            if len(queryIPLIST)!=4:
                return "Neither"
            
            for num in queryIPLIST:

                if not num.isnumeric():
                    return "Neither"
                if not (len(str(int(num)))== len(num)):
                    return "Neither"
                if not (int(num)>=0 and int(num)<=255):
                    return "Neither"

            return "IPv4"

        elif ':' in queryIP:
            queryIPLIST = queryIP.split(':')

            if len(queryIPLIST)!=8:
                return "Neither"

            for hex_num in queryIPLIST:
             
                if not (len(hex_num)>=1 and len(hex_num)<=4):
                    return "Neither"

                for num in hex_num:
                    
                    if not ((num.isnumeric() or (ord(num)-ord('a')>=0 and ord(num)-ord('a')<= ord('f')-ord('a'))) or
                    ((ord(num)-ord('A')>=0 and ord(num)-ord('A')<= ord('F')-ord('A')))):
                        return "Neither"
                
            return "IPv6"


        return "Neither"
