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
        "avatar": "https://static.miraheze.org/bluearchivewiki/9/96/Airi.png",
        "full_image": "https://static.miraheze.org/bluearchivewiki/4/4b/Airi_full.png"
    },
    ...
    "Yuzu": {
      "avatar": "https://static.miraheze.org/bluearchivewiki/7/71/Yuzu.png",
      "full_image": "https://static.miraheze.org/bluearchivewiki/0/0d/Yuzu_full.png"
    }
  }
  ```
