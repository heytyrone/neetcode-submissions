class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_dict = defaultdict(list)
        for string in strs:
            count_array = [0]*26
            for letter in string:
                count_array[ord(letter)-ord("a")] +=1
            result_dict[tuple(count_array)].append(string)
        return list(result_dict.values())
