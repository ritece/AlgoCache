class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        pre = [1]*n
        post = [1]*n
        
        for i in xrange(1,n):
            pre[i] = pre[i-1]*nums[i-1]
        for i in xrange(n-2,-1,-1):
            post[i] = post[i+1]*nums[i+1]
        
        output = [1]*n
        
        for i in xrange(n):
            output[i] = pre[i]*post[i]
        
        return output
        
        
