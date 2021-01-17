def answer(filename):
    out_file = open('answer_file', 'w')
    in_file = open(filename, 'r')
    lines = []
    for line in in_file:
        lines.append(line)
    for i in range(len(lines)):
        if (i + 1) % 2 == 0:
            out_file.write(line)
    out_file.close()