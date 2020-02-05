CC = gcc

default: libfunction.a

libfunction.a: function.o
	ar rcs $@ $^
    
function.o: function.c function.h
	$(CC) -c $<

clean:
	rm *.o *.a
