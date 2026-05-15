class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = self.freq_dict(s)
        t_dict = self.freq_dict(t)
        return s_dict == t_dict

    def freq_dict(self, s: str) -> dict:
        s_dict = {}
        for letter in s:
            if s_dict.get(letter) == None:
                s_dict[letter] = 1
            else:
                s_dict[letter] +=1
        return s_dict
            
