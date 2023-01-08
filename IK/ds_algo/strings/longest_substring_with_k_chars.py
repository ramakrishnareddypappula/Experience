

# This uses SLIDING WINDOW PROTOCOL.
#
# Intuition:
# - Use dictionary and always keep length = k
# - keep left and right at the start position
# - Initially add s[i] as key and its count as value
# - if len(d) > k , then remove the start element in dictionary and increment the start.
# - if len(d) == k, calc maxlen with right - left + 1


# Time complexity: O(n)
# Auxiliary space: O(1)
# space complexity: O(n)
def get_longest_substring_length_with_exactly_k_distinct_chars(s, k):
    """
    Args:
     s(str)
    Returns:
     int32
    """
    # Write your code here.
    # return 0
    d = {}
    left = 0
    right = 0
    max_length = 0
    while right < len(s):
        if s[right] in d:
            d[s[right]] += 1
        else:
            d[s[right]] = 1
        while len(d) > k:
            d[s[left]] -= 1
            if d[s[left]] == 0:
                d.pop(s[left])
            left += 1
        if len(d) == k:
            max_length = max(max_length, right - left + 1)
        right += 1
    return max_length

print(get_longest_substring_length_with_exactly_k_distinct_chars("ecebaaaaca", 2))
print(get_longest_substring_length_with_exactly_k_distinct_chars("aabacccac", 2))
print(get_longest_substring_length_with_exactly_k_distinct_chars("aabacccac", 1))