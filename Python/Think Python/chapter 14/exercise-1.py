def sed(pattern, repl, file1, file2):
    try:
        in_file = open(file1, 'r')
        out_file = open(file2, 'w')
        for line in in_file:
            out_line = []
            for char in line:
                if char not in pattern:
                    out_line.append(char)
                else:
                    out_line.append=append(repl)
            out_file.write(''.join(out_line))
        out_file.close()
    except as ex:
        ex
        print('Error reading file %s' file1)
        return


