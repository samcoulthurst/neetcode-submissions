class Solution:
    def strToHash(self, s):
        hash = {}
        for letter in s:
            hash[letter] = hash.get(letter,0) + 1

        return hash

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        else:
            biggest = s2
            smallest = s1
        len_smallest = len(smallest)
        len_biggest = len(biggest)
        
        for i in range(len_biggest-len_smallest+1):
            window = biggest[i:i+len_smallest]
            if self.strToHash(window) == self.strToHash(smallest):
                return True
        return False
