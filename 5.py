from computer import compute

p = [int(x) for x in open('inputs/5.txt').readline().split(',')]

# test

print('pos equal to 8')
compute([3,9,8,9,10,9,4,9,99,-1,8])

print('pos less than 8')
compute([3,9,7,9,10,9,4,9,99,-1,8])

print('imm equal to 8')
compute([3,3,1108,-1,8,3,4,3,99])

print('imm less than 8')
compute([3,3,1107,-1,8,3,4,3,99])

print('test pos jump')
compute([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9])
print('test imm jump')
compute([3,3,1105,-1,9,1101,0,0,12,4,12,99,1])

# part 1
#compute(p)
