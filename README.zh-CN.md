# GPT From Scratch——基于 PyTorch 的语言模型动手学习项目

[English](README.md) | **中文**

> 一个跟随这个 [YouTube 教程](https://www.youtube.com/watch?v=UU1WVnMk4E8&t=18584s) 的学习仓库：
> 使用 PyTorch 从 Bigram 基线开始，逐步实现 GPT 风格的 Transformer 语言模型。

## 内容

- `GPT_V1.ipynb`：GPT 模型的原始实现与训练流程。
- `GPT_V1_Fixed.ipynb`：修正后的 GPT 实现。
- `bigram.ipynb`：从 Bigram 语言模型开始的练习。
- `torch_example.ipynb`：PyTorch 基础实验。
- `scripts/`：OpenWebText 语料处理和创建数据样本的辅助脚本。
- `vocab.txt` 和 `wizard_of_oz.txt`：字符词表与示例文本。
- `data_samples/`：从 `wizard_of_oz.txt` 中截取的快速训练与验证文本样本。

## 未包含的本地文件

完整训练和验证语料（合计约 41 GiB）保留在本地。模型权重（例如 `model-01.pkl`）同样未包含
在此仓库中。这些产物过大，不适合放入普通的公开源码仓库。虚拟环境、Jupyter 检查点和缓存
也不会提交。

## 运行

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
jupyter notebook
```

打开 `GPT_V1_Fixed.ipynb` 可查看主要模型实现。它默认使用 `data_samples/train_split.txt` 和
`data_samples/val_split.txt`，因此克隆后即可进行小规模运行。这些样本仅用于演示，不适合
完整训练。

## 使用本地完整语料

如果项目根目录中已有完整的 `train_split.txt` 和 `val_split.txt`，可在启动 Jupyter 前将数据
目录指向项目根目录：

```powershell
$env:GPT_DATA_DIR = "."
jupyter notebook
```

## 从 tar 语料包创建样本

`scripts/create_data_samples.py` 可从本地 tar 格式的语料包中提取小型 UTF-8 文本样本。脚本
必须接收源语料包和目标文件路径，`--max-bytes` 参数可选。

```powershell
python scripts/create_data_samples.py .\path\to\corpus.tar .\data_samples\train_split.txt --max-bytes 524288
```
