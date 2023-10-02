# Anime Search TelegramBot

一A Anime Search robot that aggregates and searches images, supports deployment on heroku。

Currently supported websites：

[saucenao](https://saucenao.com/)

[WhatAnime](https://trace.moe/)

[ascii2d](https://ascii2d.net/)

[iqdb](http://www.iqdb.org/)



**Installation Method:**

Log in to your heroku account and click the button below; if you are logged in to heroku in the browser, click directly

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)



Docker

```
docker run  --name search -d \
-e TELEGRAM_TOKEN=Your bot API \
--restart=always \
benchao/search-photo:1.1

```



Sole Owner : [Sung Jin-Woo](https://github.com/Solo-Dragon)
