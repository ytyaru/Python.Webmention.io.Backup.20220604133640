[ja](./README.ja.md)

# Webmention.io.Backup

CLI to back up JSON data of [webmention.io][].

* [webmention.io API][]
    * `https://webmention.io/api/mentions.jf2?token=xxxxx&domain=yyyyyyy`

[webmention.io]:https://webmention.io
[webmention.io API]:https://github.com/aaronpk/webmention.io#api

# Requirement

* <time datetime="2022-06-04T13:36:34+0900">2022-06-04</time>
* [Raspbierry Pi](https://ja.wikipedia.org/wiki/Raspberry_Pi) 4 Model B Rev 1.2
* [Raspberry Pi OS](https://ja.wikipedia.org/wiki/Raspbian) buster 10.0 2020-08-20 <small>[setup](http://ytyaru.hatenablog.com/entry/2020/10/06/111111)</small>
* bash 5.0.3(1)-release
* Python 2.7.16
* Python 3.7.3
* [pyxel][] 1.3.1

[pyxel]:https://github.com/kitao/pyxel

```sh
$ uname -a
Linux raspberrypi 5.10.63-v7l+ #1496 SMP Wed Dec 1 15:58:56 GMT 2021 armv7l GNU/Linux
```

# Installation

```sh
sudo apt install python3 python3-pip
```
```sh
git clone https://github.com/ytyaru/Python.Webmention.io.Backup.20220604133640
cd Python.Webmention.io.Backup.20220604133640/src
```

# Usage

## setting.tsv

Create a "setting.tsv" file as follows.

```sh
webmention-token	target-domain
webmention-token	target-domain
webmention-token	target-domain
...
```

* Set the API Key obtained by [webmention.io][] in the first column.
* Set the domain name of the site for which you want to get webmention in the second column ("example.com" etc.)
* Prepare as many of the above as you like

## menbk

```sh
./menbk
```

1. Create a directory with the specified domain name
2. Get domain mentions
3. Get 20 mentions each and make it a JSON file

For example, it looks like the following.

* `{domain}/`
    * `0.json`
    * `1.json`
    * `2.json`
    * `...`

# Author

　[ytyaru][]

[ytyaru]:https://ytyaru.github.io/

* [![github](http://www.google.com/s2/favicons?domain=github.com)](https://github.com/ytyaru "github")
* [![hatena](http://www.google.com/s2/favicons?domain=www.hatena.ne.jp)](http://ytyaru.hatenablog.com/ytyaru "hatena")
* [![twitter](http://www.google.com/s2/favicons?domain=twitter.com)](https://twitter.com/ytyaru1 "twitter")
* [![mastodon](http://www.google.com/s2/favicons?domain=mstdn.jp)](https://mstdn.jp/web/accounts/233143 "mastdon")

# License

This software is CC0 licensed.

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](http://creativecommons.org/publicdomain/zero/1.0/deed.en)

