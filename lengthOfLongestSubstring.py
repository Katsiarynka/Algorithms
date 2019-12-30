
def length_of_longest_substring(s: str) -> str:
    longestSubstr = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if is_uniq_substr(s, i, j):
                longestSubstr = max(longestSubstr, j-i)
            else: 
                break
    return longestSubstr

def is_uniq_substr(s: str, start: int, end: int) -> bool:
    characters = set()
    for i in range(start, end):
        if s[i] in characters:
            return False
        characters.add(s[i])
    return True


assert(length_of_longest_substring(" ") == 1)
assert(length_of_longest_substring("asdf asdf") == 5)
