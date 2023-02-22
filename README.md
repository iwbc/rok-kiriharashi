# RoK 切原市

Rise of Kingdoms 霧晴らし自動化スクリプト（やっつけ仕事版）

### 動作環境

- Windows 10-11
- Python 3.10（Microsoft Store版）
- NoxPlayer 7

### セットアップ

#### 環境

Pythonは[Microsoft Store](https://www.microsoft.com/ja-jp/p/python-310/9pjpw5ldxlz5?cid=msft_web_chart&activetab=pivot:overviewtab)からインストールするのが手軽。

コマンドプロンプトやPowerShellで以下のコマンドを入力し、動作に必要なモジュールをインストールしてください。

```bash
pip install android-auto-play-opencv
```

#### NoxPlayerとライキンの設定

NoxPlayerの設定は、パフォーマンス「高い（4コアCPU、4096MBメモリ）」、解像度「1600x900」にし、ライキンは、画質「中」、フレームレート「至高」にします。

### 使い方

斥候キャンプを都市の真ん中に配置し、斥候キャンプの画面を開いた状態で実行します。

```bash
python bot.py
```
