CC=gcc
CFLAGS=-m32 --static -Wl,--omagic -o tears

all:
	$(CC) $(CFLAGS) tears.c

clean:
	rm tears