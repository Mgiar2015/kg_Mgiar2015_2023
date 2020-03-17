#The definition of a "one-to-one character mapping" is somewhat unclear.
#I am assuming this assignment does not allow for the asking of questions,
#therefore for my solution I assume that a "one-to-one character mapping" implies
# String s1 can be transformed into string s2 by the direct substition of the
# characters in s1 with their corresponding character in s2
def evaluate(s1,s2):
    char_map = {}
    if len(s1) != len(s2):
        return False
    for i in range(0,len(s1)):
        if s1[i] not in char_map:
            char_map[s1[i]] = s2[i]
        elif char_map[s1[i]] != s2[i]:
            return False
        else:
            pass
    return True

print(evaluate("abbb","cdcd"))
