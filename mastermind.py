import random
import itertools

class Game:

    def __init__(self):
        self.simulation = True     # True : Program chooses random answer and tries to get to there in the least possible moves
                                    # False: You tell program the score; This mode helps you solve the mastermind
        self.translation = False    # True: Program translates possibilities into Serbian version (translate dict)
                                    # False: Program prints guesses in their original format (numbers 1-6)
        self.actual = None
        self.translate_dict = {1:'Skocko',
                            2:'Tref',
                            3:'Pik',
                            4:'Herc',
                            5:'Karo',
                            6:'Zvezda'}
        self.fields = [1,2,3,4,5,6]
        

    
    def random_solution(self):
        return random.choice(self.all_solutions())

    def translate_guess(self,guess):
        if not self.translation:
            return guess
        return ', '.join(tuple(self.translate_dict[id] for id in guess))

    def all_solutions(self):
        return [g for g in itertools.product(self.fields,repeat=4)]

    def score(self,guess,actual):

        ans = [0,0]
        actual_list = list(actual)
        guess_list = list(guess)

        for i in range(len(guess_list)-1,-1,-1):
            if actual_list[i] == guess_list[i]:
                del actual_list[i]
                del guess_list[i]
                ans[0] += 1

        for i in range(len(guess_list)-1,-1,-1):
            if guess_list[i] in actual_list:
                del actual_list[actual_list.index(guess_list[i])]
                del guess_list[i]
                ans[1] += 1

        return tuple(ans)

    def minimal_eliminated(self,solution_list,solution):
        result_counter = {}
        for option in solution_list:
            result = self.score(option,solution)
            result_counter.setdefault(result,0)
            result_counter[result] +=1
        
        return len(solution_list) - max(result_counter.values())
            
    def best_move(self,solution_list):
        eliminated_for_solution = dict((self.minimal_eliminated(solution_list,solution),solution) for solution in solution_list)
        max_eliminated = max(eliminated_for_solution.keys())
        return eliminated_for_solution[max_eliminated]

    def filter_matching_result(self,solution_list, guess, result):
        possible_list = []
        for solution in solution_list:
            if self.score(guess, solution) == result:
                possible_list.append(solution)

        return possible_list

    def play(self):
        if self.actual == None and self.simulation:
            self.actual = self.random_solution()
            print(f"We are looking for: {self.actual}\n-----------\nGuesses:")

        self.current_guess = (1,1,2,2)
        print(self.translate_guess(self.current_guess))

        self.solution_list = self.all_solutions()

        self.guesses = 1

        while True:
            
            if self.simulation:
                self.current_score = self.score(self.current_guess,self.actual)
            else:
                self.current_score = input('Input score that you got from previous guess in format red,white pegs (eg. 1,0): ')
                self.current_score = tuple(int(g) for g in self.current_score.split(','))

            if self.current_score == (4,0):
                print(f"{self.guesses} guesses for {self.current_guess}")
                return self.guesses

            self.solution_list = self.filter_matching_result(self.solution_list, self.current_guess, self.current_score)
            

            self.current_guess = self.best_move(self.solution_list)
            print(self.translate_guess(self.current_guess))
            
            self.guesses += 1


if __name__ == '__main__':
    game = Game()
    game.play()