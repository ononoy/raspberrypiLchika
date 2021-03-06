#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ライブラリの読み込み
import RPi.GPIO as GPIO
import time
# GPIOピン番号の定義方法を設定する（BCM/BOARD）
GPIO.setmode(RPi.GPIO.BCM)
# 18番ピンを出力モードで初期化する
GPIO.setup(18, GPIO.OUT)
# LED点滅（2秒置き）を5回繰り返す
for x in xrange(5):
    GPIO.output(18, True)
    time.sleep(2)
    GPIO.output(18, False)
    time.sleep(2)
# GPIOを解放
GPIO.cleanup()
