from bangtal import *

import random

import copy

import time

 

 

setGameOption(GameOption.INVENTORY_BUTTON, False)

setGameOption(GameOption.MESSAGE_BOX_BUTTON, False)

 

 

 

main_scene = Scene("퍼즐게임", "images/backgroud.PNG")

scene1 = Scene("Loopy 퍼즐", "images/backgroud.PNG")

scene2 = Scene("Lion 퍼즐", "images/backgroud.PNG")

 

help_message = showMessage("퍼즐 맞출 이미지를 클릭해주세요!!")

 

images = (

    Object('images/loopy.jpg'),

    Object('images/lion.jpg'),

    Object('images/exit_button.png'),

    Object('images/score.jpg'),

    Object('images/another.jpg')

)

 

loopy_image = images[0]

loopy_image.locate(main_scene, 150, 50)

loopy_image.setScale(1.64)

loopy_image.show()

 

lion_image = images[1]

lion_image.locate(main_scene, 650, 50)

lion_image.setScale(0.7)

lion_image.show()

 

exit_button = images[2]

exit_button.locate(main_scene, 1150, 650)

exit_button.setScale(0.1)

exit_button.show()

 

 

blank = 8

game_board = []

init_board = []

start = 0

max_time = 987654321

loopy_max_score = 0

lion_max_score = 0

 

def hide_image():

    loopy_image.hide()

    lion_image.hide()

    exit_button.hide()

 

 

def exit_on_mouse_action(x, y, action):

    exit(0)

 

def loopy_on_mouse_action(x, y, action):

    global game_board, init_board, start, images

    start = 0

    start = time.time()

    hide_image()

    game_board = []

    init_board = []

    for index in range(100):

        piece = Object("images/loopy_" + str(index + 1) + ".jpg" )

        piece.locate(scene1, 300 + 150 * (index % 3), 460 - 150 * (index // 3))

        piece.setScale(0.61)

        piece.show()

 

        game_board.append(piece)

        init_board.append(piece)

 

    game_board[blank].hide()

    for _ in range(3):

        random_move(scene1)

#    timer.onTimeout = onTimeout

 

#    timer.start()

    startGame(scene1)

 

 

def lion_on_mouse_action(x, y, action):

    hide_image()

    global game_board, init_board, start

    start = 0

    start = time.time()

    game_board = []

    init_board = []

    for index in range(100):

        piece = Object("images/lion_" + str(index + 1) + ".jpg" )

        piece.locate(scene2, 300 + 150 * (index % 3), 460 - 150 * (index // 3))

        piece.setScale(0.7)

        piece.show()

 

        game_board.append(piece)

        init_board.append(piece)

 

    game_board[blank].hide()

    for _ in range(3):

        random_move(scene2)

    startGame(scene2)

 

 

def find_index(object):

    global game_board

    for index in range(9):

        if game_board[index] == object: return index

 

def movable(index):

    global blank

    if index < 0: return False

    if index > 8: return False

    if index % 3 > 0 and index - 1 == blank: return True

    if index % 3 < 2 and index + 1 == blank: return True

    if index > 2 and index - 3 == blank: return True

    if index < 6 and index + 3 == blank: return True

    return False

 

 

delta = [-1, 1, -3, 3]

def random_move(obj):

    global blank, delta

    while True:

        index = blank + delta[random.randrange(4)]

        if movable(index): break

    

    move(obj, index)

 

def move(obj, index):

    global blank, game_board

    game_board[index].locate(obj, 300 + 150 * (blank % 3), 460 - 150 * (blank // 3))

    game_board[blank].locate(obj, 300 + 150 * (index % 3), 460 - 150 * (index // 3))

 

    game_board[index], game_board[blank] = game_board[blank], game_board[index]

    

    blank = index

 

 

def completed():

    

    for index in range(9):

        if game_board[index] != init_board[index]: return False

    return True

 

 

def onMouseAction_piece(object, x, y, action):

    global blank, start, max_time

    sc = None

    index = find_index(object)

    if 'loopy' in object._file:

        sc = scene1

    else:

        sc = scene2

 

    if movable(index):

        move(sc, index)

 

        if completed():

            score = time.time() - start

            if max_time > score:

                max_time = score

                showMessage('The shortest time has been renewed. max score: {:2}, time: {:2} Completed!!!'.format(time.strftime('%H:%M:%S', time.gmtime(score)), time.strftime('%H:%M:%S', time.gmtime(score))))

            else:

                showMessage('Shortest time failed to break. max score: {:2}, time{:2} Completed!!!'.format(time.strftime('%H:%M:%S', time.gmtime(max_time)), time.strftime('%H:%M:%S', time.gmtime(score))))

 

 

Object.onMouseActionDefault = onMouseAction_piece
