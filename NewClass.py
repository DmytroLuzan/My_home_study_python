class Point:
    x = 1; y = 1
#     def setCoords(self):
#         print(self.__dict__)
#
#
# pt = Point
# pt.x = 5
# pt.y = 10
# pt.setCoords()

    def setCoords(self, x, y):
        self.x = x
        self.y = y

pt = Point()
pt.setCoords(5, 10)
print(pt.__dict__)




