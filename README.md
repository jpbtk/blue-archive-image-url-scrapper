# このコードはフォークです
reykim7854さんのコードを動くように修正、日本語化、立ち絵表情差分などを追加したコードです
# blue-archive-image-url-scrapper
This python script scraps Blue Archive character image URLs from [Blue Archive Wiki](https://bluearchive.wiki/wiki) using [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/).
## 要件
- python 3.6+
- beautifulsoup4
- requests
## 使い方
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
      "avatar": "https://static.miraheze.org/bluearchivewiki/7/71/Yuzu.png",
      "full_image": "https://static.miraheze.org/bluearchivewiki/0/0d/Yuzu_full.png"
    }
  }
  ```
