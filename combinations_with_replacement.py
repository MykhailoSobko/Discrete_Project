from itertools import combinations_with_replacement as itertools_c_w_r
import time


def combinations_with_replacement(r:int, n:int, human_count=False) -> list:
    '''
    returns generator of combinations C(r, n) with repetitions in sorted order
    r - elements in each combination
    n - total length of possible values for each position
    human_count - if True counting starts from 1, else from 0
    >>> list(combinations_with_replacement(0, 0))
    []
    >>> list(combinations_with_replacement(2, 4, True))
    [(1, 1), (1, 2), (1, 3), (1, 4), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4)]
    >>> list(combinations_with_replacement(2, 4, False))
    [(0, 0), (0, 1), (0, 2), (0, 3), (1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]
    >>> list(combinations_with_replacement(2, 1))
    [(0, 0)]
    >>> list(combinations_with_replacement(2, 2))
    [(0, 0), (0, 1), (1, 1)]
    '''
    if n == 0 or r == 0:
        return []
    nums = list(range(1, n+1) if human_count else range(n))

    rec_combo = [nums[0] for _ in range(r)]
    yield tuple(rec_combo)

    while True:
        # step 1
        for i in range(len(rec_combo)-1, -1, -1):
            if rec_combo[i]+1 in nums:

                # step 2
                rec_combo[i] += 1

                yield tuple(rec_combo)
                break

            if i == 0: return

            if not rec_combo[i-1] + 1 in nums:
                continue

            # step 3
            rec_combo[i-1:] = [rec_combo[i-1]+1]*(len(rec_combo)-i+1)

            yield tuple(rec_combo)

            break


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    n, r = 3, 5

    start_time = time.time()
    corr = list(itertools_c_w_r(range(n), r))
    print(time.time()-start_time)


    start_time = time.time()
    mine = list(combinations_with_replacement(r, n))
    print(time.time()-start_time)
    print(corr == mine)

