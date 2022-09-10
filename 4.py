def inputs():
    while True:
        try:
            line = input()
            yield line
        except (ValueError, EOFError):
            return


d = dict()
l = [d]
for data in inputs():
    if data == '{':
        l.append(dict())
    elif data == '}':
        del(l[len(l) - 1:len(l)])
    else:
        variable, value = data.split('=')
        try:
            x = int(value)
            l[len(l) - 1][variable] = x
        except ValueError:
            val = None
            for i in range(0, len(l)):
                dct = l[len(l) - i - 1]
                if value in dct:
                    val = dct[value]
                    l[len(l) - 1][variable] = val
                    print(val)
                    break
            if not val:
                l[len(l) - 1][variable] = 0
                print(0)


