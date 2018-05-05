# Author Conor McAvoy
# 4 May 2018

import argparse


def main():
    parser = argparse.ArgumentParser(description="Analyze the text of a file.")
    parser.add_argument("filename", nargs="?",
                        help="Name of the file to be analyzed")
    parser.add_argument("--hist-scale", default=20, type=int,
                        help="Max length of a line in the histogram.")
    arguments = parser.parse_args()
    filename = arguments.filename

    hist_scale = arguments.hist_scale
    hist_sym = "*"
    char_freqs = {chr(val): 0 for val in range(32, 127)}
    char_count = 0

    with open(filename, "r") as f:
        for line in f:
            for char in line:
                char_count += 1
                if char in char_freqs:
                    char_freqs[char] += 1

    max_freq = max(char_freqs.values())
    char_rel_freqs = {}
    for char in char_freqs:
        if char_freqs[char] > 0:
            char_rel_freqs[char] = round(char_freqs[char] * hist_scale
                                         / max_freq)

    for char, rel_freq in char_rel_freqs.items():
        print("{}: {:{sym}<{amount}}".format(char, "", sym=hist_sym,
                                             amount=rel_freq))
        

if __name__ == "__main__":
    main()
