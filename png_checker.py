from util.byte_util import getChar, getBigByte, getBigShort, getBigInt
from util.png_util import ihdr, chrm, gama, iccp
from util.png_util import sbit, text, ztxt, itxt
from util.png_util import phys, time
from util.png_util import otherChunk
import sys

chunk_util = {'ihdr': ihdr, 'chrm': chrm, 'gama': gama, 'iccp': iccp,
              'sbit': sbit, 'text': text, 'ztxt': ztxt, 'itxt': itxt,
              'phys': phys, 'time': time,
              'other': otherChunk}

filename = sys.argv[1]
file = open('test/{}.png'.format(filename), 'rb')
i = 0
color_type = 6

ptd, i = getBigByte(file, i)

file.seek(i)
png = []
for _ in range(3):
    ptd, i = getChar(file, i)
    png.append(ptd)
print(''.join(png))

i = i + 4 # Skip 4-byte symbols

iend_flag = False
while not iend_flag:
    ptd, i = getBigInt(file, i)
    size = ptd
    
    name = []
    for _ in range(4):
        ptd, i = getChar(file, i)
        name.append(ptd)
    name = ''.join(name)
    name_index = name.lower()
    
    print('=== {} ({} Bytes) ==='.format(name, size))    
    if name_index == 'iend':
        i = chunk_util['other'](file, i, size)
        iend_flag = True
    elif name_index == 'ihdr':
        i, color_type = chunk_util['ihdr'](file, i, size)
    elif name_index == 'sbit':
        i = chunk_util['sbit'](file, i, size, color_type)
    else:
        if name_index in chunk_util:
            i = chunk_util[name_index](file, i, size)
        else:
            i = chunk_util['other'](file, i, size)