class LetterCounter:
    def __init__(self, text):
        self.text = text

    def calculate_most_common(self):
        counter = {}
        most_common = None
        most_common_count = 0  # Initialize most_common_count to 0
        for char in self.text:
            if not char.isalpha():
                continue
            counter[char] = counter.get(char, 0) + 1
            if counter[char] > most_common_count:
                most_common = char
                most_common_count = counter[char]  # Update most_common_count

        if most_common is not None:
            return [most_common_count, most_common]
        else:
            return [0, ""]  # Return [0, ""] if no letters were found in the input text

counter = LetterCounter("Digital Punk")
print(counter.calculate_most_common())
# Intended output:
# [2, "i"]
