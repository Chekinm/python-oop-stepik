# task 3
from math import sqrt

class TrackLine:

    def __init__(self, to_x, to_y, max_speed):
        self.to_x = to_x
        self.to_y = to_y
        self.max_speed = max_speed


class Track:

    def __init__(self, start_x, start_y):

        self.start_x = start_x
        self.start_y = start_y
        self.lines = []
        self.curr_x = start_x
        self.curr_y = start_y
        self.lenght = 0

    def add_track(self, tr):

        if isinstance(tr, TrackLine):
            self.lines.append(tr)
            x, y, speed = tr.to_x, tr.to_y, tr.max_speed
            self.lenght += sqrt((x- self.curr_x) ** 2 + (y - self.curr_y) ** 2)
            self.curr_x, self.curr_y = x, y
        else:
            raise TypeError('track supposed to be an instance of TrackLine class')

    def get_tracks(self):
        return tuple(self.lines)

    def __len__(self):
        return int(self.lenght)

    def __eq__(self, other):
        if isinstance(other, Track):
            return self.lenght == other.lenght
        
    def __gt__(self, other):
        if isinstance(other, Track):
            return self.lenght > other.lenght

track1 = Track(0, 0)
track2 = Track(0, 1)

track1.add_track(TrackLine(2, 4, 100))
track1.add_track(TrackLine(5, -4, 100))

track2.add_track(TrackLine(3, 2, 90))
track2.add_track(TrackLine(10, 8, 90))

res_eq = track1 == track2
