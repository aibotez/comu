import itchat
import pyautogui
import time
from pymouse import PyMouse
#pyautogui.click(100,100,clicks=2)
# 154,1 #591,1
# #
m = PyMouse()
#m.move(100,100)

#time.sleep(20)
@itchat.msg_register('Note',isGroupChat=True)
def get(msg):
    if '红包' in msg['Text']:
        print('hhhh')
        time.sleep(0.6)
        m.click(601,637)
        time.sleep(0.2)
        m.click(663,474)
        time.sleep(0.2)
        m.click(663,474)
        time.sleep(0.2)
        m.click(663,474)
        time.sleep(0.2)
        m.click(663,474)


itchat.auto_login(True)
print('登录完成')
itchat.run()
