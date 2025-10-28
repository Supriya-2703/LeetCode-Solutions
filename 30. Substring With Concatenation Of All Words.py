from collections import Counter

class Solution:
    def findSubstring(self, s, words):
        if not s or not words:
            return []

        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        word_count = Counter(words)
        
        result = []

        for i in range(len(s) - total_len + 1):
            seen = []
            for j in range(0, total_len, word_len):
                word = s[i+j:i+j+word_len]
                seen.append(word)
            if Counter(seen) == word_count:
                result.append(i)
        
        return result
