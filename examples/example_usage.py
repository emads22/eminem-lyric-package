from eminem_lyric import EminemLyric


def main():
    # Create an instance of the EminemLyric class with a song title
    song_title = "Lose Yourself"
    eminem_lyric = EminemLyric(song_title)

    try:
        # Fetch the formatted lyrics of the song
        lyrics = eminem_lyric.lyric
        print(f"\n\n>> Lyrics for '{song_title}':\n\n{lyrics}\n")

        # Fetch the raw lyrics data (as a dictionary)
        raw_lyrics = eminem_lyric.lyric_raw
        print(f"\n\n>> Raw lyrics data for '{song_title}':\n\n{raw_lyrics}\n\n")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
