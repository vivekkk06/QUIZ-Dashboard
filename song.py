class playlist:
    def __init__(self, name):
        self.name = name
        self.l = []
    def add_song(self, song):
        return self.l.append(song)
    def total_duration(self):
        total=0
        for i in self.l:
            total += i.duration_sec
        return total
    def __len__(self):
        return len(self.l)

class song(playlist):
    def __init__(self, title, duration_sec):
        self.title = title
        self.duration_sec = duration_sec

pl = playlist('MyFavs')
print(len(pl), pl.total_duration())

s1 = song('Track1', 120)
s2 = song('Track2', 200)
pl = playlist('Mix')
pl.add_song(s1)
pl.add_song(s2)
print(len(pl), pl.total_duration())

pl = playlist('Solo')
pl.add_song(song('A', 60))
print(pl.total_duration())