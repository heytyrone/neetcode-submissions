class Solution:

    def encode(self, strs: List[str]) -> str:
        combine_str = ""
        for item in strs:
            combine_str = combine_str + str(len(item)) + "#" + item
        return combine_str
    def decode(self, s: str) -> List[str]:
        break_list = []
        i = 0
        prior_i = 0
        while i < len(s):
            if s[i] == "#":
                length = int(s[prior_i:i])    # Length of coming string
                break_list.append(s[i+1:i+length+1])
                i = i+length
                prior_i = i+1
            i+=1
        return break_list

