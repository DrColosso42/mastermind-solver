## Mastermind solver

Mastermind solver program based on Donald Knuth's algorithm with
the exception of checking for guess only in the set of left possible 
in contrast of Knuth's all guess checking algorithm. This is due
performance reasons, but it does affect the success rate of the program.
Algorithm is supposed to finish every single game in 5 or less guesses,
however with this slight change it guesses in 5 or less in about 95% cases,
rest 5% is 6 guesses (6 is enough to secure victory in every game).

### How to use

There is one important variable (simulation variable) in the initializator of the Game class. First you choose
if you want the program to do the simulation where it assigns itself random solution and tries
to get to it in the least possible number of guesses. The other mode is made for 
you to actually win Mastermind game. In this mode script tells you which combination to guess
and it gives you next guess based on the score you recive.