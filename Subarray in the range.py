class SubArray:

    def function(self, array, a, k):

        for i in range(a, k):
            print(array[i], end = " ")

array = list(map(int, input().split()))
a, k = map(int, input().split())
object = SubArray()
object.function(array, a, k)
