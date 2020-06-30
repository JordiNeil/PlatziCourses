# -*- coding:utf-8 -*-
import turtle 

def main():
	window = turtle.Screen()
	dave = turtle.Turtle()

	make_square(dave)

def make_square(dave):
	len = int(input("Tamaño cuadrado"))

	for i in range(4):
		make_line_and_turn(dave, len)
	

def make_line_and_turn(dave, length):
	dave.forward(length)
	dave.left(90)

if __name__ == '__main__':
	main()
	input()