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

For some reason, there were mentions that could not be obtained in domain units. Therefore, it is acquired in units of target (page).

## targets.tsv

Write the URL of the page for which you want to get mentions line by line as shown below.

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
-->

## menbk

```sh
./menbk
```

1. Create a directory with the domain name of the specified page
1. Create a file along the path of the specified page
1. Get all mentions for that page
1. Save as JSON file

For example, it looks like the following.

* `backup/`
    * `ytyaru.github.io/`
        * `ytyaru.github.io.json`
        * `Html.MonaCoin.Button.Component.Generator.20220526192239.json`
        * `Html.MonaCoin.Button.Generator.20220519194201.json`
        * ...

If the page does not have any mentions, do not create a JSON file.

<!--
1. Create a directory with the specified domain name
2. Get domain mentions
3. Get 20 mentions each and make it a JSON file

For example, it looks like the following.

* `{domain}/`
    * `0.json`
    * `1.json`
    * `2.json`
    * `...`
-->

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

