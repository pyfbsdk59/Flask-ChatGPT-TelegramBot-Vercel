# Flask-ChatGPT-TelegramBot-Vercel
# A Flask ChatGPT TelegramBot quickly built on the platform Vercel.


### [繁體中文](https://github.com/pyfbsdk59/Flask-ChatGPT-TelegramBot-Vercel/blob/main/README.md)
### [日本語](https://github.com/pyfbsdk59/Flask-ChatGPT-TelegramBot-Vercel/blob/main/README_jp.md)


#### 0. Migrating to GPT3.5 model...



#### 1. This project refers to the following predecessors' projects, and it is only for friends who have just learned Flask to deploy TelegramBot on Vercel:

https://github.com/howarder3/GPT-Linebot-python-flask-on-vercel<br><br>
https://github.com/zaoldyeck/telegram-innovation-chatbot/tree/basic

#### 2. Since this project is deployed on Vercel, the code is different from the version of Docker, and Flask framework must be used and webhook must be set. Please see knowhows of  setting webhook below.

https://zaoldyeck.medium.com/%E6%89%8B%E6%8A%8A%E6%89%8B%E6%95%99%E4%BD%A0%E6%80%8E%E9%BA%BC%E6%89%93%E9%80%A0-telegram-bot-a7b539c3402a

#### 3. Two environment variables must be set in Vercel's Environment Variables, namely OPENAI_API_KEY and TELEGRAM_BOT_TOKEN.

#### 4. Please open the browser, enter the following URL, and set the webhook as the last step after deploying Vercel. The format is shown as https://api.telegram.org/bot{$token}/setWebhook?url={$webhook_url}。

##### The actual example is like the following example (Don't copy it directly, please use your own telegram token and the URL of the Vercel project)：


https://api.telegram.org/bot606248605:AAGv_TOJdNNMc_v3toHK_X6M-dev_1tG-JA/setWebhook?url=https://xxx.vercel.app/callback


#### 5. The following text will be shown after success：

{
  ok: true,
  result: true,
  description: "Webhook was set"
}
------
### You can learn how to create a telegram bot and get the token here. 
https://ithelp.ithome.com.tw/articles/10245264<br><br>
https://tcsky.cc/tips-01-telegram-chatbot/

