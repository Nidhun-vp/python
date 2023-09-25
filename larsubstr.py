class Solution:
    def lengthofLongestSubstring(self,s:str)->int:
        if len(s)==0:
            return 0
        map={}
        max_length=start=0
        for i in range(len(s)):
            if s[i] in map and start<=map[s[i]]:
                start=map[s[i]]+1
            else:
                max_length=max(max_length,i-start+1)
            map[s[i]]=i
            return(max_length)        
 #Create an instance of the Solution class
solution = Solution()        
# Call the lengthofLongestSubstring method on the instance
input_string = "abcabcbb"  # You can change this input string
result = solution.lengthofLongestSubstring(input_string)
# Print the result
print("Length of the longest substring without repeating characters:", result)