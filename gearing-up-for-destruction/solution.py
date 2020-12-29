def solution(pegs):
    DEBUG = False
    SOLVED = False
    MIN_RADIUS = 1
    num_pegs = len(pegs)

    # validate inputs
    if not 2 <= num_pegs <= 20:
        return [-1, -1]

    if not min(pegs) >= 1 and max(pegs) < 10000:
        return [-1, -1]

    r0max = pegs[1] - pegs[0]

    # vary the initial radius from MIN_RADIUS to max
    for r in range(MIN_RADIUS * 3, r0max * 3):
        radii = []
        radii.append(r)
        if DEBUG:
            print('radius %s: %s/3' % (0, radii[0]))
        i = 1
        # interate from peg 1 to last peg
        while i < num_pegs and SOLVED == False:
            lastidx = i - 1
            peg_span = pegs[i] - pegs[lastidx]

            # need at lease a span of 2 between pegs since min gear radius is 1
            if peg_span < 2:
                return ([-1, -1])

            # radius for gear on current peg fills space left by the last gear's radius
            new_radius = peg_span * 3 - radii[lastidx]
            if new_radius < MIN_RADIUS * 3:
                if DEBUG:
                    print('radius %s: %s/3 less than minimum radius' %
                          (i, new_radius))
                # Break out of peg iteration while loop - solution not possible with this initial radius
                break

            radii.append(new_radius)
            if DEBUG:
                print('radius %s: %s/3' % (i, radii[i]))
            # Check for Valid Solution
            if i == num_pegs - 1:
                if radii[0] == 2 * radii[num_pegs - 1]:
                    SOLVED = True
                    a = radii[0]
                    b = 3
                    if a % 3 == 0:
                        a = a / 3
                        b = 1
                    return ([a, b])
                else:
                    if DEBUG:
                        print('initial radius %s/3 is not a solution' % radii[0])
            i = i + 1
    return([-1, -1])


# pegs = [1, 3]
# print('Pegs: %s Solution: %s' % (pegs, solution(pegs)))

# pegs = [1, 4]
# print('Pegs: %s Solution: %s' % (pegs, solution(pegs)))

# pegs = [1, 5]
# print('Pegs: %s Solution: %s' % (pegs, solution(pegs)))

pegs = [1, 5, 7]
print('Pegs: %s Solution: %s' % (pegs, solution(pegs)))

# pegs = [4, 30, 50]
# print('Pegs: %s Solution: %s' % (pegs, solution(pegs)))

# # # Test case - span between peg 1 and 2 not large enough
# pegs = [3, 10, 12]
# print('Pegs: %s Solution: %s' % (pegs, solution(pegs)))

# pegs = [4, 17, 50]
# print('Pegs: %s Solution: %s' % (pegs, solution(pegs)))

# pegs = [4]
# print('Pegs: %s Solution: %s' % (pegs, solution(pegs)))

# pegs = [-1, 10, 20]
# print('Pegs: %s Solution: %s' % (pegs, solution(pegs)))

# pegs = [10, 20, 500000]
# print('Pegs: %s Solution: %s' % (pegs, solution(pegs)))
