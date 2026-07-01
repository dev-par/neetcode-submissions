class Solution:
    # abcdef
    # 6abcdef
    # 123abc
    # 6123abc
    # ;123abc
    # 6;;123abc
    # how do we know where to stop reading the length? 
    # we should encode with a number and a delimiter
    # for example, 6;abc123
    def encode(self, strs: List[str]) -> str:
        joining_list = []
        for string in strs:
            joining_list.append(str(len(string)) + ";" + string)
        return "".join(joining_list)

    def decode(self, s: str) -> List[str]:
        print(s)
        res = []
        i = 0
        while i < len(s):
            length = ""
            while s[i] != ";":
                length += s[i]
                i += 1
            int_length = int(length)
            i += 1
            word = ""
            for j in range(int_length):
                word += s[i]
                i += 1
            res.append(word)
        
        return res

            

# 