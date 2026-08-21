class Solution:
    # abc 12 331
    # 3,abc2,12
    # 3,abc3,3,2
    # prepend each string with it's length and a chosen delimiter

    def encode(self, strs: List[str]) -> str:
        # build new lists and join them
        delimiter = ";"
        new_list = []
        for string in strs:
            length = str(len(string))
            new_string = length + delimiter + string
            new_list.append(new_string)
        return "".join(new_list)


    def decode(self, s: str) -> List[str]:
        # we need to parse the string 
    #start by calculating the length, moving one, then moving a factor of length, repeat
        # while loop because of funny jumps
        # 3,abc3,3,2
        # i

        # length = i
        # move i forward two
        # substring from i to i + length - 1

        # ["we","say",":","yes","!@#$%^&*()"]
        # 2;we3;say1;:3;yes10;!@#$%^&*()
        #               i
        # length = 3

        res = []
        i = 0
        while i < len(s):
            length = ""
            while s[i].isnumeric():
                length += s[i]
                i += 1
            length = int(length)
            i += 1
            res.append(s[i:i + length])
            i += length
        return res