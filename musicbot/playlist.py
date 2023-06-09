from collections import deque
import random

from config import config


class Playlist:
    """Сохраняет ссылки YouTube на песни, которые будут воспроизводиться и уже воспроизведены, и предлагает основные операции с очередями"""

    def __init__(self):
        # Stores the links os the songs in queue and the ones already played
        self.playque = deque()
        self.playhistory = deque()

        # A seperate history that remembers the names of the tracks that were played
        self.trackname_history = deque()

        self.loop = False

    def __len__(self):
        return len(self.playque)

    def add_name(self, trackname):
        self.trackname_history.append(trackname)
        if len(self.trackname_history) > config.MAX_TRACKNAME_HISTORY_LENGTH:
            self.trackname_history.popleft()

    def add(self, track):
        self.playque.append(track)

    def next(self):

        if len(self.playque) == 0:
            return None

        song_played = self.playque.popleft()

        if self.loop == True:
            if song_played != "Dummy":
                self.playque.clear()
                self.add(song_played)

        if len(self.playque) == 0:
            return None

        if song_played != "Dummy":
            self.playhistory.append(song_played)
            if len(self.playhistory) > config.MAX_HISTORY_LENGTH:
                self.playhistory.popleft()

        return self.playque[0]

    def prev(self):
        if len(self.playhistory) == 0:
            dummy = "DummySong"
            self.playque.appendleft(dummy)
            return dummy
        self.playque.appendleft(self.playhistory.pop())
        return self.playque[0]

    def shuffle(self):
        random.shuffle(self.playque)

    def empty(self):
        self.playque.clear()
        self.playhistory.clear()
