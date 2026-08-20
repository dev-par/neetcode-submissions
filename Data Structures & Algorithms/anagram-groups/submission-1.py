from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # what exactly is an anagram
        # same characters, same frequency
        # how can we get a common identifier 
        # we need to maintain a list of all original words with the same characters
        # key : value pair
        # sort each word, look for the sorted key in the map, and append the orignal word to the value
        # default dict of list 
        result = []
        ana_list = defaultdict(list)
        for word in strs:
            # convert the frequency into an array of size 26
            count = [0] * 26
            for c in word:
                count[ord(c) - ord('a')] += 1
            ana_list[tuple(count)].append(word)
        
        return list(ana_list.values())
