# Implement a class called Player that represent a circket Player.The player class should have a method called play() which prints "The player is playing cricket.Derive two classes.Batsman and bowler from the Player class.Overide the play() method in each derived class to print"The batsman is batting" and "The bowler is bowing",respectively.Write a program to create objects pf both the batsman and bowler classes and play() method for each object

class Player:
    def play(self):
        print("The player is playing cricket")

class Batsman(Player):
    def play(self):
        print("The batsman is batting")

class Bowler(Player):
    def play(self):
        print("The bowler is bowling")

# Create objects for the Batsman and Bowler classes
batsman = Batsman()
bowler = Bowler()

# Call the play() method for each object
batsman.play()
bowler.play()