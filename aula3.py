from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.mouse import *

SPEED_BALL_X = 250
SPEED_BALL_Y = 150
SPEED_PAD = 300

window = Window(600, 480)
window.set_title("Pong")
keyboard = window.get_keyboard()

background = GameImage("grama.jpg")
ball = Sprite("bola.png")
pad_left = Sprite("padE.png")
pad_right = Sprite("padD.png")

scoreP1 = 0
scoreP2 = 0

def start():
	ball.set_position(window.height/2, window.width/2)

def draw():
	background.draw()
	pad_left.draw()
	pad_right.draw()
	ball.draw()

	window.draw_text(str(scoreP1), 0, 0, 60, (255,255,255), "Liberation Sans Serif", False, False)
	window.draw_text(str(scoreP2), 575, 0, 60, (255,255,255), "Liberation Sans Serif", False, False)

ball.x = window.width/2 - ball.width/2
ball.y = window.height/2 - ball.height/2

pad_right.x = 0
pad_left.x = window.width - pad_left.width
pad_right.y = window.height/2 - pad_right.height/2
pad_left.y = window.height/2 - pad_left.height/2

while(True):

	ball.x = ball.x + SPEED_BALL_X * window.delta_time()
	ball.y = ball.y + SPEED_BALL_Y * window.delta_time()

	if(ball.x + ball.width > window.width):
		start()
		scoreP1 += 1	

	if(ball.x < 0):
		start()
		scoreP2 += 1

	if(ball.y + ball.height > window.height):
		ball.y = ball.y
		SPEED_BALL_Y = -SPEED_BALL_Y

	if(ball.y < 0):
		ball.y = 0
		SPEED_BALL_Y = -SPEED_BALL_Y

	if(keyboard.key_pressed("W") and pad_right.y > 0):
		pad_right.y = pad_right.y - SPEED_PAD * window.delta_time()

	if(keyboard.key_pressed("S") and pad_right.y < window.height - pad_right.height):
		pad_right.y = pad_right.y + SPEED_PAD * window.delta_time()

	if(keyboard.key_pressed("UP") and pad_left.y > 0):
		pad_left.y = pad_left.y - SPEED_PAD * window.delta_time()

	if(keyboard.key_pressed("DOWN") and pad_left.y < window.height - pad_left.height):
		pad_left.y = pad_left.y + SPEED_PAD * window.delta_time()

	if(pad_right.collided(ball) or pad_left.collided(ball)):
		SPEED_BALL_X = -SPEED_BALL_X
	
	draw()
	window.update()
