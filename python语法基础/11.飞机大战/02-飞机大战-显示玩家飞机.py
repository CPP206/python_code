import pygame
import time

def main():
	#1.创建窗口
	screen = pygame.display.set_mode((480, 852), 0, 32)

	#2.创建一个背景图片
	background = pygame.image.load(".\\feiji\\fanfan.jpg")

	#3.创建一个飞机图片
	hero = pygame.image.load(".\\feiji\\fanfan.jpg")

	while True:
		screen.blit(background, (0, 0))
		screen.blit(hero, (210, 300))
		pygame.display.update()
		time.sleep(0.01)


if __name__ == "__main__":
	main()