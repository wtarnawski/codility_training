
# https://app.codility.com/programmers/lessons/4-counting_elements/max_counters/

def solution(N, A):
    # our idea is to extract every 'N+1' item of A with index 'index', then:
    #   count highest number of increments of a single counter in every window,
    #       //and as a window we understand A slices like: '0:index_1', 'index_1:index_2'...'index_n-1:index_n'
    #   then remember this value and add it to an 'offset'. This way we extract an information used to produce final
    #   counter list.

    offset = 0
    index_global = 0  # used to generate windows
    for index, a in enumerate(A):
        if a == N + 1:

            _maxi = 0
            # print(f'index_global:   {index_global}')
            # print(f'index:   {index}')
            for _a in A[index_global:index]:
                if _a == N + 1:
                    continue
                _maxi = max(A[index_global:index].count(_a), _maxi)

            # print(f'_maxi:   {_maxi}')
            offset += _maxi
            index_global = index  # index of the next window
    # calculation of final window.
    #   It's much more effective and less memory consuming to do this only for the final window,
    #   than apply this formulae to every window in order to come up with this result.
    counters = [offset] * N
    for a_final in A[index_global:]:
        if a_final == N + 1:
            continue
        counters[a_final - 1] += 1
    return counters


print(solution(5, [3, 4, 4, 6, 1, 4, 4]))
print("expected [3, 2, 2, 4, 2]")
print(solution(5, [3, 4, 4, 6, 1, 4, 4, 6, 2, 2, 1]))
print("expected [5, 6, 4, 4, 4]")
print(solution(5, [6, 6, 6, 6, 6]))
print("expected [0, 0, 0, 0, 0]")
