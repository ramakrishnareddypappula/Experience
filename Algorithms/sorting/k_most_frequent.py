

# {
# "k": 4,
# "words": ["car", "bus", "taxi", "car", "driver", "candy", "race", "car", "driver", "fare", "taxi"]

from collections import Counter
def out(k, words):
    res = list()

    # count per word
    word_dict = Counter(words)

    # Transform to freq with list of words
    freq_dict = dict()
    for word, freq in word_dict.items():
        if freq in freq_dict:
            freq_dict[freq].append(word)

        else:
            freq_dict[freq] = [word]
    print(freq_dict)
    freq_dict1 = dict(sorted(freq_dict.items(), reverse=True))
    print(freq_dict1)


print(out(4, ["car", "bus", "taxi", "car", "driver", "candy", "race", "car", "driver", "fare", "taxi"]))