class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_dict = defaultdict(list)
        for string in strs:
            freq_dict["".join(sorted(string))].append(string)
            # Set dict ID to sorted version of string, add string to list
        return list(freq_dict.values())

