.data
num1: .word   10      
num2: .word   20      
result: .word   0       

.text
lw $t0, 24($t1)     
lw $t1, 12($t2)     
add $t2, $t0, $t1  
sw $t2, 0($zero)     
li $v0, 10
add.d $f0, $f2, $f3
LABEL: add.s $f1, $f2, $f3
add $t0, $s2, $t0
sub $t0, $s2, $t0
and $t0, $s2, $t0
or $t0, $s2, $t0
nor $t0, $s2, $t0
xor $t0, $s2, $t0
addi $t2, $t3, -10
andi $t2, $t3, -10
ori $t2, $t3, -10
xori $t2, $t3, -10
addiu $t1, $t2, 10
addu $t1, $t2, $t3
subu $t1, $t2, $t3
beq $t1, $zero, LABEL
bne $t1, $zero, LABEL
bgez $t1, LABEL
bgezal $t1, LABEL
c.eq.d $f2, $f4
c.eq.s $f0, $f1
clo $t1, $t2
div $t1, $t2
div.d $f2, $f4, $f6
div.s $f0, $f1, $f2
j LABEL
jal LABEL
jalr $t1
jr $t0
lb $t1, 100($t2)
lh $t1, -100($t2)
lhu $t1, -100($t2)
li $t1, 0x101010
lui $t1, 0x010101
lw $t0, 140($s3)
madd $t1, $t2
mfhi $t1
mflo $t1
movn $t1, $t2, $t3
msubu $t1, $t2
mul $t1, $t2, $t5
mul.d $f2, $f4, $f6
mul.s $f1, $f2, $f3
mult $t1, $t2
sb $t4, 1000($t2)
sll $t2, $t3, 10
srl $t2, $t3, 10
slt $t1, $t2, $t3
slti $t1, $t2, -100
sltu $t1, $t2, -100
sra $t2, $t1, 10
srav $t1, $t2, $t3
sub.d $f2, $f4, $f6
sub.s $f0, $f1, $f3
sw $t0, 120($s3)
teq $t1, $t2
tge $t1, $t2
tgei $t1, -100
u $t1, -100
tne $t1, $t2
tnei $t1, -100