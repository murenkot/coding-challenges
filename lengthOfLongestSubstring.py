class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_sub = ''
        current_sub = ''
        for i in s:
            if (i not in current_sub):
                current_sub += i
            else:
                # it means that substring brakes
                # compare current_sub to longest_sub
                if len(current_sub) > len(longest_sub):
                    # we need to move current_sub to longest_sub
                    longest_sub = current_sub
                current_sub = current_sub.split(i)[1] + i
        if (len(current_sub) > len(longest_sub)):
            return len(current_sub)
        return len(longest_sub)


x = Solution()
print(x.lengthOfLongestSubstring("dvdf"))
