import telegram


class Messenger:
    token = '1424769968:AAGuBZwW1p3EdDZjRbix7FbzfxuLSywHuqw'
    chat_id = '1564304240'
    motion_alert_text = 'Motion Detected'
    bot = telegram.Bot(token=token)

    def __init__(self) -> None:
        super().__init__()

    def send_motion_alert(self):
        self.bot.send_message(self.chat_id, self.motion_alert_text)
