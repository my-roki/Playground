import os
import requests
from dotenv import load_dotenv


class MessageBot:
    def __init__(self, discord_webhook_url: str = "", slack_token: str = ""):
        self.discord_webhook_url = discord_webhook_url
        self.slack_token = slack_token

    # discord_webhook_url : Discord Webhook URL
    # content : Discord Webhook이 보낼 텍스트 메시지. 마크다운 형식이 지원된다.
    def discord_message(self, content: str) -> None:
        if self.discord_webhook_url.startswith("https://discord.com/api/webhooks/"):
            raise Exception("Discord Webhook URL이 잘못되었습니다.")

        message = {"content": content}
        requests.post(self.discord_webhook_url, data=message)

    # channel : 메시지를 보낼 채널 #stock_notice
    # text : Slack Bot이 보낼 텍스트 메시지. 마크다운 형식이 지원된다.
    def slack_message(self, channel, text) -> None:
        if self.slack_token == "":
            raise Exception("Slack Token이 잘못되었습니다.")

        requests.post(
            "https://slack.com/api/chat.postMessage",
            headers={"Authorization": "Bearer " + self.slack_token},
            data={"channel": channel, "text": text},
        )


if __name__ == "__main__":
    # 환경변수 설정
    load_dotenv()
    USERNAME = os.getenv("USERNAME")
    ENCRYPTED_PASSWORD = os.getenv("ENCRYPTED_PASSWORD")
    DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")
    SLACK_TOKEN = os.getenv("SLACK_TOKEN")

    message_bot = MessageBot(
        discord_webhook_url=DISCORD_WEBHOOK_URL,
        slack_token=SLACK_TOKEN,
    )
    message_bot.discord_message("test")
    message_bot.slack_message("#99-명령어테스트", "test")
