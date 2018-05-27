;
; mario bros clone for c64
; author: Cesare Ghirelli
; 
;
; KEYBOARD & SCREEN
;

CLEAR   =$E544		; clear screen
SCNKEY 	=$ff9f		; see key pressed
GETIN	=$ffe4		; read key value
CHROUT	=$ffd2		; print char to screen
;  PETSCII codes (https://www.c64-wiki.com/wiki/PETSCII)
CRSUP	=#145
CRSRIGH	=#29
CSRDOWN	=#17
CSRLEFT	=#157

;
; SPRITES
;

SP0 	=$7F8		; sprite 0 pointer
SP0COL 	=$d027		; sprite 0 color
SP0X	=$d000		; sprite 0 x pos
SP0Y	=$d001		; sprite 0 y pos
ENABLE  =$d015

*=$0801 ; sys 2061 (runs automatically)
sysline:
	.byte $0b,$08,$01,$00,$9e,$32,$30,$36,$31,$00,$00,$00

*=$080d ; sys2061

start:	jsr CLEAR	; clear screen
		lda #$80	; sprite block #$80 ($80 * 64 bytes($40) = $2000)
		sta SP0 	;
		lda #$04	; set sprite color
		sta SP0COL 
		lda #$01
		sta ENABLE
		lda #$F0	; sprite position
		sta SP0X
		sta SP0Y

readk:	jsr SCNKEY	; keys handling
		jsr GETIN	; read key in accumulator
		beq	readk	; continue if 0
		jsr CHROUT	; print accu
		cmp CRSUP
		beq up
		cmp	CRSRIGH
		beq right
		cmp CSRDOWN
		beq down
		cmp CSRLEFT
		beq left
		jmp readk
up:		dec	SP0Y
		jmp readk
right:	inc SP0X
		jmp readk
down:	inc SP0Y
		jmp readk
left:	dec SP0X
		jmp readk
		rts

; sprite 0 data

*=$2000
	.binary "data/sprite1.spr"