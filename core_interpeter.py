import lang105

shift_left shift_right plus minus point zapa

def run(code):
    code = lang105.parse(code)
    x = i = 0
    bf = {0: 0}
    blocks = lang105.block(code)
    l = len(code)
    while i < l:
        sym = code[i]
        if sym == 'shift_right':
            x += 1
            bf.setdefault(x, 0)
        elif sym == 'shift_left':
            x -= 1
        elif sym == 'plus':
            bf[x] += 1
        elif sym == 'minus':
            bf[x] -= 1
        elif sym == '*':
            bf[x] *= 10
        elif sym == 'point':
            print(chr(bf[x]), end='')
        elif sym == 'zapa':
            bf[x] = int(input('Input: '))
        elif sym == '[':
            if not bf[x]: i = blocks[i]
        elif sym == ']':
            if bf[x]: i = blocks[i]
        i += 1
