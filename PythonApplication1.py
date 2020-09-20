from bangtal import *

scene1 = Scene("방1", "images/배경-1.png")
flower_key = ''

door1 = Object('images/문-오른쪽-닫힘.png')
door1.locate(scene1, 800, 270)
door1.show()
door1.closed = True

key1 = Object('images/열쇠.png')
key1.locate(scene1, 600, 150)
key1.setScale(0.2)
key1.show()

flowerpot = Object('images/화분1.png')
flowerpot.locate(scene1, 550, 150)
flowerpot.moved = False
flowerpot.show()

scene2 = Scene("방2", "images/배경-2.png")

flowerpot2 = Object('images/화분2.png')
flowerpot2.locate(scene2, 550, 150)
flowerpot2.moved = False
flowerpot2.show()

door2 = Object('images/문-오른쪽-열림.png')
door2.locate(scene2, 320, 270)
door2.show()

door3 = Object('images/문-오른쪽-닫힘.png')
door3.locate(scene2, 910, 270)
door3.locked = True
door3.show()

keypad = Object('images/키패드.png')
keypad.locate(scene2, 885, 420)
keypad.show()

switch = Object('images/스위치.png')
switch.locate(scene2, 880, 440)
switch.lighted = True
switch.show()

password = Object('images/암호.png')
password.locate(scene2, 400, 100)


def door1_on_mouse_action(x, y, action):
    if key1.inHand() is False:
        showMessage('열쇠가 필요해!')
    else:
        if door1.closed:
            door1.setImage('images/문-오른쪽-열림.png')
            door1.closed = False
        else:
            scene2.enter()


def door2_on_mouse_action(x, y, action):
    scene1.enter()


def door3_on_mouse_action(x, y, action):
    global flower_key
    if door3.locked:
        showMessage('문이 잠겨있다.')
    else:
        if flower_key == 'wenswew': 
            endGame()
        else:
            showMessage("화분을 움직여 비밀번호를 만들어주세요")


def key1_on_mouse_action(x, y, action):
    key1.pick()


def flowerpot_on_mouse_action(x, y, action):
    # if flowerpot.moved is False:
    flowerpot.moved = True
    if action == MouseAction.DRAG_LEFT:
        flowerpot.locate(scene1, 450, 150)
    elif action == MouseAction.DRAG_RIGHT:
        flowerpot.locate(scene1, 650, 150)




def flowerpot2_on_mouse_action(x, y, action):
    global flower_key
    if flowerpot2.moved is False:
        if action == MouseAction.CLICK:
            flowerpot2.moved = True
            showMessage('비밀번호를 이용해 Key를 얻으세요 알파벳 기준으로 동서남북... 초기화는 클릭')
            
    else:
        if action == MouseAction.CLICK:
            flower_key = ''
            showMessage('비밀번호가 초기화 되었습니다')
            showMessage('비밀번호를 이용해 Key를 얻으세요 알파벳 기준으로 동서남북... 초기화는 클릭')
        if action == MouseAction.DRAG_LEFT:
            flowerpot2.locate(scene2, 450, 150)
            flower_key += 'w'
        elif action == MouseAction.DRAG_RIGHT:
            flowerpot2.locate(scene2, 650, 150)
            flower_key += 'e'
        elif action == MouseAction.DRAG_UP:
            flowerpot2.locate(scene2, 550, 250)
            flower_key += 'n'
        elif action == MouseAction.DRAG_DOWN:
            flowerpot2.locate(scene2, 550, 50)
            flower_key += 's'

        if flower_key == 'wenswew':
            showMessage('완료되었습니다.')


def keypad_on_mouse_action(x, y, action):
    showKeypad('bangtal', door3)


def door3_on_keypad():
    global flower_key
    if flower_key == 'wenswew':
        showMessage('문이 열렸다!')
        door3.locked = False
        door3.setImage('images/문-오른쪽-열림.png')
    else:
        showMessage('화분을 움직여 hidden 비밀번호를 만들어주세요.')


def switch_on_mouse_action(x, y, action):
    switch.lighted = not switch.lighted
    if switch.lighted:
        scene2.setLight(1)
        password.hide()
    else:
        scene2.setLight(0.2)
        password.show()


key1.onMouseAction = key1_on_mouse_action
door1.onMouseAction = door1_on_mouse_action
door2.onMouseAction = door2_on_mouse_action
door3.onMouseAction = door3_on_mouse_action
door3.onKeypad = door3_on_keypad
flowerpot.onMouseAction = flowerpot_on_mouse_action
flowerpot2.onMouseAction = flowerpot2_on_mouse_action
keypad.onMouseAction = keypad_on_mouse_action
switch.onMouseAction = switch_on_mouse_action

startGame(scene1)