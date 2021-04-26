BINARY_NAME = sl
CC=gcc
CFLAGS=-O -Wall

PACKAGE_DIR = pkg
ART_DIR = share

sl: train_animation.c train_animation.h
	$(CC) $(CFLAGS) -o $(ART_DIR)/0_train_animation train_animation.c -lncurses

.PHONY: run clean test all
clean:
	rm -f share/0_train_animation
	rm -f sl_0.1*

package:
	rm -rf $(PACKAGE_DIR)
	mkdir -p $(PACKAGE_DIR)
	cd sl && dpkg-buildpackage -uc -us
	mv sl_0.1* pkg/

