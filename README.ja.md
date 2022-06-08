[en](./README.md)

# Webmention.io.Backup

　[webmention.io][]のJSONデータをバックアップするCLI。

* [webmention.io API][]
    * `https://webmention.io/api/mentions.jf2?token=xxxxx&domain=yyyyyyy`

[webmention.io]:https://webmention.io
[webmention.io API]:https://github.com/aaronpk/webmention.io#api

# 開発環境

* <time datetime="2022-06-04T13:36:34+0900">2022-06-04</time>
* [Raspbierry Pi](https://ja.wikipedia.org/wiki/Raspberry_Pi) 4 Model B Rev 1.2
* [Raspberry Pi OS](https://ja.wikipedia.org/wiki/Raspbian) buster 10.0 2020-08-20 <small>[setup](http://ytyaru.hatenablog.com/entry/2020/10/06/111111)</small>
* bash 5.0.3(1)-release
* Python 2.7.16
* Python 3.7.3

```sh
$ uname -a
Linux raspberrypi 5.10.63-v7l+ #1496 SMP Wed Dec 1 15:58:56 GMT 2021 armv7l GNU/Linux
```

# インストール

```sh
sudo apt install python3 python3-pip
```
```sh
git clone https://github.com/ytyaru/Python.Webmention.io.Backup.20220604133640
cd Python.Webmention.io.Backup.20220604133640/src
```

# 使い方

　なぜかdomain単位だと取得できないメンションがあった。よってtarget（ページ）単位で取得するようにした。

## targets.tsv

　以下のようにメンションを取得したいページのURLを１行ずつ書く。

```tsv
https://ytyaru.github.io/
https://ytyaru.github.io/Html.Mpurse.Api.20220517160403/setup.html
https://ytyaru.github.io/Html.Mpurse.Api.20220517160403/index.html
https://ytyaru.github.io/Html.SNS.Icon.20220524195153/
https://ytyaru.github.io/MonaCoin.Icon.20220521092535/
https://ytyaru.github.io/Html.MonaCoin.Button.Generator.20220519194201/
https://ytyaru.github.io/Html.MonaCoin.Button.Component.Generator.20220526192239/
https://ytyaru.github.io/Html.MonaCoin.Button.Component.Generator.Animation.20220531091850/
https://ytyaru.github.io/Html.MonaCoin.Button.Component.Generator.Slim.20220531090526/
https://ytyaru.github.io/Html.Mastodon.Toot.Button.Dialog.WebComponent.20220602192922/
https://ytyaru.github.io/Html.Tweet.Button.Generator.20220606171017/
https://ytyaru.github.io/Html.Tweet.Button.WebComponent.20220607091729/
https://ytyaru.github.io/Html.Webmention.WebComponent.20220607141057/
```

<!--

## domain単位

### setting.tsv

　次のように「setting.tsv」ファイルを作成する。

```sh
webmention-token	target-domain
webmention-token	target-domain
webmention-token	target-domain
...
```

* [webmention.io][]で取得したAPI Keyを1列目にセットする
* webmentionを取得したいサイトのドメイン名を2列目にセットする（「example.com」等）
* 上記を好きな数だけ用意する

-->

## menbk

```sh
./menbk
```

1. 指定したページのドメイン名のディレクトリを作る
1. 指定したページのパスに沿ったファイルを作る
1. そのページのメンションを全件取得する
1. JSONファイルとして保存する

　たとえば以下のような感じ。

* `backup/`
    * `ytyaru.github.io/`
        * `ytyaru.github.io.json`
        * `Html.MonaCoin.Button.Component.Generator.20220526192239.json`
        * `Html.MonaCoin.Button.Generator.20220519194201.json`
        * ...

　なお、メンションが一件も存在しないページなら、JSONファイルは作成しない。

<!--
1. 指定したドメイン名のディレクトリを作る
2. ドメインのメンションを取得する
3. メンションは20件ずつ取得してJSONファイルにする

　たとえば以下のような感じ。

* `{domain}/`
    * `0.json`
    * `1.json`
    * `2.json`
    * `...`
-->

# 著者

　[ytyaru][]

[ytyaru]:https://ytyaru.github.io/

* [![github](http://www.google.com/s2/favicons?domain=github.com)](https://github.com/ytyaru "github")
* [![hatena](http://www.google.com/s2/favicons?domain=www.hatena.ne.jp)](http://ytyaru.hatenablog.com/ytyaru "hatena")
* [![twitter](http://www.google.com/s2/favicons?domain=twitter.com)](https://twitter.com/ytyaru1 "twitter")
* [![mastodon](http://www.google.com/s2/favicons?domain=mstdn.jp)](https://mstdn.jp/web/accounts/233143 "mastdon")

# ライセンス

　このソフトウェアはCC0ライセンスである。

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](http://creativecommons.org/publicdomain/zero/1.0/deed.ja)

