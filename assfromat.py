import re


def fromatass():
    '''
    the.walking.dead.s11e18.repack.1080p.web.h264-cakes
    re ^((?![\u4e00-\u9fa5]).)*$
    '''
    regs = re.compile(r'^Dialogue((?![\u4e00-\u9fa5]).)*$')
    assf = 'the.walking.dead.s11e18.repack.1080p.web.h264-cakes.ass'
    n_lines = []
    with open(file=assf, mode='r', encoding='utf-8') as ass:
        lines = ass.readlines()
        for line in lines:
            match = re.search(regs, line)
            if match != None:
                edx = line.replace('Default', 'Default2')
                n_lines.append(edx)
            else:
                n_lines.append(line)
    with open(file=assf, mode='w', encoding='utf-8') as ass:
        ass.writelines(n_lines)


if __name__ == '__main__':
    fromatass()