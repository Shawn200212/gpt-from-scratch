# 在另一台电脑推送到 GitHub

本文件夹已经是一个完整的 Git 仓库，包含初始提交和全部准备公开的工程文件。复制整个文件夹时请保留隐藏的 `.git` 文件夹。

## 已包含

- GPT 模型与教学笔记本：`GPT_V1.ipynb`、`GPT_V1_Fixed.ipynb`、`bigram.ipynb`、`torch_example.ipynb`
- 数据预处理脚本、词表、示例文本与小型训练/验证样本
- `README.md`、`requirements.txt`、`.gitignore`

## 有意不包含

- 约 41 GiB 的完整训练/验证语料
- 模型权重（例如 `model-01.pkl`）
- 虚拟环境、Jupyter 检查点和缓存
- 任何密码、访问令牌或个人凭据

## 推送步骤

在另一台电脑的 PowerShell 或终端中进入本文件夹，然后执行：

```powershell
git status -sb
git remote add origin https://github.com/Shawn200212/gpt-from-scratch.git
git push -u origin main
```

请先在 GitHub 中创建一个**公开且空白**的 `gpt-from-scratch` 仓库；不要初始化 README、`.gitignore` 或 License。若使用不同的仓库名，请将上面 URL 中的仓库名相应替换。

推送完成后可在 GitHub 页面检查 `README.md`、四个 notebook、`scripts/`、`data_samples/`、`vocab.txt` 和 `wizard_of_oz.txt` 是否存在。
