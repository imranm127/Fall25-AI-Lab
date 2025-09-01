class MovieBudgetAnalyzer:
    def __init__(self):
        # Initial dataset of movies
        self.movies = [
            ("Dangal", 70000000),
            ("Baahubali 2", 250000000),
            ("PK", 85000000),
            ("Kabhi Khushi Kabhie Gham", 55000000),
            ("Sholay", 30000000),
            ("Padmaavat", 215000000),
            ("Sanju", 100000000)
        ]

    def add_movies(self):
        num = int(input("How many movies do you want to add: "))
        for i in range(num):
            name = input("Enter movie name: ")
            budget = int(input("Enter movie budget: "))
            self.movies.append((name, budget))

    def calculate_average_budget(self):
        total_budget = 0
        for movie in self.movies:
            total_budget += movie[1]
        return total_budget / len(self.movies)

    def find_budget(self, average_budget):
        print("Movies with budget higher than average:")
        count = 0
        for movie in self.movies:
            name, budget = movie
            if budget > average_budget:
                print(f"{name} — higher by {budget - average_budget}")
                count += 1
        print("Total movies with budget higher than average:", count)



analyzer = MovieBudgetAnalyzer()
analyzer.add_movies()


average = analyzer.calculate_average_budget()
print("Average Budget:", average)

analyzer.find_budget(average)