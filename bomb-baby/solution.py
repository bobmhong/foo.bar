DEBUG = True

# given an input arsenal {m: int, f: int}, generate a list of all distinct
# arsenals that could be made


def generate(arsenal, orig_arsenals):
    arsenals = list(orig_arsenals)
    m = arsenal['m']
    f = arsenal['f']

    mgen = {'m': m + f, 'f': f}
    if not mgen in arsenals:
        arsenals.append(mgen)
        if DEBUG:
            print('generated arsenal %s' % mgen)
    fgen = {'m': m, 'f': m + f}
    if not fgen in arsenals:
        arsenals.append(fgen)
        if DEBUG:
            print('generated arsenal %s' % fgen)

    return(arsenals)


def solution(m, f):

    mgoal = int(m)
    fgoal = int(f)

    goal = {'m': mgoal, 'f': fgoal}
    print('Goal: %s' % goal)

    # Initial Arsenal
    arsenal = {'m': 1, 'f': 1}

    # List of possible arsenals after n generation cycles
    n = 0
    arsenals = []
    arsenals.append(arsenal)

    FOUND = False
    while not FOUND and n < 100:
        if goal in arsenals:
            return(str(n))
        n = n + 1
        if DEBUG:
            print('** Cycle %s ** ' % n)
        new_arsenals = []
        for a in arsenals:
            generated = generate(a, new_arsenals)
            new_arsenals.extend(generated)
        min_m = min(map(lambda a: a['m'], new_arsenals))
        min_f = min(map(lambda a: a['f'], new_arsenals))

        if min_m > goal['m'] or min_f > goal['f']:
            return ('impossible')

        arsenals = new_arsenals


if DEBUG:
    # m = 1
    # f = 2
    # print('Solving for M:%s F:%s Solution: %s' % (m, f, solution(m, f)))

    m = 4
    f = 7
    print('Solving for M:%s F:%s Solution: %s' % (m, f, solution(m, f)))
