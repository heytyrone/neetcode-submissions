class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result_dict = defaultdict(int)
        result_list = []
        for value in nums:
            result_dict[value] +=1
        print(f"{result_dict=}")
        for value, freq in result_dict.items():
            result_list.append([freq, value])
        result_list.sort()
        final_list = []
        for pair in result_list[-k:]:
            final_list.append(pair[1])
        return final_list