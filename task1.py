class Matrix():

    def __init__(self, new_list):
        self.new_list = new_list

    def __str__(self):
        return '\n'.join(map(str, self.new_list))

    def __add__(self, other):
        for i in range(len(self.new_list)):

            for el in range(len(other.new_list[i])):
                self.new_list[i][el] = self.new_list[i][el] + other.new_list[i][el]

        return Matrix.__str__(self)


m = Matrix([[1,2,3], [3,4,5]])
new_m = Matrix([[5,6,7], [7,8,9]])
print(m)
print(new_m)
print(m.__add__(new_m))
