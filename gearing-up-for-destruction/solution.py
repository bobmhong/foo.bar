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
    for r in range(MIN_RADIUS, r0max):
        radii = []
        radii.append(r)
        if DEBUG:
            print('radius %s: %s' % (0, radii[0]))
        i = 1
        # interate from peg 1 to last peg
        while i < num_pegs and SOLVED == False:
            lastidx = i - 1
            peg_span = pegs[i] - pegs[lastidx]

            # need at lease a span of 2 between pegs since min gear radius is 1
            if peg_span < 2:
                return ([-1, -1])

            # radius for gear on current peg fills space left by the last gear's radius
            new_radius = peg_span - radii[lastidx]
            if new_radius < MIN_RADIUS:
                if DEBUG:
                    print('radius %s: %s less than minimum' % (i, new_radius))
                # Break out of peg iteration while loop - solution not possible with this initial radius
                break

            radii.append(new_radius)
            if DEBUG:
                print('radius %s: %s' % (i, radii[i]))
            # Check for Valid Solution
            if i == num_pegs - 1:
                if radii[0] == 2 * radii[num_pegs - 1]:
                    SOLVED = True
                    return ([radii[0], 1])
                else:
                    if DEBUG:
                        print('initial radius %s is not a solution' % radii[0])
            i = i + 1
    return([-1, -1])


print(solution([4, 30, 50]))

# Test case - span between peg 1 and 2 not large enough
print(solution([3, 10, 12]))

print(solution([4, 17, 50]))

print(solution([4]))

print(solution([-1, 10, 20]))

print(solution([10, 20, 500000]))
