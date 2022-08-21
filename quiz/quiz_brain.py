class QuizBrain:

    def __init__(self, question_bank):
        self.question_number = 0
        self.question_list = question_bank
        self.score =0 
    
    def still_has_question(self):
        if self.question_number+1 < len(self.question_list):
            return True
        else:
            return False


    def next_question (self):
        n_question = self.question_list[self.question_number].text
        self.question_number +=1
        ans = input(str(self.question_number) + ":" + n_question + '("True or False"):')
        if ans == self.question_list[self.question_number].answer:
            print("You are correct !!")
            self.score +=1

        else:
            print("Incorrect answer :(")
        
        print("Your score is :" + str(self.score) + "/12")
        print("\n")

       

