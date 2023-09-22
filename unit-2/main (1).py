'''Implement a class called player that represent a cricket player. The player class should have a 
method called play() which prints "The player is playing cricket. derive two classes, Batsman and
Bowler, from the player class.  Override the play() method in each derived class to print "The batsman
is batting" and "The bowler is bowking", respectively. Write a     program to create object of both the
batsman and bowler classes and call the play() method for each object.'''


# Define the base class player
class Player:
    def play(self):
        print("The player is playing cricket.")

# Define the derived class Batsman
class Batsman(Player):
    def play(self):
        print("The batsman is batting.")

# Define the derived class bowler
class Bowler(Player):
    def play(self):
        print("The bowler is bowling.")
      
# create object of batsman and bowler classes
batsman = Batsman()
bowler = Bowler()

# call the play() method for each object
batsman.play()
bowler.play()