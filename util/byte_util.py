import struct

def getChar(file, start):
    file.seek(start)
    pt = file.read(1)
    ptd = struct.unpack('c', pt)[0]
    return ptd.decode('utf-8'), start + 1

def getLittleByte(file, start):
    file.seek(start)
    pt = file.read(1)
    ptd = struct.unpack('<B', pt)[0]
    return ptd, start + 1

def getLittleShort(file, start):
    file.seek(start)
    pt = file.read(2)
    ptd = struct.unpack('<H', pt)[0]
    return ptd, start + 2

def getLittleInt(file, start):
    file.seek(start)
    pt = file.read(4)
    ptd = struct.unpack('<I', pt)[0]
    return ptd, start + 4

def getBigByte(file, start):
    file.seek(start)
    pt = file.read(1)
    ptd = struct.unpack('>B', pt)[0]
    return ptd, start + 1

def getBigShort(file, start):
    file.seek(start)
    pt = file.read(2)
    ptd = struct.unpack('>H', pt)[0]
    return ptd, start + 2

def getBigInt(file, start):
    file.seek(start)
    pt = file.read(4)
    ptd = struct.unpack('>I', pt)[0]
    return ptd, start + 4