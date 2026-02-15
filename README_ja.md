# personal-colour-labspace

[![DOI](https://zenodo.org/badge/1158264019.svg)](https://doi.org/10.5281/zenodo.18646259)

**Languages:** [English](README.md) | 日本語（本ページ）

本リポジトリは，論文
**「Personal Colour between Perceptual Space and Social Practice」**（採録済み・校正中）
に付随する，匿名化データセットおよび最小限の再現可能コードを提供するものである．

本リポジトリにより，色座標からパーソナルカラーのラベルを分類する分析の再現が可能となる．

## リポジトリ構成
- `data/lab_samples.csv` — 匿名化されたサンプル単位データセット（RGBおよびCIE L\*a\*b\*）
- `data/README_data.md` — データ辞書／コードブック
- `run_pipeline.py` — データセットの読み込みおよび検証を行う最小実行スクリプト
- `requirements.txt` — Python依存パッケージ
- `config.example.yml` — 設定テンプレート（パスおよび乱数シード）
- `.gitignore` — 生成物およびローカル設定ファイルを除外するための設定

## データ概要
各行は1つの色サンプルに対応する．データセットには以下が含まれる：
- sRGB値（`rgb_hex`, `r`, `g`, `b`）
- CIE L\*a\*b\* 座標（`L_star`, `a_star`, `b_star`）
- 2種類のパーソナルカラーラベル：
  - `tone2_label`（2値トーン）
  - `season_label`（季節ラベル；`spring_autumn` のような曖昧カテゴリを含む）

詳細は `data/README_data.md` を参照されたい．

## クイックスタート
1. Python環境を作成し，依存関係をインストールする：
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
2. ローカル設定ファイルを作成する：
   ```bash
   cp config.example.yml config.yml
   ```
3. 実行する：
   ```bash
   python run_pipeline.py
   ```

## 再現性に関する注意
- 本リポジトリは，機械固有の絶対パス（例：個人のGoogle Driveディレクトリ）への依存を避ける設計としている．
- 乱数シードは `config.yml` により制御される（デフォルト：`seed: 42`）．
- 本データセットはRGBとCIE L\*a\*b\*の両方を提供し，実装依存の変換手続きに左右されない下流分析を可能にする．

## ライセンスと引用
- コードのライセンス：MIT License（`LICENSE` を参照）
- データのライセンス：CC BY 4.0 (`data/LICENSE` を参照)
- 引用：ZenodoのConcept DOI（全バージョン）を引用されたい： https://doi.org/10.5281/zenodo.18646259

