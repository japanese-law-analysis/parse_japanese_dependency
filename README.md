# parse_japanese_dependency

[Ginza](https://megagonlabs.github.io/ginza/)を用いて係り受けの解析を行うソフトウェアです。

```
python parse_japanese_dependency.py --input input.json --output output.json
```

で使用できます。

`input.json`には文と文のIDを書きます。書き方は`test.json`を見てください。

また、ライブラリとしては解析対象のテキストとモデルを受け取って解析結果の辞書情報を返す`parse_document`関数が使用できます。


# インストール

依存ライブラリは

- spacy
- ginza
- ja_ginza
- ja_ginza_electra

です。

詳しくは[Ginza](https://megagonlabs.github.io/ginza/)の「実行環境のセットアップ/2. GiNZA + 従来型モデル」の節などを確認してください。

