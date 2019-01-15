from util.byte_util import getChar, getBigByte, getBigShort, getBigInt

def ihdr(file, start, size):
    i = start
    
    ptd, i = getBigInt(file, i)
    print('寬度:', ptd)

    ptd, i = getBigInt(file, i)
    print('長度:', ptd)

    ptd, i = getBigByte(file, i)
    print('位元深度:', ptd)

    color_type = {0: '灰階', 2: '真彩', 3: '索引色', 4: '帶alpha灰階', 
                  6: '帶alpha真彩'}
    ptd, i = getBigByte(file, i)
    clr_type = ptd
    print('顏色種類:', color_type[clr_type], '({})'.format(clr_type))
    
    i = i + 2 # Skip 2 1-byte parameters

    il_type = {0: '無', 1: 'Adam7'}
    ptd, i = getBigByte(file, i)
    print('格行掃描方法:', il_type[ptd], '({})'.format(ptd))
    i = i + 4 # Skip 4-byte CRC
    return i, clr_type

def chrm(file, start):
    i = start

    ptd, i = getBigInt(file, i)
    print('白點 X:', ptd)

    ptd, i = getBigInt(file, i)
    print('白點 Y:', ptd)

    ptd, i = getBigInt(file, i)
    print('紅 X:', ptd)

    ptd, i = getBigInt(file, i)
    print('紅 Y:', ptd)

    ptd, i = getBigInt(file, i)
    print('綠 X:', ptd)

    ptd, i = getBigInt(file, i)
    print('綠 Y:', ptd)

    ptd, i = getBigInt(file, i)
    print('藍 X:', ptd)

    ptd, i = getBigInt(file, i)
    print('藍 Y:', ptd)
    
    i = i + 4 # Skip 4-byte CRC
    
    return i

def gama(file, start, size):
    i = start
    
    ptd, i = getBigInt(file, i)
    print('Gamma:', ptd)
    
    i = i + 4 # Skip 4-byte CRC
    
    return i

def iccp(file, start, size):
    i = start
    ptd = '0'
    profile = []
    
    while not ptd == '\0':
        ptd, i = getChar(file, i)
        profile.append(ptd)
    print('Profile:', ''.join(profile))

    return start + size + 4

def sbit(file, start, size, clr_type):
    i = start
    
    if clr_type == 0:
        ptd, i = getBigByte(file, i)
        print('最高灰階有效位:', ptd)
    elif clr_type == 2 or clr_type == 3:
        ptd, i = getBigByte(file, i)
        print('最高紅色有效位:', ptd)
        
        ptd, i = getBigByte(file, i)
        print('最高綠色有效位:', ptd)
        
        ptd, i = getBigByte(file, i)
        print('最高藍色有效位:', ptd)
    elif clr_type == 4:
        ptd, i = getBigByte(file, i)
        print('最高灰階有效位:', ptd)
        
        ptd, i = getBigByte(file, i)
        print('最高alpha有效位:', ptd)
    elif clr_type == 6:
        ptd, i = getBigByte(file, i)
        print('最高紅色有效位:', ptd)
        
        ptd, i = getBigByte(file, i)
        print('最高綠色有效位:', ptd)
        
        ptd, i = getBigByte(file, i)
        print('最高藍色有效位:', ptd)
        
        ptd, i = getBigByte(file, i)
        print('最高alpha有效位:', ptd)
    
    return start + size + 4

def text(file, start, size):
    i = start
    keyword = []
    text = []
    
    while not ptd == '\0':
        ptd, i = getChar(file, i)
        keyword.append(ptd)
    keyword = ''.join(keyword)
    
    while not i == start + size + 4:
        ptd, i = getChar(file, i)
        text.append(ptd)
    text = ''.join(text)
    print(keyword + ':', text)
    
    return start + size + 4

def ztxt(file, start, size):
    i = start
    keyword = []
    text = []
    
    while not ptd == '\0':
        ptd, i = getChar(file, i)
        keyword.append(ptd)
    keyword = ''.join(keyword)
    print('關鍵字:', keyword)
    
    return start + size + 4

def itxt(file, start, size):
    i = start
    keyword = []
    lang = []
    
    while not ptd == '\0':
        ptd, i = getChar(file, i)
        keyword.append(ptd)
    keyword = ''.join(keyword)
    print('關鍵字:', keyword)
    
    i = i + 2 # Skip 2-byte parameter
    
    while not ptd == '\0':
        ptd, i = getChar(file, i)
        lang.append(ptd)
    lang = ''.join(lang)
    print('語言:', lang)
    
    return start + size + 4

def phys(file, start, size):
    i = start
    
    ptd, i = getBigInt(file, i)
    print('X軸每單位像素數:', ptd)
    
    ptd, i = getBigInt(file, i)
    print('Y軸每單位像素數:', ptd)
    
    unit_type = {0: '未知(長寬比)', 1: '公制'}
    ptd, i = getBigByte(file, i)
    print('單位:', unit_type[ptd], '({})'.format(ptd))
    
    i = i + 4 # Skip 4-byte CRC
    
    return i

def time(file, start, size):
    i = start
    
    year, i = getBigShort(file, i)
    month, i = getBigByte(file, i)
    day, i = getBigByte(file, i)
    hour, i = getBigByte(file, i)
    minute, i = getBigByte(file, i)
    second, i = getBigByte(file, i)
    print('時間:',
          '{}-{}-{} {}:{}:{}'.format(year, month, day, hour, minute, second))
    
    i = i + 4 # Skip 4-byte CRC
    
    return i

def otherChunk(file, start, size):
    return start + size + 4