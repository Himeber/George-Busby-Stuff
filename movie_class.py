def line():
    return "-----------------------"
class Movie:
    def __init__(self,title,year,director,rating,genre,cast):
        self.genre = genre
        self.director = director
        self.cast = cast
        self.year = year
        self.title = title
        self.rating = rating
    def __str__(self):
        printer = self.title + " - Published " + str(self.year) + " - Rated " + self.rating + "\n" + line() + "\nDirected by " + self.director + "\nCast:"
        for i in self.cast:
            printer += "\n-"
            printer += i
        printer += "\n" + line()
        return printer
movies = [Movie("The Shawshank Redemption", 1994, "Frank Darabont", "R", "Drama", ["Tim Robbins", "Morgan Freeman"]),Movie("Pulp Fiction", 1994, "Quentin Tarantino", "R", "Crime", ["John Travolta", "Uma Thurman", "Samuel L. Jackson"]),Movie("The Godfather", 1972, "Francis Ford Coppola", "R", "Crime", ["Marlon Brando", "Al Pacino", "James Caan"]),Movie("Inception", 2010, "Christopher Nolan", "PG-13", "Sci-Fi", ['Leonardo DiCaprio', 'Joseph Gordon-Levitt', 'Ellen Page']),Movie('The Matrix', (1999), 'Lana Wachowski', 'R', 'Sci-Fi', ['Keanu Reeves', 'Laurence Fishburne', 'Carrie-Anne Moss']),Movie('Forrest Gump', (1994), 'Robert Zemeckis', 'PG-13', 'Drama', ['Tom Hanks', 'Robin Wright', 'Gary Sinise']),Movie('The Dark Knight', (2008), 'Christopher Nolan', 'PG-13', 'Action', ['Christian Bale', 'Heath Ledger', 'Aaron Eckhart']),Movie("Schindler's List", (1993), 'Steven Spielberg', 'R', 'Drama', ['Liam Neeson', 'Ben Kingsley', 'Ralph Fiennes']),Movie('Fight Club', (1999), 'David Fincher', 'R', 'Drama', ['Brad Pitt', 'Edward Norton', 'Helena Bonham Carter']),Movie('Goodfellas', (1990), 'Martin Scorsese', 'R', 'Crime', ['Robert De Niro', 'Ray Liotta', 'Joe Pesci']),Movie('The Silence of the Lambs', (1991), 'Jonathan Demme', 'R', 'Thriller', ['Jodie Foster', 'Anthony Hopkins', 'Scott Glenn']),Movie('Titanic', (1997), 'James Cameron', 'PG-13', 'Romance', ['Leonardo DiCaprio', 'Kate Winslet', 'Billy Zane']),Movie('The Lord of the Rings: The Fellowship of the Ring', (2001), 'Peter Jackson', 'PG-13', 'Fantasy', ['Elijah Wood', 'Ian McKellen', 'Orlando Bloom']),Movie('Gladiator', (2000), 'Ridley Scott', 'R', 'Action', ['Russell Crowe', 'Joaquin Phoenix', 'Connie Nielsen']),Movie('The Green Mile', (1999), 'Frank Darabont', 'R', 'Drama', ['Tom Hanks', 'Michael Clarke Duncan', 'David Morse']),Movie('Saving Private Ryan', (1998), 'Steven Spielberg', 'R', 'War', ['Tom Hanks', 'Matt Damon', 'Tom Sizemore']),Movie('Jurassic Park', (1993), 'Steven Spielberg', 'PG-13', 'Adventure', ['Sam Neill', 'Laura Dern', 'Jeff Goldblum']),Movie('The Departed', (2006), 'Martin Scorsese', 'R', 'Crime', ['Leonardo DiCaprio', 'Matt Damon', 'Jack Nicholson']),Movie('The Lion King', (1994), 'Roger Allers', 'G', 'Animation', ['Matthew Broderick', 'Jeremy Irons', 'James Earl Jones']),Movie('Eternal Sunshine of the Spotless Mind', (2004), 'Michel Gondry', 'R', 'Romance', ['Jim Carrey', 'Kate Winslet', 'Kirsten Dunst']),Movie('Inglourious Basterds', (2009), 'Quentin Tarantino', 'R', 'War', ['Brad Pitt', 'Christoph Waltz', 'Mélanie Laurent']),Movie('The Sixth Sense', (1999), 'M. Night Shyamalan', 'PG-13', 'Thriller', ['Bruce Willis', 'Haley Joel Osment', 'Toni Collette']),Movie('The Usual Suspects', (1995), 'Bryan Singer', 'R', 'Mystery', ['Kevin Spacey', 'Gabriel Byrne', 'Chazz Palminteri']),Movie('Memento', (2000), 'Christopher Nolan', 'R', 'Thriller', ['Guy Pearce', 'Carrie-Anne Moss', 'Joe Pantoliano']),Movie('Braveheart', (1995), 'Mel Gibson', 'R', 'Biography', ['Mel Gibson', 'Sophie Marceau', 'Patrick McGoohan']),Movie('The Terminator', (1984), 'James Cameron', 'R', 'Sci-Fi', ['Arnold Schwarzenegger', 'Linda Hamilton', 'Michael Biehn']),Movie('Back to the Future', (1985), 'Robert Zemeckis', 'PG', 'Adventure', ['Michael J. Fox', 'Christopher Lloyd', 'Lea Thompson']),Movie('Alien', (1979), 'Ridley Scott', 'R', 'Horror', ['Sigourney Weaver', 'Tom Skerritt', 'John Hurt']),Movie('The Truman Show', (1998), 'Peter Weir', 'PG', 'Drama', ['Jim Carrey', 'Laura Linney', 'Noah Emmerich'])]
running = True
while running:
    print("MovieLister1997")
    print(line())
    print("Options:")
    print("V: View list")
    print("A: Sort alphabetically")
    print("C: Sort chronologically")
    print("G: Sort by genre")
    print("T: Search by title")
    print("D: Search by director")
    print("A: Search by cast")
    print("X: Exit")
    print(line())
    action = input("What do you want to do?\n> ")