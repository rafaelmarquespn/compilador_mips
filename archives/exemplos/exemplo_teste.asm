.data
a: .word 1, 2, 3

.text 
li $t0, 101010
lw $t1, 0($t0)
lw $t2, 4($t0)
lw $t3, 8($t0)
madd $t2, $t3
clo $t1, $t2
add $t1, $t2, $t3
xor $t4, $t1, $t2
addi $t5, $t4, 10
xori $t6, $t5, 200
addi $t2, $t3, 10
andi $t2, $t3, 10
ori $t2, $t3, 10
xori $t2, $t3, 10
addiu $t1, $t2, 10
addu $t1, $t2, $t3
subu $t1, $t2, $t3
sw $t4, 0($t0)
sw $t5, 4($t0)
sw $t6, 8($t0)