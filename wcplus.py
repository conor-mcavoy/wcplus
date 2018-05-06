# Author Conor McAvoy
# 4 May 2018

import argparse


def main():
    parser = argparse.ArgumentParser(description="Analyze the text of a file.")
    parser.add_argument("filename", nargs="?",
                        help="name of the file to be analyzed")
    parser.add_argument("--char-hist", action="store_true",
                        help="show the character frequency histogram")
    parser.add_argument("--word-hist", action="store_true",
                        help="show the word frequency histogram")
    parser.add_argument("--hist-scale", default=20, type=int,
                        help="max length of a line in a histogram (default 20)")
    arguments = parser.parse_args()
    filename = arguments.filename

    char_hist = arguments.char_hist
    word_hist = arguments.word_hist
    hist_scale = arguments.hist_scale
    hist_sym = "*"

    char_freqs = {}
    word_freqs = {}
    char_count = 0
    word_count = 0
    line_count = 0

    with open(filename, "r") as f:
        for line in f:
            line_count += 1
            for char in line:
                char_count += 1
                if char in char_freqs:
                    char_freqs[char] += 1
                elif ord(char) > 32:
                    char_freqs[char] = 1

            for word in line.split():
                word_count += 1
                if word in word_freqs:
                    word_freqs[word] += 1
                else:
                    word_freqs[word] = 1

    print("{} {} {}".format(char_count, word_count, line_count))
    
    if char_hist:
        max_freq = max(char_freqs.values())
        for char in sorted(char_freqs):
            if char_freqs[char] > 0:
                rel_freq = round(char_freqs[char] * hist_scale / max_freq)
                print("{}: {:{sym}<{amount}}".format(char, "", sym=hist_sym,
                                                     amount=rel_freq))

    if word_hist:
        max_freq = max(word_freqs.values())
        max_len = max(map(len, word_freqs.keys()))
        for word in sorted(word_freqs):
            if word_freqs[word] > 0:
                rel_freq = round(word_freqs[word] * hist_scale / max_freq)
                print("{:<{pad}}: {:{sym}<{amount}}".format(word, "",
                                                           pad=max_len,
                                                           sym=hist_sym,
                                                           amount=rel_freq))
                

if __name__ == "__main__":
    main()
