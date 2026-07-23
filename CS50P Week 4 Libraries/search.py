from artwork import get_artworks
from artists import get_artists

def main():
    artist = input("Artist: ")
    artists = get_artists(query=artist, limit=3)
    
    for artist in artists:
        print(f"* {artist}")

if __name__=="__main__":
    main()
