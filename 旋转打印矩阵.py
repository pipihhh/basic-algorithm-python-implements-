class Solution(object):
    def __init__(self):
        pass

    def print_matrix(self, arr):
        x = len(arr) - 1
        y = len(arr[0]) - 1
        ru = [0, y]
        ld = [x, 0]
        while ru[0] <= ld[0] and ru[1] >= ld[1]:
            print(ru, ld)
            self.print_edge(arr, ru, ld)
            ru[0] += 1
            ru[1] -= 1
            ld[0] -= 1
            ld[1] += 1

    def print_edge(self, arr, ru, ld):
        if ru[0] == ld[0]:
            for i in range(ld[1], ru[1]+1):
                print(arr[ru[0]][i])
            return
        if ru[1] == ld[1]:
            for i in range(ru[0], ld[0]+1):
                print(arr[i][ru[1]])
            return
        for i in range(ru[1]):
            print(arr[ru[0]][i])

        for i in range(ld[0]):
            print(arr[i][ru[1]])

        i = ru[1]
        while i:
            print(arr[ld[0]][i])
            i -= 1

        i = ld[0]
        while i:
            print(arr[i][ld[1]])
            i -= 1


a = Solution()
# a.print_edge([[1,],[2,],[3,]], (0, 0), (2, 0))
a.print_matrix([[1,2,3,4],[4,5,6,7],[8,9,10,11]])
