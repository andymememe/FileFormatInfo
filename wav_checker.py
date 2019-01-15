from util.byte_util import getChar, getLittleByte, getLittleShort, getLittleInt
import sys

filename = sys.argv[1]
file = open('test/{}.wav'.format(filename), 'rb')

riff = []
for i in range(4):
    ptd, _ = getChar(file, i)
    riff.append(ptd)
print(''.join(riff))

ptd, _ = getLittleInt(file, 4)
tss = ptd
print('總區塊大小:', tss)

wave = []
for i in range(4):
    ptd, _ = getChar(file, 8 + i)
    wave.append(ptd)
print(''.join(wave))

fmt = []
for i in range(4):
    ptd, _ = getChar(file, 12 + i)
    fmt.append(ptd)
print(''.join(fmt))

ptd, _ = getLittleShort(file, 22)
print('聲道數量:', ptd)

ptd, _ = getLittleInt(file, 24)
smr = ptd
print('取樣頻率:', smr)

ptd, _ = getLittleInt(file, 28)
brt = ptd
print('位元組率:', brt)

ptd, _ = getLittleShort(file, 34)
print('位元深度:', ptd)
print('取樣頻率 * 位元深度 / 8 = 位元組率:', int((smr * ptd) / 8) == brt)

data = []
for i in range(4):
    ptd, _ = getChar(file, 36 + i)
    data.append(ptd)
print(''.join(data))

ptd, _ = getLittleInt(file, 40)
N = ptd
print('子區塊2大小:', N)
print('子區塊2大小 + 36 = 總區塊大小:', N + 36 == tss)
