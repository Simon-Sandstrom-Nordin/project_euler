from dataclasses import dataclass


@dataclass(frozen=True)
class Song:
    trackid: str
    runtime: str
    artist: str
    songname: str

    def __lt__(self, other):
        return self.songname < other.songname

    def __le__(self, other):
        return self.songname <= other.songname
