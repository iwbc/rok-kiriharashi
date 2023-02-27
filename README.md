# RoK 切原市

Rise of Kingdoms 霧晴らし自動化スクリプト（やっつけ仕事版）

## 動作環境

- Windows 10-11
- BlueStacks 5 or NoxPlayer 7

## セットアップ

### ダウンロード

[kiriharashi.exe v1.1.1](https://github.com/iwbc/rok-kiriharashi/releases/download/1.1.1/kiriharashi.exe)

### BlueStacks（NoxPlayer）とライキンの設定

#### BlueStacks（NoxPlayer）の設定

インスタンスを以下の設定で新しく作成してください。

- Androidバージョン：
  - Nougat 32bit（BlueStacksのみ）
  - Android 7 32bit（NoxPlayerのみ）
- パフォーマンス
  - CPU：4コア
  - メモリ：4GB（4096MB）
- 解像度：1600x900
- 画素密度：240DPI（BlueStacksのみ）
- 上位設定の`Android Debug Bridge`を有効化（BlueStacksのみ）

#### ライキンの設定

- 画質：中
- フレームレート：至高
- 言語：日本語

## 使い方

斥候キャンプを都市の真ん中に配置してください。  
斥候管理画面を開いた状態でkiriharashi.exeを実行し、自動操作したいエミュレーターの番号を入力します。  
※ BlueStacksの場合、起動後にBOTがエミュレーターを検出できるようになるまで少し時間がかかります。


## 開発用

### exe化

```
nuitka --onefile --standalone --include-data-dir=templates=templates --include-data-files=libs/adb.exe=libs/adb.exe --include-data-files=libs/AdbWinApi.dll=libs/AdbWinApi.dll .\kiriharashi.py
```
