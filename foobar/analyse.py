import sys
import string
from collections import defaultdict

import matplotlib.mlab as mlab
import matplotlib.pyplot as plt


KEEP_CHARS = set(string.ascii_letters + string.digits + "' ")

def main():
    counts = defaultdict(int)

    for line in sys.stdin:
        line = "".join([(c.lower() if c in KEEP_CHARS else ' ') for c in line])
        words = line.split()

        for word in words:
            counts[word] += 1

    sorted_words = []
    sorted_counts = []
    for word, count in sorted(counts.items(), key=lambda x: x[1], reverse=True):
        # could use itertools.takewhile here
        if count < 2:
            break
        sorted_words.append(word)
        sorted_counts.append(count)

    # the histogram of the data
    plt.barh(sorted_words, sorted_counts, 1, color='g')
    plt.xlabel('Frequency')
    plt.ylabel('Word')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
