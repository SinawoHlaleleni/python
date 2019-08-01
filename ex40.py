from flask import Flask
app = Flask(__name__)


class Song(object):
    @app.route('/')
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So i'll stop right there"])

bulls_on_parade = Song(["Then rally around the family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

return 'Song'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
