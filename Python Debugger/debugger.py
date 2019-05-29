def bp_ins(filename, line):
    """Inserts breakpoints into code"""
    with open(filename, 'r') as f:
        lines = f.readlines()
    lines.insert(line-1, "")
    lines[line-1] = 'breakpoint()\n'
    with open(f"break_{filename}", 'w+') as f:
        f.writelines(lines)

def debug_file_exec(filename):
    """Executes provided file through the console"""
    exec(open(f"break_{filename}").read())

filename = 'text.py'
bp_ins(filename, 2)
debug_file_exec(filename)



# print('ok')
# print('no')
# print('9')
# print(17)
# print('never')
