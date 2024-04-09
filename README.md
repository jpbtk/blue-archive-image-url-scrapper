# このコードはフォークです
動かなかった[reykim7854さんのコード](https://github.com/reykim7854/blue-archive-image-url-scrapper)を動くように修正、日本語化、立ち絵表情差分などを追加したコードです
# タスクリスト
- [x] 別衣装(実装生徒)の立ち絵表情差分
- [ ] 別衣装(ストーリーのみ)の立ち絵
- [ ] イロハ
# すぐ使いたいなら
[student-images.json](https://github.com/jpbtk/blue-archive-image-url-scrapper/blob/main/student-images.json)をダウンロードして使ってね(2024/04/09更新)
# blue-archive-image-url-scrapper
このPythonスクリプトは、 [Blue Archive Wiki](https://bluearchive.wiki/wiki) から、 [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) を使用して、キャラクターの立ち絵のURLを取得します。
## 要件
- python 3.6+
- beautifulsoup4
- requests
## 使い方
[requirements.txt](https://github.com/jpbtk/blue-archive-image-url-scrapper/blob/main/requirements.txt)、[scrapper.py](https://github.com/jpbtk/blue-archive-image-url-scrapper/blob/main/scrapper.py)をダウンロードしてください
- `requirements.txt`から必要なライブラリをインストールしてください
  ```
  pip install -r requirements.txt
  ```
- scrapper.pyを実行
  - Windows
    ```
    py scrapper.py
    ```
  - linux / mac
    ```
    python3 scrapper.py
    ```
- 実行結果
```
生徒さんの名前を取得しています...(177/177 キャラクター)
Airiさんの立ち絵を取得しています...(1/177 キャラクター)
Akaneさんの立ち絵を取得しています...(2/177 キャラクター)
Akane (Bunny Girl)さんの立ち絵を取得しています...(3/177 キャラクター)
...
Yuukaさんの立ち絵を取得しています...(174/177 キャラクター)
Yuuka (Sportswear)さんの立ち絵を取得しています...(175/177 キャラクター)
Yuzuさんの立ち絵を取得しています...(176/177 キャラクター)
Yuzu (Maid)さんの立ち絵を取得しています...(177/177 キャラクター)
正常に終了しました。
```
- JSONファイルはここに作られます→`student-images.json`
  
  例:
  ```json
  {
    "Airi": {
    "00": "https://static.miraheze.org/bluearchivewiki/9/9e/Airi_00.png",
    "01": "https://static.miraheze.org/bluearchivewiki/f/ff/Airi_01.png",
    "02": "https://static.miraheze.org/bluearchivewiki/b/b3/Airi_02.png",
    "03": "https://static.miraheze.org/bluearchivewiki/4/40/Airi_03.png",
    "04": "https://static.miraheze.org/bluearchivewiki/0/00/Airi_04.png",
    "05": "https://static.miraheze.org/bluearchivewiki/8/84/Airi_05.png",
    "06": "https://static.miraheze.org/bluearchivewiki/b/ba/Airi_06.png",
    "07": "https://static.miraheze.org/bluearchivewiki/5/52/Airi_07.png",
    "99": "https://static.miraheze.org/bluearchivewiki/f/fa/Airi_99.png"
  },
    ...
  "Yuzu (Maid)": {
    "00": "https://static.miraheze.org/bluearchivewiki/c/c8/Yuzu_%28Maid%29_00.png",
    "01": "https://static.miraheze.org/bluearchivewiki/c/ca/Yuzu_%28Maid%29_01.png",
    "02": "https://static.miraheze.org/bluearchivewiki/9/90/Yuzu_%28Maid%29_02.png",
    "03": "https://static.miraheze.org/bluearchivewiki/3/39/Yuzu_%28Maid%29_03.png",
    "04": "https://static.miraheze.org/bluearchivewiki/7/79/Yuzu_%28Maid%29_04.png",
    "05": "https://static.miraheze.org/bluearchivewiki/4/4b/Yuzu_%28Maid%29_05.png",
    "06": "https://static.miraheze.org/bluearchivewiki/9/94/Yuzu_%28Maid%29_06.png",
    "07": "https://static.miraheze.org/bluearchivewiki/b/b2/Yuzu_%28Maid%29_07.png",
    "08": "https://static.miraheze.org/bluearchivewiki/6/6d/Yuzu_%28Maid%29_08.png",
    "09": "https://static.miraheze.org/bluearchivewiki/8/8b/Yuzu_%28Maid%29_09.png",
    "10": "https://static.miraheze.org/bluearchivewiki/8/8e/Yuzu_%28Maid%29_10.png",
    "99": "https://static.miraheze.org/bluearchivewiki/7/7c/Yuzu_%28Maid%29_99.png"
  }
  }
  ```
