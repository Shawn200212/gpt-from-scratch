[English](README.md) | [简体中文](README.zh-CN.md)

<a id="gpt-from-scratch--a-hands-on-pytorch-language-model-study--gpt-from-scratch基于-pytorch-的语言模型动手学习项目"></a>
<a id="gpt-from-scratch--a-hands-on-pytorch-language-model-study"></a>
<a id="gpt-from-scratch基于-pytorch-的语言模型动手学习项目"></a>

# GPT From Scratch — a hands-on PyTorch language-model study

> A learning repository that follows this [YouTube tutorial](https://www.youtube.com/watch?v=UU1WVnMk4E8&t=18584s)
> to build language models step by step, from a Bigram baseline to a GPT-style Transformer in
> PyTorch.

<a id="contents--内容"></a>
<a id="contents"></a>
<a id="内容"></a>

## Contents

- `GPT_V1.ipynb`: the original GPT implementation and training workflow.
- `GPT_V1_Fixed.ipynb`: the corrected GPT implementation.
- `bigram.ipynb`: exercises beginning with a Bigram language model.
- `torch_example.ipynb`: introductory PyTorch experiments.
- `scripts/`: helper scripts for processing the OpenWebText corpus and creating data samples.
- `vocab.txt` and `wizard_of_oz.txt`: a character vocabulary and example text.
- `data_samples/`: small training and validation samples extracted from `wizard_of_oz.txt` for quick runs.

<a id="local-files-not-included--未包含的本地文件"></a>
<a id="local-files-not-included"></a>
<a id="未包含的本地文件"></a>

## Local files not included

The full training and validation corpora (about 41 GiB in total) remain local. Model weights such as
`model-01.pkl` are also not included. These artifacts are too large for a normal public source
repository. Virtual environments, Jupyter checkpoints, and caches are excluded as well.

<a id="run--运行"></a>
<a id="run"></a>
<a id="运行"></a>

## Run

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
jupyter notebook
```

Open `GPT_V1_Fixed.ipynb` to view the main model implementation. By default, it uses
`data_samples/train_split.txt` and `data_samples/val_split.txt`, so a small-scale run is available
immediately after cloning. These samples are intended for demonstration only, not full training.

<a id="use-the-full-local-corpus--使用本地完整语料"></a>
<a id="use-the-full-local-corpus"></a>
<a id="使用本地完整语料"></a>

## Use the full local corpus

If full `train_split.txt` and `val_split.txt` files are available in the project root, point the data
directory there before starting Jupyter:

```powershell
$env:GPT_DATA_DIR = "."
jupyter notebook
```

<a id="create-a-sample-from-a-tar-archive--从-tar-语料包创建样本"></a>
<a id="create-a-sample-from-a-tar-archive"></a>
<a id="从-tar-语料包创建样本"></a>

## Create a sample from a tar archive

`scripts/create_data_samples.py` extracts a small UTF-8 text sample from a local tar-format corpus
archive. It requires a source archive and destination file; `--max-bytes` is optional.

```powershell
python scripts/create_data_samples.py .\path\to\corpus.tar .\data_samples\train_split.txt --max-bytes 524288
```
