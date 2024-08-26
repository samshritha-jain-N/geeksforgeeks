#User function Template for python3

class Solution:
	def countOddEven(self, arr):
	    a=[0,0]
		count=0
		cnt1=0
		for i in arr:
		    if i%2==0:
		        count+=1
		    else:
		        cnt1+=1
        a[0]=cnt1
        a[1]=count
        return a
		        
		        


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    # Testcase input
    testcase = int(input())

    for _ in range(testcase):

        arr = list(map(int, input().split()))

        # Creating an object of the Solution class
        ob = Solution()

        # Calling the function to count even and odd
        res = ob.countOddEven(arr)

        # Printing the result
        print(*res)

# } Driver Code Ends