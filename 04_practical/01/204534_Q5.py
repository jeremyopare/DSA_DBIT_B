from typing import Dict

def count_char_frequencies(text: str) -> Dict[str, int]:
    frequencies: Dict[str, int] = {}
    for char in text:
        if char in frequencies:
            frequencies[char] += 1
        else:
            frequencies[char] = 1
    return frequencies

input_string = "data structures and algorithms"
result = count_char_frequencies(input_string)
print(result)