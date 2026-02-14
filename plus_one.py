class Solution(object):
    def plusOne(self, digits):

        num=0
        for i in digits:
            num = (num*10)+ int(i)
        num=num+1
        r = list(map(int, str(num)))
        return r