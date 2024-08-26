class Solution:
    def thirdLargest(self,t):
        if len(t)<3:
            return -1
        else:
            s=sorted(t)
            s.reverse()
            return s[2]






#{ 
 # Driver Code Starts
# Your code goes here
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        arr = list(map(int, input().strip().split()))
        print(Solution().thirdLargest(arr))

# } Driver Code Ends