def get_top_songs_by_year():
    top_songs = []
    with open("spotify-2023.csv", "r", encoding="latin-1") as file:
        lines = file.readlines()
    print("Primeiras 5 linhas:")
    for line in lines[:5]:
        print(line.strip())
    for year in range(2012, 2023):
        year_songs = []
        for line in lines[1:]:
            if '"' in line or "feat." in line:
                continue
            fields = line.strip().split(",")
            if len(fields) < 10:
                continue
            try:
                rel_year = int(fields[3])
                if rel_year == year:
                    song = [fields[0], fields[1], rel_year, int(fields[8])]
                    year_songs.append(song)
            except (ValueError, IndexError):
                continue
        if year_songs:
            top_songs.append(max(year_songs, key=lambda x: x[3]))
    return top_songs[:10]

result = get_top_songs_by_year()
print("\nMúsicas mais tocadas (2012-2022):")
print(result)