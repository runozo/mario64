all: mario64

mario64: mario64.asm
	64tass --m6502 -Wall mario64.asm -o mario64.prg
	x64 mario64.prg

clean:
	rm *.prg *.tmp