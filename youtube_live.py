import pytchat
import setting

# PytchatCoreオブジェクトの取得
livechat = pytchat.create(setting.video_id)# video_idはhttps://....watch?v=より後ろの

def get_chat():
    if livechat.is_alive():
        # チャットデータの取得
        chatdata = livechat.get()
        for c in chatdata.items:
            print(f"{c.datetime} {c.author.name} {c.message} {c.amountString}")
        return chatdata.items[0].amountString
    return False