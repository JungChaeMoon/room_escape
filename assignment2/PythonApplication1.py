from bangtal import *
import random
import copy

setGameOption(GameOption.INVENTORY_BUTTON, False)
setGameOption(GameOption.MESSAGE_BOX_BUTTON, False)

puzzle_images = {
    'loopy':[
        Object('images/loopy_1.jpg'), 
        Object('images/loopy_2.jpg'),
        Object('images/loopy_3.jpg'),
        Object('images/loopy_4.jpg'),
        Object('images/loopy_5.jpg'),
        Object('images/loopy_6.jpg'),
        Object('images/loopy_7.jpg'),
        Object('images/loopy_8.jpg'),
    ],
    'lion': [
        Object('images/lion_1.jpg'), 
        Object('images/lion_2.jpg'),
        Object('images/lion_3.jpg'),
        Object('images/lion_4.jpg'),
        Object('images/lion_5.jpg'),
        Object('images/lion_6.jpg'),
        Object('images/lion_7.jpg'),
        Object('images/lion_8.jpg'),
    ]
}

seted = [False] * 9

init_locate = [[None, None, None],[ None, None, None],[None, None, None]]
shuffle_locate = []


puzzle_game_background = Scene("퍼즐게임", "images/backgroud.PNG")
puzzle_game_loopy_bg = Scene("루피 퍼즐", 'images/backgroud.PNG')
puzzle_game_lion_bg = Scene("라이언 퍼즐", 'images/backgroud.PNG')

help_message = showMessage('퍼즐맞출 이미지를 클릭해주세요!!')

images = (
    Object('images/loopy.jpg'),
    Object('images/lion.jpg')
)

loopy_image = images[0]
loopy_image.locate(puzzle_game_background, 150, 50)
loopy_image.setScale(1.64)
loopy_image.show()


lion_image = images[1]
lion_image.locate(puzzle_game_background, 650, 50)
lion_image.setScale(0.7)
lion_image.show()

exit_button = Object('images/exit_button.png')
exit_button.locate(puzzle_game_background, 400, 500)
exit_button.setScale(0.2)
exit_button.show()


def hide_image():
    lion_image.hide()
    loopy_image.hide()
    exit_button.hide()


def loopy_on_mouse_action(x, y, action):
    global puzzle_game_loopy_bg, init_locate, shuffle_locate
    hide_image()
    count = -1
    for idx, obj in enumerate(puzzle_images['loopy']):
        if idx % 3 == 0:
            count += 1
        init_locate[count][idx % 3] = obj
        init_locate[count][idx % 3].setScale(0.7)
        init_locate[count][idx % 3].locate(puzzle_game_loopy_bg, 150 + ( 175 * ((idx % 3) + 1)), 500 - (count * 175))

    shuffle_locate = copy.deepcopy(init_locate)
    random_shuffle()

    for i in range(0,3):
        for j in range(0,3):
            if shuffle_locate[i][j] is None:
                continue
            shuffle_locate[i][j].show()

    puzzle_game_loopy_bg.enter()
    

def random_shuffle():
    global shuffle_locate

    x = 2
    y = 2
    dir_x = [-1,1,0,0]
    dir_y = [0,0,1,-1]

    for _ in range(10000):
        num = random.randint(0, 3)
        nx = x + dir_x[num]
        ny = y + dir_y[num]
        if shuffle_locate[x][y] is None and 0<=nx<=2 and 0<=ny<=2:
            shuffle_locate[x][y], shuffle_locate[nx][ny] = shuffle_locate[nx][ny], shuffle_locate[x][y]
            x = nx - 1
            y = ny - 1


def move(x, y):
    global shuffle_locate

    dir_x = [-1, 1, 0, 0]
    dir_y = [0, 0, 1, -1]
    for i in range(4):
        nx = x + dir_x[i]
        ny = y + dir_y[i]
        if nx < 0 or ny > 2 or nx < 0 or ny > 2:
            continue
        if shuffle_locate[nx][ny] is not None:
            continue
        shuffle_locate[x][y] = None
        shuffle_locate[x][y].locate(puzzle_game_loopy_bg, nx, ny)
        break
    is_correct()


def is_correct():
    global shuffle_locate, init_locate

    if shuffle_locate == init_locate:
        return True
    else:
        return False


    
def lion_on_mouse_action(x, y, action):
    global puzzle_game_lion_bg, init_locate, shuffle_locate
    hide_image()
    count = -1
    for idx, obj in enumerate(puzzle_images['lion']):
        if idx % 3 == 0:
            count += 1
        init_locate[count][idx % 3] = obj
        init_locate[count][idx % 3].setScale(0.7)
        init_locate[count][idx % 3].locate(puzzle_game_loopy_bg, 150 + ( 175 * ((idx % 3) + 1)), 500 - (count * 175))
        init_locate[count][idx % 3].show()

    puzzle_game_lion_bg.enter()
    shushuffle_locate = copy.deepcopy(init_locate)

def exit_on_mouse_action(x, y, action):
    exit(0)



def start_puzzle_game(x, y, action):
    start_button.hide()
    exit_button.hide()




loopy_image.onMouseAction = loopy_on_mouse_action
lion_image.onMouseAction = lion_on_mouse_action
exit_button.onMouseAction = exit_on_mouse_action
for _, values in puzzle_images.items():
    for val in values:
        val = move





startGame(puzzle_game_background)