#User function Template for python3


class Solution:
    def findMissing(self,  a, b, n):
        a.sort()
        b.sort()
        for i in a:
            if i in b:
                b.remove(i)
            else:
                return i
                
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.findMissing(a, b, n))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends