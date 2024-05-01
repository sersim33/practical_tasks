def sort_films_by_title(films):
    sorted_films = sorted(films.items())
    # for film, year in sorted_films:
    #     film = film.replace("Avengers: ", "")  # Remove "Avengers: " from the film title
    #     print(f"({film}: {year}!)")
    return sorted_films
films = {
    'Lvengers: Endgame': 2019,
    'Wuardians of the Galaxy': 2014,
    'Iron Man': 2008,
    'Ahor': 2011
}

print(sort_films_by_title(films))