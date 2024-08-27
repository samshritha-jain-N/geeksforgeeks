
class Solution:
    def longest(self, names):
        # code here
        longword=""
        for word in names:
            if len(word)>len(longword):
                longword=word
        return longword
            


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        names = input().split()
        obj = Solution()
        res = obj.longest(names)
        print(res)

# } Driver Code Ends