import sys
# I assume that a "one-to-one character mapping" implies
# string s1 can be transformed into string s2 by the direct substition of the
# characters in s1 with their corresponding character in s2
# (Each unique character in s1 can only be assosiated to a single character in s2)
# I am also assuming the two string must be of the same length, based on the provivded examples
# For examples such as where s1 is aaabc and s2 is deeef this solution will return False
# because I am working under the assumption that the order of chatacters must be maintained.
def evaluate(s1,s2):
    char_map = {}
    if len(s1) != len(s2):
        return False
    for i in range(0,len(s1)):
        if s1[i] not in char_map.keys():
            char_map[s1[i]] = s2[i]
        elif char_map[s1[i]] != s2[i]:
            return False
        else:
            pass
    return True

# I convert the output to a string and then print in lowercase so the output
# matches the example provided
print(str(evaluate(sys.argv[1],sys.argv[2])).lower())
