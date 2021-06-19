from collections import namedtuple

if __name__ == '__main__':
    print('hi')


def maximum_subsequence(a):
    L = [i.size for i in a]
    I = [[b.index] for b in a]
    I_2 = I[:]
    Item_1 = namedtuple("Item", ["inc_subsequence", "size"])
    items_1 = list()
    for i in range(len(L)):
        # below finds the maximum cost increasing index subsequence up to a given index, if there is no number smaller than itself then max_cis= zero
        max_cis = max((L[j] for j in range(i) if I_2[j] < I_2[i]), default=0)
        # below creates a list of the subsequences up to each index
        I[i] = [*I[L.index(max_cis)], *I[i]] if max_cis != 0 else I[i]
        # below creates a list of the cost of each subsequence
        L[i] = max_cis + L[i]

        items_1.append(Item_1(I[i], L[i]))

    return items_1
