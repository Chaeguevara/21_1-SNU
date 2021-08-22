class SolutionP1(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        result = False
        
        #Stack
        stk = []

        pair ={
            "}":"{",
            "]":"[",
            ")":"("
            }

        # Get top item of stack and compare with input
        for c in s:
            print(c)
            try:
                comp = pair[c]
                top = stk.pop()
                if top != comp:
                    return result 
            except KeyError:
                stk.append(c)
        
        if (len(stk) > 0):
            return result
        result = True
        return result



# s = "([)]"
# # s.replace('"',"")
# print(s)

# print(SolutionP1.isValid(SolutionP1,s))

class SolutionP2(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        """
        1-D CNN + Greedy
        """
        calcDic = {}
        count = 1
        listLength = len(s)
        if listLength == 1:
            return s
        for i in range(listLength-1,0,-1):
            for j in range(count):
                subStr = s[j:listLength-count+1+j]
                # print(subStr,i)
                #Dynamic 
                try:
                    calcDic[subStr] += 1
                    pass
                except KeyError:
                    calcDic[subStr]=0
                # print(calcDic)
                if self.isPan(self,subStr):
                    return subStr
            count += 1

        return s[0]

    def isPan(self,subStr):
        subLen = len(subStr)
        if subLen == 0:
            return True
        # Odd even at once
        for i in range(int(subLen/2)):
            if (subStr[i]!=subStr[subLen-1-i]):
                return False

        return True

pr = "geeksforrofskeeg"
# print(pr[0:3])
print(SolutionP2.longestPalindrome(SolutionP2,pr))