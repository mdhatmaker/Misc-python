import random as rnd


wheel = ['g0', 'b28', 'r9', 'b26', 'r30', 'b11', 'r7', 'b20', 'r32', 'b17', 'r5', 'b22', 'r34', 'b15', 'r3', 'b24', 'r36', 'b13', 'r1',
'g00', 'r27', 'b10', 'r25', 'b29', 'r12', 'b8', 'r19', 'b31', 'r18', 'b6', 'r21', 'b33', 'r16', 'b4', 'r23', 'b35', 'r14', 'b2']

board = [[],[],[]]
board[2] = ['r3', 'b6', 'r9', 'r12', 'b15', 'r18', 'r21', 'b24', 'r27', 'r30', 'b33', 'r36']
board[1] = ['b2', 'r5', 'b8', 'b11', 'r14', 'b17', 'b20', 'r23', 'b26', 'b29', 'r32', 'b35']
board[0] = ['r1', 'b4', 'r7', 'b10', 'b13', 'r16', 'r19', 'b22', 'r25', 'b28', 'b31', 'r34']
# also 'g0' and 'g00'
# 1-18, 19-36
# even, odd
# red, black
# 1st 12, 2nd 12, 3rd 12  (2 to 1)
# 1st column, 2nd column, 3rd column  (2 to 1)

rnd.seed()

for x in range(15):
    i = rnd.randint(0, len(wheel))
    print(wheel[i])

