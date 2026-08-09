"""Create a sampled OpenWebText training corpus from local .xz source files."""

import concurrent.futures
import lzma
import os
import random

from tqdm import tqdm


def process_file(args):
    directory, filename = args
    file_path = os.path.join(directory, filename)
    with lzma.open(file_path, "rt", encoding="utf-8") as infile:
        return infile.read()


def xz_files_in_dir(directory):
    return [
        filename
        for filename in os.listdir(directory)
        if filename.endswith(".xz") and os.path.isfile(os.path.join(directory, filename))
    ]


def process_files_in_parallel(files, folder_path, output_file):
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
        args = [(folder_path, filename) for filename in files]
        vocabulary = set()
        with open(output_file, "w", encoding="utf-8") as output:
            for text in tqdm(executor.map(process_file, args), total=len(files)):
                output.write(text)
                vocabulary.update(text)
    return vocabulary


def main(folder_path="openwebtext", sample_rate=0.01):
    files = xz_files_in_dir(folder_path)
    split_index = int(len(files) * 0.9)
    train_files, val_files = files[:split_index], files[split_index:]

    train_sample = random.sample(train_files, max(1, int(len(train_files) * sample_rate)))
    val_sample = random.sample(val_files, max(1, int(len(val_files) * sample_rate)))
    train_output, val_output = "output_train.txt", "output_val.txt"

    vocab = process_files_in_parallel(train_sample, folder_path, train_output)
    vocab.update(process_files_in_parallel(val_sample, folder_path, val_output))
    with open("vocab.txt", "w", encoding="utf-8") as vfile:
        for char in sorted(vocab):
            vfile.write(char + "\n")


if __name__ == "__main__":
    main()
