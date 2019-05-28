def bp_ins(filename):
    """Inserts breakpoints into code"""
    with open(filename, 'r+') as f:
        lines = f.readlines()
        for line in lines:
            print(line)

bp_ins("text.txt")
