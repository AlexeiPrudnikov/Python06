def RLEcoding(text):
    stat = []
    for i in text:
        if (len(stat) == 0):
            stat.append([1, i])
        else:
            if stat[len(stat) - 1][1] == i:
                stat[len(stat) - 1][0] += 1
            else:
                stat.append([1, i])
    rleResult = ''
    for i in stat:
        rleResult += ''.join(map(str, i))
    return rleResult
def RLEencoding(text):
    count = ''
    result = ''
    for i in text:
        if 48 <= ord(i) <= 57:
            count += i
        else:
            for z in range(int(count)):
                result += i
            count = ''
    return result
file = open('text.txt', 'r')
line = file.read()
file.close()
coding = RLEcoding(line)
file = open('rle_coding.txt', 'w')
file.write(coding)
file.close()
file = open('rle_coding.txt', 'r')
code = file.read()
file.close()
file = open('rle_encoding.txt', 'w')
file.write(RLEencoding(code))
file.close()


