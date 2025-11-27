def apply_stem_shift(stem, from_char, to_char, positions):
    def shift(s):
        index = s.rfind(from_char)
        return s[:index] + to_char + s[index + 1:] if index != -1 else s

    result = [shift(stem) if i in positions else stem for i in range(6)]

    position = stem.rfind(from_char)
    if position == 0:
        for i in [0, 1, 2, 5]:
            result[i] = "h" + result[i]

    return result
