# mypkg
[![test](https://github.com/kouzou2111/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/kouzou2111/mypkg/actions/workflows/test.yml)

2023年ロボットシステム学講義用リポジトリ

## リポジトリ内で使用できるコマンド

・talker.py

・listener.py

・talk_listen.launch.py

## talkerの概要

実行すると0.5秒間隔で0から1ずつ足した値をメッセージとしてcountupトピックを通じてパブリッシュする。talker単体では送信中の値を確認することができない。

## 使用方法

```bash
$ ros2 run mypkg talker
```
## listenerの概要

実行するとtalkerが可動しているときcountupトピックを通じてメッセージをサブスクライブした端末で受信することができる。talkerと並列して実行する場合は別の端末から実行する必要がある。

## 使用方法

```bash
$ ros2 run mypkg listener
[INFO] [1703905159.253466126] [listener]: Listen:0
[INFO] [1703905159.736600482] [listener]: Listen:1
[INFO] [1703905160.237778361] [listener]: Listen:2
[INFO] [1703905160.737473958] [listener]: Listen:3
[INFO] [1703905161.237584810] [listener]: Listen:4
[INFO] [1703905161.737528567] [listener]: Listen:5
[INFO] [1703905162.237059324] [listener]: Listen:6
[INFO] [1703905162.737383335] [listener]: Listen:7
[INFO] [1703905163.237154692] [listener]: Listen:8
[INFO] [1703905163.736449315] [listener]: Listen:9
[INFO] [1703905164.237330613] [listener]: Listen:10
```

## talk_listen.launchの概要

talkerとlistenerの機能を一つにまとめ同時に実行できるようにしたもの

## 使用方法

```bash
ros2 launch mypkg talk_listen.launch.py
[INFO] [launch]: All log files can be found below /home/fass1080/.ros/log/2023-12-30-12-07-24-810757-DESKTOP-TTGLLEK-237
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [talker-1]: process started with pid [239]
[INFO] [listener-2]: process started with pid [241]
[listener-2] [INFO] [1703905645.589176274] [listener]: Listen:0
[listener-2] [INFO] [1703905646.080160831] [listener]: Listen:1
[listener-2] [INFO] [1703905646.580714971] [listener]: Listen:2
[listener-2] [INFO] [1703905647.080237070] [listener]: Listen:3
[listener-2] [INFO] [1703905647.580660883] [listener]: Listen:4
[listener-2] [INFO] [1703905648.080767021] [listener]: Listen:5
[listener-2] [INFO] [1703905648.580512568] [listener]: Listen:6
[listener-2] [INFO] [1703905649.080447016] [listener]: Listen:7
[listener-2] [INFO] [1703905649.580470320] [listener]: Listen:8
[listener-2] [INFO] [1703905650.080597975] [listener]: Listen:9
[listener-2] [INFO] [1703905650.580411385] [listener]: Listen:10
```

## 使用手順
下記のコードをホームディレクトリでクローンすることで利用できます
```
git clone https://github.com/kouzou2111/mypkg.git
```

## 動作環境
### 必要なソフトウェア　
* python
  * テスト済み: 3.7~3.10


### テスト環境
* ubuntu 22.04.2 LTS
  * ROS2 humble

### 利用したコンテナ
上田隆一[コンテナ](https://hub.docker.com/layers/ryuichiueda/ubuntu22.04-ros2/latest/images/sha256-0e1773bc6f12b57172c8818aac36aeb97ca13269028028d49ad5f6f8cc0d6204?context=explore)

## ライセンス
* このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
    * このパッケージのtest.ymlのpythonのバージョンテスト部分以外のコードは，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです．
         * [ryuichiueda/my_slides robosys_2022](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2022)
    * © 2023 kouzou2111
