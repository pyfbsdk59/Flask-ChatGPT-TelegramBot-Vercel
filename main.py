import logging
import os


import telegram.constants
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
import openai
	
openai.api_key = os.getenv("OPENAI_API_KEY") 


chat_language = os.getenv("INIT_LANGUAGE", default = "zh")
	
MSG_LIST_LIMIT = int(os.getenv("MSG_LIST_LIMIT", default = 20))
LANGUAGE_TABLE = {
	  "zh": "哈囉！",
	  "en": "Hello!"
	}


class Prompts:
	    def __init__(self):
	        self.msg_list = []
	        self.msg_list.append(f"AI:{LANGUAGE_TABLE[chat_language]}")
	    
	    def add_msg(self, new_msg):
	        if len(self.msg_list) >= MSG_LIST_LIMIT:
	            self.remove_msg()
	        self.msg_list.append(new_msg)
	
	    def remove_msg(self):
	        self.msg_list.pop(0)
	
	    def generate_prompt(self):
	        return '\n'.join(self.msg_list)	
	
class ChatGPT:  
    def __init__(self):
        self.prompt = Prompts()
        self.model = os.getenv("OPENAI_MODEL", default = "text-davinci-003")
        self.temperature = float(os.getenv("OPENAI_TEMPERATURE", default = 0))
        self.frequency_penalty = float(os.getenv("OPENAI_FREQUENCY_PENALTY", default = 0))
        self.presence_penalty = float(os.getenv("OPENAI_PRESENCE_PENALTY", default = 0.6))
        self.max_tokens = int(os.getenv("OPENAI_MAX_TOKENS", default = 240))
	
    def get_response(self):
        response = openai.Completion.create(
	            model=self.model,
	            prompt=self.prompt.generate_prompt(),
	            temperature=self.temperature,
	            frequency_penalty=self.frequency_penalty,
	            presence_penalty=self.presence_penalty,
	            max_tokens=self.max_tokens
                )
        
        print("AI回答內容：")        
        print(response['choices'][0]['text'].strip())

        print("AI原始回覆資料內容：")      
        print(response)
        
        return response['choices'][0]['text'].strip()
	
    def add_msg(self, text):
        self.prompt.add_msg(text)


class ChatGPT3TelegramBot:

    def __init__(self):
        self.chatgpt = ChatGPT()

    # Help menu
    async def help(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await update.message.reply_text("/start - Start the bot\n/reset - Reset conversation\n/help - Help menu")

    # Start the bot
    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        if not self.is_allowed(update):
            logging.info(f'User {update.message.from_user.name} is not allowed to start the bot')
            return

        logging.info('Bot started')
        await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a Chat-GPT3 Bot, please talk to me!")

    # Reset the conversation
    async def reset(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        if not self.is_allowed(update):
            logging.info(f'User {update.message.from_user.name} is not allowed to reset the bot')
            return

        logging.info('Resetting the conversation...')
#
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Done!")

    # Refresh session
    async def refresh(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        if not self.is_allowed(update):
            logging.info(f'User {update.message.from_user.name} is not allowed to refresh the session')
            return

        logging.info('Refreshing session...')
#
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Done!")



    # React to messages
    async def prompt(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        if not self.is_allowed(update):
            logging.info(f'User {update.message.from_user.name} is not allowed to use the bot')
            return

        logging.info(f'New message received from user {update.message.from_user.name}')
        await context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.constants.ChatAction.TYPING)
        
        ai_reply_response = self.get_chatgpt_response(update.message.text)
        
        
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            reply_to_message_id=update.message.message_id,
            text=  ai_reply_response, #AI回答的內容
            #text=response["message"], #原始程式
            parse_mode=telegram.constants.ParseMode.MARKDOWN
        )

    def get_chatgpt_response(self, user_message) -> dict:
        try:

            #user_message #接收人類問題的字詞變數
            self.chatgpt.prompt.add_msg(f"HUMAN:{user_message}?\n")
            response = self.chatgpt.get_response() #ChatGPT產生的回答
            
            print("AI回答內容2：")      
            print(response) 

            return response
        
        except ValueError as e:
            logging.info(f'Error: {e}')
            return {"message": "I'm having some trouble talking to you, please try again later."}

    async def error_handler(self, update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
        logging.debug(f'Exception while handling an update: {context.error}')

    def is_allowed(self, update: Update) -> bool:
        
        allowed_chats= os.getenv("TELEGRAM_USER_ID") 
        #""  #引號中填入允許通話的Telegram id #Please add your Telegram id between "".
        
        return str(update.message.from_user.id) in allowed_chats #self.config['allowed_chats']

    def run(self):
        
        telegram_bot_token = os.getenv("TELEGRAM_BOT_TOKEN") 
        
        application = ApplicationBuilder().token(telegram_bot_token).build()

        application.add_handler(CommandHandler('start', self.start))
        application.add_handler(CommandHandler('reset', self.reset))
        application.add_handler(CommandHandler('help', self.help))
        application.add_handler(CommandHandler('refresh', self.refresh))
        application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), self.prompt))

        application.add_error_handler(self.error_handler)

        application.run_polling()
#####################################################################

def main():
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )

    telegram_bot = ChatGPT3TelegramBot()
    

    telegram_bot.run()



if __name__ == '__main__':
    main()
