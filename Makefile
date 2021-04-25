#==========================================
#    Makefile: makefile for sl 5.1
#	Copyright 1993, 1998, 2014
#                 Toyoda Masashi
#		  (mtoyoda@acm.org)
#	Last Modified: 2014/03/31
#==========================================

CC=gcc
CFLAGS=-O -Wall

all: train_animation

train_animation: train_animation.c train_animation.h
	$(CC) $(CFLAGS) -o train_animation train_animation.c -lncurses

clean:
	rm -f train_animation

distclean: clean
