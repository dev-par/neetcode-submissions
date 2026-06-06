from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # group all anagrams into sublists
        # anagrams are the same when sorted
        # use the key as the sorted anagram and the value as a list of the anagrams
        
        hashmap = defaultdict(list)
        for word in strs:
            sorted_word = "".join(sorted(word))
            hashmap[sorted_word].append(word)

        return list(hashmap.values())