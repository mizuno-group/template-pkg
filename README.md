# template-dev
パッケージ公開用テンプレート

`template-dev`を基礎とし, PyPIなどでの公開と他者による再利用を目的としたPythonパッケージ開発テンプレート。

## 特徴

  - **`pyproject.toml` による依存関係の一元管理**
  - **安全な `src` レイアウトの採用**
  - **品質を保証するための `tests/` ディレクトリを標準装備**
  - **CLI (コマンドラインインターフェース) の実装をサポート**

## ディレクトリ構成

```
.
├── notebooks/            # 利用者向けのサンプルノートブック
│   └── usage_example.ipynb
├── src/
│   └── my_project/       # パッケージのソースコード
│       ├── init.py
│       ├── cli.py        # (任意) CLIのエントリーポイント
│       └── core.py
├── tests/                # テストコード
│   └── test_module.py
├── .gitignore
├── LICENSE               # ライセンスファイル
├── pyproject.toml        # プロジェクト定義ファイル
└── README.md             # この説明書
```

## 利用手順

### 1\. リポジトリの作成

GitHub上で "Use this template" ボタンを押し, 新規リポジトリを作成する。

### 2\. 環境のセットアップ

ローカルにクローン後, 以下のコマンドを実行する。

```bash
# clone
git clone -b {branch名} {repository URL}
cd {repository名}
```
基本インストール (開発環境が整っているコンテナではこれでOK)。

```bash
# 編集可能モードでインストールすることでsrc以下の編集が即座に反映される
pip install -e "."
```

開発用ツールも含めたフルインストールの場合は以下 (詳細はtoml参照)
```bash
pip install -e ".[dev]"
```

### 3\. プロジェクト名の設定

1.  `pyproject.toml` 内の `name` を変更する。
2.  `src/my_project` ディレクトリ名を `pyproject.toml` の `name` と一致させる。

## 開発フロー

1.  再利用可能なコードは `src/` 以下に記述する。
2.  テスト記述: tests/ 以下に, src/ に実装した機能のテストコードを記述する。pytestの実行で品質を担保する。
3.  サンプル作成: notebooks/ に, 利用者がパッケージの使い方を理解できるようなサンプルノートブックを作成する。
4.  情報更新: pyproject.tomlのバージョンや作者情報, README.mdを更新し, リリース準備を整える。
  
***
***
***
# ▼ テンプレート利用時は上記を全て削除し, 以下をプロジェクトに合わせて編集する ▼
***

# {project_name}
short description  

## Note
This repository is under construction and will be officially released by [Mizuno group](https://github.com/mizuno-group).  
Please contact tadahaya[at]gmail.com before publishing your paper using the contents of this repository.  

## Installation
You can install this package from PyPI.  

```bash
pip install {project_name}
```

Alternatively, install the latest version directly from the GitHub repository:

```bash
pip install git+[repository URL]
```

## Directory Structure
```
.
├── notebooks/            # example notebooks
│   └── usage_example.ipynb
├── src/
│   └── my_project/       # source codes
│       ├── init.py
│       ├── cli.py        # CLI entry point
│       └── core.py
├── tests/                # test codes
│   └── test_module.py
├── .gitignore
├── LICENSE               
├── pyproject.toml        
└── README.md             
```

## Authors
- [YOUR NAME](LINK OF YOUR GITHUB PAGE)  
    - main contributor  
- [Tadahaya Mizuno](https://github.com/tadahayamiz)  
    - correspondence  

## Contact
If you have any questions or comments, please feel free to create an issue on github here, or email us:  
- YOUR ADDRESS  
- tadahaya[at]gmail.com  
    - lead contact  