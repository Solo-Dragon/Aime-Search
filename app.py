


from bot import *

import threading
from flask import Flask
status =""
app = Flask(__name__)

@app.route('/bot', methods=['GET'])
def bot_info():
    try:
        print(bot.get_me())
        return str(bot.get_me())
    except:
        return "Unable to obtain bot information，Check, please api token"

def run_bot():

    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            time.sleep(10)




@app.route('/', methods=['GET'])
def index():
    global status
    if status=="":
        t1 = threading.Thread(target=run_bot)  

        t1.start()

        print(t1.is_alive())
        status=t1
        # threading.enumerate()
        #print(threading.enumerate())
        return "Arise Bot", 200
    else:
        print(status.is_alive())
        if status.is_alive()==True:
            return "Bot Already Running", 200
        elif status.is_alive()==False:
            t1 = threading.Thread(target=run_bot)

            t1.start()

            print(t1.is_alive())
            status=t1
            return "Rerise Bot", 200

#worker: python3 bot.py

if __name__ == '__main__':

    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)