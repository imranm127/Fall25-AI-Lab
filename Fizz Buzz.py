class FizzBuzz:
    def __init__(self, start, end):
        # constructor to set the starting and ending numbers
        self.start = start
        self.end = end

    def play(self):
    
        i = self.start
        while i <= self.end:
            if i % 3 == 0:
                print("Fizz")
                if i % 5 == 0:
                    print("Buzz")
            elif i % 5 == 0:
                print("Buzz")
            else:
                print(i)

            print() 
            i += 1

game = FizzBuzz(1, 15)
game.play()