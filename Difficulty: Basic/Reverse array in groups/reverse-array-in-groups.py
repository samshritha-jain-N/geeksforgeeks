#User function template for Python

class Solution:
    # Function to reverse every sub-array group of size k.
    def reverseInGroups(self, arr,k):
        n=len(arr)
        for i in range(0,n,k):
            start=i
            end=min(i+k,n)-1
            while start<end:
                arr[start],arr[end]=arr[end],arr[start]
                start+=1
                end-=1
        return arr[start],arr[end],n
        
                


#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    t = int(data[0])
    line_index = 1
    for _ in range(t):
        k = int(data[line_index])
        line_index += 1
        arr = list(map(int, data[line_index].split()))
        line_index += 1
        ob = Solution()
        ob.reverseInGroups(arr, k)
        print(" ".join(map(str, arr)))

# } Driver Code Ends