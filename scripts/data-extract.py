"""Build train/validation corpus files and a character vocabulary from .xz files."""

import lzma
import os

from tqdm import tqdm


def xz_files_in_dir(directory):
    return [
        filename
        for filename in os.listdir(directory)
        if filename.endswith(".xz") and os.path.isfile(os.path.join(directory, filename))
    ]


def main(folder_path="openwebtext", train_output="output_train.txt", val_output="output_val.txt"):
    files = xz_files_in_dir(folder_path)
    split_index = int(len(files) * 0.9)
    files_train, files_val = files[:split_index], files[split_index:]
    vocab = set()

    for files_for_split, output_file in ((files_train, train_output), (files_val, val_output)):
        with open(output_file, "w", encoding="utf-8") as outfile:
            for filename in tqdm(files_for_split, total=len(files_for_split)):
                filepath = os.path.join(folder_path, filename)
                with lzma.open(filepath, "rt", encoding="utf-8") as infile:
                    text = infile.read()
                outfile.write(text)
                vocab.update(text)

    with open("vocab.txt", "w", encoding="utf-8") as vfile:
        for char in sorted(vocab):
            vfile.write(char + "\n")


if __name__ == "__main__":
    main()
