class Solution:
    def fullJustify(self, words, maxWidth):
        res = []
        i = 0
        n = len(words)

        while i < n:
            line_len = len(words[i])
            j = i + 1

            while j < n and line_len + 1 + len(words[j]) <= maxWidth:
                line_len += 1 + len(words[j])
                j += 1

            num_words = j - i

            if j == n or num_words == 1:
                line = " ".join(words[i:j])
                line += " " * (maxWidth - len(line))
                res.append(line)
            else:
                total_chars = sum(len(w) for w in words[i:j])
                total_spaces = maxWidth - total_chars
                gaps = num_words - 1

                space_per_gap = total_spaces // gaps
                extra = total_spaces % gaps

                line = ""
                for k in range(i, j - 1):
                    line += words[k]
                    spaces = space_per_gap + (1 if extra > 0 else 0)
                    line += " " * spaces
                    if extra > 0:
                        extra -= 1
                line += words[j - 1]  
                res.append(line)

            i = j

        return res
