import tkinter
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score = tkinter.Label(text=f"Score: {self.quiz.score}", fg="White", bg=THEME_COLOR)
        self.score.grid(column=1, row=0)

        self.canvas = tkinter.Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125,
                                                     fill=THEME_COLOR,
                                                     width=280,
                                                     text="Question ...",
                                                     font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = tkinter.PhotoImage(file="images/true.png")
        self.true = tkinter.Button(image=true_image,
                                   highlightthickness=0,
                                   command=self.check_true_answer)
        self.true.grid(row=2, column=0)

        false_image = tkinter.PhotoImage(file="images/false.png")
        self.false = tkinter.Button(image=false_image,
                                    highlightthickness=0,
                                    command=self.check_false_answer)
        self.false.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,
                                   text=f"You've reached the end of the quiz with {self.quiz.score} points!")
            self.true.config(state="disabled")
            self.false.config(state="disabled")

    def check_true_answer(self):
        answer = self.quiz.check_answer("True")
        self.give_feedback(answer)

    def check_false_answer(self):
        answer = self.quiz.check_answer("False")
        self.give_feedback(answer)

    def give_feedback(self, is_right):
        if is_right:
            self.score.config(text=f"Score {self.quiz.score}")
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
