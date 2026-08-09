# GPT From Scratch

一个基于 PyTorch 的 GPT / Transformer 学习工程，跟随 [YouTube 教程](https://www.youtube.com/watch?v=UU1WVnMk4E8&t=18584s) 手工实现。

## 内容

- `GPT_V1.ipynb`：GPT 模型的原始实现与训练流程。
- `GPT_V1_Fixed.ipynb`：修正后的 GPT 实现。
- `bigram.ipynb`：从 Bigram 语言模型开始的练习。
- `torch_example.ipynb`：PyTorch 基础实验。
- `scripts/`：OpenWebText 语料处理和创建数据样本的辅助脚本。
- `vocab.txt`、`wizard_of_oz.txt`：小型词表与示例文本。
- `data_samples/`：由 `wizard_of_oz.txt` 截取的快速训练/验证文本样本。

## 未包含的本地文件

完整训练和验证语料（约 41 GiB）以及模型权重（例如 `model-01.pkl`）保留在本地，未推送到此仓库：它们超过普通 GitHub 仓库的单文件大小限制，也不适合作为公开源码仓库内容。虚拟环境、Jupyter 检查点和缓存同样不会提交。

## 运行

```powershell
python -m venv .venv
.\\.venv\\Scripts\\Activate.ps1
pip install -r requirements.txt
jupyter notebook
```

打开 `GPT_V1_Fixed.ipynb` 可查看主要模型代码。默认会使用 `data_samples/train_split.txt` 和 `data_samples/val_split.txt`，因此克隆后即可进行小规模运行；它们仅用于演示，不适合正式训练。

## 重新生成样本

如果本地保留有完整语料，可在启动 Jupyter 前将数据目录指向项目根目录：

```powershell
$env:GPT_DATA_DIR = "."
jupyter notebook
```

`scripts/create_data_samples.py` 可从本地 tar 格式的语料包中提取小型 UTF-8 文本样本。
