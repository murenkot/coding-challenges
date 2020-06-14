import string


class Solution:
    def longestPalindrome(self, s: str) -> str:
        # alphabet = list(string.ascii_lowercase)
        # alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
        #             'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        unique_char = []
        for n in s:
            if n not in unique_char:
                unique_char.append(n)
        palindrome = ''
        if len(s) > 1:
            for character in unique_char:
                if character in s:
                    num_of_char = len(s.split(character)) - 1
                    if num_of_char > 1:
                        indexes = [i for i, e in enumerate(
                            s) if e == character]
                        for i in range(0, len(indexes)-1):
                            for y in range(1, len(indexes)):
                                word = s[indexes[i]:indexes[y]+1]
                                # check if the word is palindrom
                                revers_word = word[::-1]
                                if word == revers_word:
                                    # check if palindrom is longer then existing
                                    if len(word) > len(palindrome):
                                        palindrome = word

            if palindrome == '':
                return s[0]
            else:
                return palindrome
        else:
            return s


x = Solution()
print(x.longestPalindrome("222020221"))
