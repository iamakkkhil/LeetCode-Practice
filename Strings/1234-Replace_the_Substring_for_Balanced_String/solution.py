class Solution:
    
    def check_satisfy(self, s, p1, p2, balanced_count):
        count_chars = {"Q":0, "W":0, "E":0, "R":0}
        new_s = s[:p1]+s[p2:]
        for i in new_s:
            count_chars[i] += 1
            if count_chars[i] > balanced_count:
                return False
        return True


    def balancedString(self, s: str) -> int:
        balanced_count = len(s)/4 
        substring_count = len(s)

        p1,p2 = 0,0

        while(p2>=p1 and p2<=len(s)):
            if self.check_satisfy(s, p1, p2, balanced_count):
                p1 += 1
                if substring_count > (p2-p1+1):
                    substring_count = p2-p1+1
            else:
                p2+=1
        
        return substring_count