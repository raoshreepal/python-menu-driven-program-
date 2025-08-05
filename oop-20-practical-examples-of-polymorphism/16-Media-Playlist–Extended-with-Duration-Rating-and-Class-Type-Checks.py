'''
🔹Scenario: Media player plays a playlist of mixed content, showing type, duration, and rating.
🔹Definition: Polymorphism via play() method; playlist contains different media types.
'''
class Media:
    def __init__(self, title, duration, rating):
        self.title = title
        self.duration = duration
        self.rating = rating

    def play(self):
        raise NotImplementedError("Subclass must implement play()")

class Song(Media):
    def play(self):
        return f"🎵 Playing song: {self.title} ({self.duration} mins, ⭐{self.rating}/5)"

class Movie(Media):
    def play(self):
        return f"🎬 Now showing: {self.title} ({self.duration} mins, ⭐{self.rating}/5)"

class Podcast(Media):
    def play(self):
        return f"🎙️ Listening to podcast: {self.title} ({self.duration} mins, ⭐{self.rating}/5)"

# Playlist with mixed media
playlist = [
    Song("Perfect", 4, 4.7),
    Movie("Inception", 148, 4.9),
    Podcast("Tech Today", 30, 4.4)
]

for i, media in enumerate(playlist, start=1):
    print(f"{i}. {media.play()}")
