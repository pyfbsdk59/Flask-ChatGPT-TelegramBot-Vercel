# Python-ChatGPT-TelegramBot-Docker
# 一個Python ChatGPT TelegramBot快速建置平台。


### [English](https://github.com/pyfbsdk59/Python-ChatGPT-TelegramBot-Docker/blob/main/README_en.md)
### [日本語](https://github.com/pyfbsdk59/Python-ChatGPT-TelegramBot-Docker/blob/main/README_jp.md)


#### 1. 初次上傳專案到github，請多包涵。初版沒有設置另外的.env檔案和環境變數。之後會改正。


#### 2. 本專案參考了以下前輩的方案改成製作，只針對剛學習Python或Docker的朋友來佈置TelegramBot在VPS上：

https://github.com/howarder3/GPT-Linebot-python-flask-on-vercel<br><br>
https://github.com/n3d1117/chatgpt-telegram-bot

#### 3. 可使用任何VPS建制，例如DigitalOcean, Linode或是vultr。 用ssh連入主機，輸入帳密後，

---
# 環境建制（先建制了Makefile）

### Step 1: 輸入以下指令（建制docker和pyenv環境） 
   
    make do1


### Step 2: 輸入以下多行的指令。一個一個複製貼上輸入。（一共有7個指令）

echo 'export LC_ALL=C.UTF-8' >> ~/.bashrc

echo 'export LANG=C.UTF-8' >> ~/.bashrc

echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc

echo 'export PATH="$PYENV_ROOT/shims:$PATH"' >> ~/.bashrc

echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc

echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n eval "$(pyenv init -)"\nfi' >> ~/.bashrc

exec $SHELL


### Step 3: 輸入以下指令 （建制python環境且安裝docker-compose）

     make do2

       
### Step 4: 輸入 cd ~ ，到主目錄，輸入以下指令下載本專案。

    git clone https://github.com/pyfbsdk59/Python-ChatGPT-TelegramBot-Docker.git
   

### Step 5: 輸入以下指令進入本專案目錄（已建制Makefile）。

    cd Python-ChatGPT-TelegramBot-Docker


### Step 6a: 輸入以下指令，開始建制本專案的容器，完成後會有1個container（記得先用nano指令修改main.py的OEPNAI api key的部分，還有加入自己的TelegramBot token和自己的TG帳號的id。）

    make dcup
    
### Step 6b: 也可以不用設置Docker就直接執行，請輸入以下指令，但要先有Python環境。

    python main.py &

------
### 創建Telegram機器人和取得token，請參考： 
https://ithelp.ithome.com.tw/articles/10245264<br><br>
https://tcsky.cc/tips-01-telegram-chatbot/

### 取得自己的Telegram user id，加入機器人，取得。請參考：
https://telegram.me/getidsbot<br><br>
https://blog.csdn.net/qq_40394269/article/details/124832889