######## task 4 ##########

# class MediaPlayer:

#     def open(self, file):
#         setattr(self, 'filename', file)

#     def play(self):
#         print(f'Воспроизведение {self.filename}')


# media1 = MediaPlayer()
# media2 = MediaPlayer()

# media1.open("filemedia1")
# media2.open("filemedia2")

# media1.play()

# media2.play()


###### task 5 ######

# class Graph:
#     LYMIT_Y = [0, 10]

#     def set_data(self, data):
#         self.data = data

#     def draw(self):
#         filtered = filter(
#             lambda x: x >= Graph.LYMIT_Y[0] and x <= Graph.LYMIT_Y[1],
#             self.data,
#             )
#         print(*filtered)


# graph_1 = Graph()

# graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
# graph_1.draw()


# #  task 7

# import sys

# class StreamData:

#     def create(self, fields, lst_values):
#         if len(fields) == len(lst_values):
#             for i in range(len(fields)):
#                 setattr(self, fields[i], lst_values[i])
#             return True
#         else:
#             return False

# class StreamReader:
#     FIELDS = ('id', 'title', 'pages')

#     def readlines(self):
#         lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
#         sd = StreamData()
#         res = sd.create(self.FIELDS, lst_in)
#         return sd, res


# sr = StreamReader()
# data, result = sr.readlines()


# # task 9 

# import sys

# # программу не менять, только добавить два метода
# lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока


# class DataBase:
#     lst_data = []
#     FIELDS = ('id', 'name', 'old', 'salary')

#     def insert(self, data):
#         for line in data:
#             person_data_dict = {field: value for field, value in zip(self.FIELDS, line.split())}
#             DataBase.lst_data.append(person_data_dict)

#     def select(self, a, b):
#         return DataBase.lst_data[a: max(b, len(DataBase.lst_data)) + 1]

# db = DataBase()
# db.insert(lst_in)

# task 10

class Translator:
    def add(self, eng, rus):
        if 'tr' not in self.__dict__:
            self.tr = {}

        self.tr.setdefault(eng, [])
        if rus not in self.tr[eng]:
            self.tr[eng].append(rus)
        
    def remove(self, eng):
        self.tr.setdefault(eng, [])
        self.tr.pop(eng)

    def translate(self, eng):
        # return self.tr[eng]
        return self.tr.get(eng, [])


tr = Translator()

tr.add('tree', 'дерево')
tr.add('car', 'машина')
tr.add('car', 'автомобиль')
tr.add('leaf', 'лист')
tr.add('river', 'река')
tr.add('go', 'идти')
tr.add('go', 'ехать')
tr.add('go', 'ходить')
tr.add('milk', 'молоко')

tr.remove('car')
print(*tr.translate('go'))
print(*tr.translate('go11'))
