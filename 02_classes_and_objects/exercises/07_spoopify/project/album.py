from project.song import Song


class Album:

    def __init__(self, name: str, *songs) -> None:
        self.name = name
        self.published = False
        self.songs = list(songs)

    def add_song(self, song: Song) -> str:
        if self.published:
            return "Cannot add songs. Album is published."
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        if song in self.songs:
            return "Song is already in the album."
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str) -> str:
        if self.published:
            return "Cannot remove songs. Album is published."
        if song := next((s for s in self.songs if s.name == song_name), None):
            self.songs.remove(song)
            return f"Removed song {song.name} from album {self.name}."
        return "Song is not in the album."

    def publish(self) -> str:
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self) -> str:
        info = f"Album {self.name}\n"
        for s in self.songs:
            info += f"== {s.get_info()}\n"
        return info
