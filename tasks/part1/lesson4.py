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

class Graph:
    LYMIT_Y = [0, 10]

    def set_data(self, data):
        self.data = data

    def draw(self):
        filtered = filter(
            lambda x: x >= Graph.LYMIT_Y[0] and x <= Graph.LYMIT_Y[1],
            self.data,
            )
        print(*filtered)


graph_1 = Graph()

graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
graph_1.draw()
