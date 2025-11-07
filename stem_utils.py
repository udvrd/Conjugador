def apply_stem_shift(stem, from_char, to_char, positions):
    def shift(s):
        index = s.rfind(from_char)
        return s[:index] + to_char + s[index + 1:] if index != -1 else s

    return [shift(stem) if i in positions else stem for i in range(6)]
