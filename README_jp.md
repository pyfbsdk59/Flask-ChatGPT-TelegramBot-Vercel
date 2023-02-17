# Flask-ChatGPT-TelegramBot-Vercel
# プラットフォーム Vercel 上に迅速に構築された Flask ChatGPT TelegramBot。


### [繁體中文](https://github.com/pyfbsdk59/Flask-ChatGPT-TelegramBot-Vercel/blob/main/README.md)
### [English](https://github.com/pyfbsdk59/Flask-ChatGPT-TelegramBot-Vercel/blob/main/README_en.md)


#### 1. このプロジェクトは、以下のプロジェクトを参照しており、Flask を学習したばかりの人が Vercel に TelegramBot をデプロイするためのものです。

https://github.com/howarder3/GPT-Linebot-python-flask-on-vercel<br><br>
https://github.com/zaoldyeck/telegram-innovation-chatbot/tree/basic

#### 2. このプロジェクトは Vercel にデプロイされているため、コードは Docker のバージョンとは異なり、Flask フレームワークを使用し、webhook を設定する必要があります。 以下のWebhook設定のノウハウをご覧ください。

https://zaoldyeck.medium.com/%E6%89%8B%E6%8A%8A%E6%89%8B%E6%95%99%E4%BD%A0%E6%80%8E%E9%BA%BC%E6%89%93%E9%80%A0-telegram-bot-a7b539c3402a

#### 3. Vercel の環境変数で、OPENAI_API_KEY と TELEGRAM_BOT_TOKEN という 2 つの環境変数を設定する必要があります。

#### 4. ブラウザを開き、以下の URL を入力し、Webhook を Vercel をデプロイした後の最後のステップとして設定してください。 フォーマットは次のように示されます。 https://api.telegram.org/bot{$token}/setWebhook?url={$webhook_url}。

##### 実際の例は次の例のようになります (直接コピーしないでください。自分のテレグラム トークンと Vercel プロジェクトの URL を使用してください)。：


https://api.telegram.org/bot606248605:AAGv_TOJdNNMc_v3toHK_X6M-dev_1tG-JA/setWebhook?url=https://xxx.vercel.app/callback


#### 5. 成功すると次のテキストが表示されます：

{
  ok: true,
  result: true,
  description: "Webhook was set"
}
------
### テレグラム ボットの作成方法とトークンの取得方法については、こちらをご覧ください。. 
https://ithelp.ithome.com.tw/articles/10245264<br><br>
https://tcsky.cc/tips-01-telegram-chatbot/

