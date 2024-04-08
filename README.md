# このコードはフォークです
reykim7854さんのコードを動くように修正、日本語化、立ち絵表情差分などを追加したコードです
# タスクリスト
- [ ] 別衣装の立ち絵表情差分
# blue-archive-image-url-scrapper
このPythonスクリプトは、 [Blue Archive Wiki](https://bluearchive.wiki/wiki) から、 [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) を使用して、キャラクターの立ち絵のURLを取得します。
## 要件
- python 3.6+
- beautifulsoup4
- requests
## 使い方
requirements.txt、scrapper.pyをダウンロードしてください
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
  "Yuzu": {
    "00": "https://static.miraheze.org/bluearchivewiki/2/29/Yuzu_00.png",
    "01": "https://static.miraheze.org/bluearchivewiki/a/a2/Yuzu_01.png",
    "02": "https://static.miraheze.org/bluearchivewiki/2/27/Yuzu_02.png",
    "03": "https://static.miraheze.org/bluearchivewiki/0/0e/Yuzu_03.png",
    "04": "https://static.miraheze.org/bluearchivewiki/9/9e/Yuzu_04.png",
    "05": "https://static.miraheze.org/bluearchivewiki/0/0a/Yuzu_05.png",
    "06": "https://static.miraheze.org/bluearchivewiki/c/cb/Yuzu_06.png",
    "07": "https://static.miraheze.org/bluearchivewiki/d/de/Yuzu_07.png",
    "08": "https://static.miraheze.org/bluearchivewiki/0/02/Yuzu_08.png",
    "99": "https://static.miraheze.org/bluearchivewiki/a/a9/Yuzu_99.png"
  },
  "Yuzu (Maid)": {
    "00": "//static.miraheze.org/bluearchivewiki/c/c8/Yuzu_%28Maid%29_00.png"
  }
  }
  ```
