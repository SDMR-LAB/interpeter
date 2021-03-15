def block(code):
    opened = []
    blocks = {}
    for i in range(len(code)):
        if code[i] == '[':
            opened.append(i)
        elif code[i] == ']':
            blocks[i] = opened[-1]
            blocks[opened.pop()] = i
    return blocks

def parse(code):
    new = ""
    for c in code:
        if c in "shift_left shift_right plus minus point zapa[]":
            new += c
    return new
