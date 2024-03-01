import pytchat
import time

import setting
import core
# PytchatCoreオブジェクトの取得
livechat = pytchat.create(setting.video_id)# video_idはhttps://....watch?v=より後ろの

while livechat.is_alive():
    # チャットデータの取得
    chatdata = livechat.get()
    for c in chatdata.items:
        print(f"{c.datetime} {c.author.name} {c.message} {c.amountString}")
        core.talk(c.amountString)
    time.sleep(5)