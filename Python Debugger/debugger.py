from pathlib import Path
import os
def bp_ins(filename, start, end):
    """Inserts breakpoints into code"""
    with open(filename, 'r') as f:
        lines = f.readlines()
    lines.insert(start-1, "")
    lines.insert(end+1, "")
    lines.insert(0, "")
    lines[start-1] = 'ipdb.set_trace()\n'
    lines[end+1] = 'ipdb.set_trace()\n'
    lines[0] = "import ipdb\n"
    with open(f"break_{filename}", 'w+') as f:
        f.writelines(lines)


def debug_file_exec(filename):
    """Executes provided file through the console"""
    exec(open(f"break_{filename}").read())

filename = 'text.py'
bp_ins(filename, 2, 66)
exec(open('break_text.py').read())
#os.system("C:/Windows/System32/WindowsPowerShell/v1.0/powershell.exe")


# print('ok')
# print('no')
# print('9')
# print(17)
# print('never')
