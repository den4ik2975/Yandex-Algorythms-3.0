k = int(input())
s = input()


def max_beauty_string(s: str, k: int) -> int:
    freq = {}
    left, max_freq, max_len = 0, 0, 0

    for right, char in enumerate(s):
        freq[char] = freq.get(char, 0) + 1
        max_freq = max(max_freq, freq[char])

        if right - left + 1 - max_freq > k:
            freq[s[left]] -= 1
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len

print(max_beauty_string(s, k))