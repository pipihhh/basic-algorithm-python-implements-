class Solution(object):
    def rotate_matrix(self, arr):
        x = len(arr) - 1
        start = 0
        while start <= x:
            self.rotate_edge(arr, [start, start], [x, x])
            start += 1
            x -= 1

    def rotate_edge(self, arr, lu, rd):
        while lu[1] < rd[0]:
            tmp = arr[lu[0]][lu[1]]
            arr[lu[0]][lu[1]] = arr[rd[1]][lu[0]]
            arr[rd[1]][lu[0]] = arr[rd[0]][rd[1]]
            arr[rd[0]][rd[1]] = arr[lu[1]][rd[0]]
            arr[lu[1]][rd[0]] = tmp
            lu[1] += 1
            rd[1] -= 1
        print(arr)


a = Solution()
a.rotate_matrix([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
