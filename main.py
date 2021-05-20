def solve(V, E):
    n = len(V)
    W = []
    H = [0] * n
    t = [0] * n
    V_W = list(range(n))

    E.sort(key=lambda e: e[2])
    E_ = []
    for e in E:
        E_.append(e)

    W.append(0)
    elapsed_time = 0

    while len(W) < n:

        w = 0
        h = 0
        for e in E_:
            if e[0] not in W and e[1] not in W:
                continue
            h = e[2]
            for v in W:
                if H[v] < h:
                    elapsed_time += h - H[v]
                    H[v] = h
            if e[0] not in W:
                w = e[0]
            elif e[1] not in W:
                w = e[1]
            else:
                w = -1

            E_.remove(e)

            if w >= 0:
                t[w] = elapsed_time
                W.append(w)

            break

    return t


def main():
    V = []
    E = []
    T = 0
    n = 0
    m = 0
    case = 0
    edge_counter = 0
    while True:
        line = input()
        if not line or line.isspace():
            continue

        if T < 1:
            T = int(line)
        elif n < 1:
            data = line.split()
            n = int(data[0])
            m = int(data[1])
            V.append(list(range(n)))
            E.append([])
            edge_counter = 0
        else:
            data = line.split()
            v1 = int(data[0])
            v2 = int(data[1])
            h = int(data[2])
            E[case].append([v1 - 1, v2 - 1, h])
            edge_counter += 1

        if n > 0 and edge_counter == m:
            case += 1
            n = 0
            m = 0

        if case >= T:
            break

    for case in range(T):
        t = solve(V[case], E[case])
        print('\nCase #' + str(case + 1) + ':\n')
        print(' '.join([str(i) for i in t]))


if __name__ == '__main__':
    main()
