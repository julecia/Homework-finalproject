import tkinter as tk
import tkinter.ttk as ttk

ects = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

grade = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10]

priority = ['Low', 'Medium', 'High', 'Critical']

percentage = [10, 20, 30, 40, 50, 60, 70, 80, 90]


# get the official hours per credit
def compute_official_hours(ects):
    return ects * 25


# Get the recommended hours based on the parameters given by the user: credits, grade, priority
def compute_recommended_hours(ects, grade, priority):
    hours = []
    hour = ects * 25 + (grade * 3)
    if priority == 0:
        hour *= (2 / 3)
        low_grade = round(hour, 2)
        hours.append(low_grade)
    elif priority == 1:
        hour *= (6 / 7)
        low_grade = round(hour, 2)
        hours.append(low_grade)
    elif priority == 2:
        hour *= (7 / 6)
        low_grade = round(hour, 2)
        hours.append(low_grade)
    elif priority == 3:
        hour *= 6 / 5
        low_grade = round(hour, 2)
        hours.append(low_grade)
    good_grade = round(hour * 1.5, 2)
    hours.append(good_grade)
    excellent_grade = round(hour * 2, 2)
    hours.append(excellent_grade)
    return hours


# Get the hours referred to theory, exercises and test based on the percentages entered by the user.
def compute_percentage_hours(good_grade, theory, exercises, test):
    percentages = []
    percentages.append(round(good_grade * (theory / 100), 2))  # Good grade as reference
    percentages.append(round(good_grade * (exercises / 100), 2))
    percentages.append(round(good_grade * (test / 100), 2))
    return percentages


# constructor

class Studier(tk.Frame):

    def __init__(self):
        # inheritance based on the class model
        super().__init__()

        # Initialize private attributes of the class

        self.label_title = None
        self.label_ects = None
        self.label_grade = None
        self.label_priority = None
        self.label_official = None
        self.label_min = None
        self.label_good = None
        self.label_excellent = None
        self.label_theory = None
        self.label_exercises = None
        self.label_test = None

        self.text_theory = None
        self.text_exercises = None
        self.text_test = None
        self.text_official = None
        self.text_min = None
        self.text_good = None
        self.text_excellent = None

        self.frame_timer = None
        self.frame_subject = None
        self.frame_recommend = None
        self.frame_scheduler = None
        self.frame_theory = None
        self.frame_exercises = None
        self.frame_test = None
        self.frame_results = None

        self.combo_ects = None
        self.combo_grade = None
        self.combo_priority = None
        self.combo_theory = None
        self.combo_exercises = None
        self.combo_test = None

        self.button_hours = None
        self.button_theory = None
        self.button_exercises = None
        self.button_compute = None

        self.str_official = None
        self.str_min = None
        self.str_good = None
        self.str_excellent = None
        self.str_theory = None
        self.str_exercises = None
        self.str_test = None

        self.value_theory = None
        self.value_exercises = None
        self.value_test = None
        self.ects = 0.0
        self.grade = 0.0
        self.priority = 0
        self.hours = []

        self.gui()

    # Get the data from the comboboxes (credits, grade, priority) when press the button.
    def get_subject_data(self):

        self.combo_exercises.config(state='disabled')
        self.button_exercises.config(state='disabled')
        self.combo_test.config(state='disabled')
        self.button_compute.config(state='disabled')

        self.ects = int(self.combo_ects.get())
        self.grade = float(self.combo_grade.get())
        aux = self.combo_priority.get()
        if aux == 'Low':
            self.priority = 0
        elif aux == 'Medium':
            self.priority = 1
        elif aux == 'High':
            self.priority = 2
        elif aux == 'Critical':
            self.priority = 3

        self.str_official.set(str(compute_official_hours(self.ects)) + ' hrs')

        self.hours = compute_recommended_hours(self.ects, self.grade, self.priority)
        self.str_min.set(str(self.hours[0]) + ' hrs')
        self.str_good.set(str(self.hours[1]) + ' hrs')
        self.str_excellent.set(str(self.hours[2]) + ' hrs')

        self.combo_theory.config(state='readonly')
        self.button_theory.config(state='active')

    def set_theory(self):

        self.combo_exercises.config(state='readonly')
        self.button_exercises.config(state='active')
        self.value_theory = int(self.combo_theory.get())
        aux = []

        for p in percentage:
            if (100 - self.value_theory) > p:
                aux.append(p)

        self.combo_exercises.config(values=aux)

        self.combo_theory.config(state='disabled')
        self.button_theory.config(state='disabled')

    # Get percentage when the Set button is pressed.
    def set_exercises(self):

        self.button_compute.config(state='active')
        self.value_exercises = int(self.combo_exercises.get())

        aux = 100 - (self.value_theory + self.value_exercises)
        self.combo_test.config(values=aux)
        self.combo_test.current(0)

        self.combo_exercises.config(state='disabled')
        self.button_exercises.config(state='disabled')

    # Get percentage when the Set button is pressed and call the method for computing the results.
    def compute_percentages(self):
        self.value_test = int(self.combo_test.get())

        percentages = compute_percentage_hours(self.hours[1], self.value_theory, self.value_exercises, self.value_test)
        self.str_theory.set(str(percentages[0]) + ' hrs')
        self.str_exercises.set(str(percentages[1]) + ' hrs')
        self.str_test.set(str(percentages[2]) + ' hrs')

        self.button_compute.config(state='disabled')

        self.combo_theory.config(state='readonly')
        self.button_theory.config(state='active')

    # Create the main window and initial values as title, background color...
    def gui(self):

        self.master.title(" SP ")
        self.config(bg="black")
        self.pack(fill=tk.BOTH, expand=True)
        self.label_title = tk.Label(self, text="SP", font=("Bradley Hand", 25), fg="white", bg="black")
        self.label_title.grid(columnspan=1, sticky=tk.W, pady=(50, 10), padx=(20, 0), column=0, row=0)

        self.frame_timer = tk.LabelFrame(self, text="-> TIMER <-", font=("Bradley Hand", 20), bg="black", borderwidth=0,
                                         fg="white")
        self.frame_timer.grid(columnspan=3, sticky=tk.N, pady=10, padx=(45, 45), column=0, row=1)

        self.frame_subject = tk.LabelFrame(self.frame_timer, text="| Subject |", font=("Bradley Hand", 18), bg="black",
                                           borderwidth=0, fg="white")
        self.frame_subject.grid(columnspan=3, sticky=tk.W, pady=20, padx=20, column=0, row=1)

        self.button_hours = tk.Button(self.frame_subject, text="          Get Estimation          ",
                                      command=self.get_subject_data, font=("Bradley Hand", 14), fg="black")
        self.button_hours.grid(columnspan=2, sticky=tk.W, row=0, column=0, padx=0, pady=15)

        self.label_ects = tk.Label(self.frame_subject, text="-> ECTS (Credits)", font=("Bradley Hand", 16), bg="black",
                                   fg="white")
        self.label_ects.grid(column=1, row=2, sticky=tk.W, padx=1, pady=(20, 6))
        self.combo_ects = ttk.Combobox(self.frame_subject, state='readonly', values=ects, width=4)
        self.combo_ects.current(5)
        self.combo_ects.grid(column=0, row=2, sticky=tk.W, padx=(0, 5), pady=(6, 6))

        self.label_grade = tk.Label(self.frame_subject, text="-> Minimum Grade", font=("Bradley Hand", 16), bg="black",
                                    fg="white")
        self.label_grade.grid(column=1, row=3, sticky=tk.W, padx=1, pady=10)
        self.combo_grade = ttk.Combobox(self.frame_subject, state='readonly', values=grade, width=4)
        self.combo_grade.current(7)
        self.combo_grade.grid(column=0, row=3, sticky=tk.W, padx=(0, 5), pady=(6, 6))

        self.label_priority = tk.Label(self.frame_subject, text="-> Priority Scale", font=("Bradley Hand", 16),
                                       bg="black", fg="white")
        self.label_priority.grid(column=1, row=4, sticky=tk.W, padx=1, pady=10)
        self.combo_priority = ttk.Combobox(self.frame_subject, state='readonly', values=priority, width=8)
        self.combo_priority.current(1)
        self.combo_priority.grid(column=0, row=4, sticky=tk.W, padx=(0, 5), pady=(6, 6))

        self.frame_recommend = tk.LabelFrame(self.frame_timer, text="| Study Time Recommendations |",
                                             font=("Bradley Hand", 18), bg="black",
                                             borderwidth=0, fg="white")
        self.frame_recommend.grid(columnspan=3, sticky=tk.E + tk.N, pady=20, padx=20, column=5, row=1)
        self.label_official = tk.Label(self.frame_recommend, text="-> ECTS official hours", font=("Bradley Hand", 16),
                                       bg="black", fg="white")
        self.label_official.grid(column=1, row=2, sticky=tk.W, padx=1, pady=(20, 10))
        self.str_official = tk.StringVar()
        self.text_official = tk.Entry(self.frame_recommend, width=10, state='disabled', textvariable=self.str_official)
        self.text_official.grid(column=0, row=2, sticky=tk.W, padx=(2, 2), pady=(20, 10))
        self.label_min = tk.Label(self.frame_recommend, text="-> Hours for low grade", font=("Bradley Hand", 16),
                                  fg="white", bg="black")
        self.label_min.grid(column=1, row=3, sticky=tk.W, padx=1, pady=10)
        self.str_min = tk.StringVar()
        self.text_min = tk.Entry(self.frame_recommend, width=10, state='disabled', textvariable=self.str_min)
        self.text_min.grid(column=0, row=3, sticky=tk.W, padx=(2, 2), pady=(0, 10))
        self.label_good = tk.Label(self.frame_recommend, text="-> Hours for good grade", font=("Bradley Hand", 16),
                                   bg="black", fg="white")
        self.label_good.grid(column=1, row=4, sticky=tk.W, padx=1, pady=10)
        self.str_good = tk.StringVar()
        self.text_good = tk.Entry(self.frame_recommend, width=10, state='disabled', textvariable=self.str_good)
        self.text_good.grid(column=0, row=4, sticky=tk.W, padx=(2, 2), pady=(0, 10))
        self.label_excellent = tk.Label(self.frame_recommend, text="-> Hours for excelent grade",
                                        font=("Bradley Hand", 16),
                                        bg="black", fg="white")
        self.label_excellent.grid(column=1, row=5, sticky=tk.E, padx=1, pady=10)
        self.str_excellent = tk.StringVar()
        self.text_excellent = tk.Entry(self.frame_recommend, width=10, state='disabled',
                                       textvariable=self.str_excellent)
        self.text_excellent.grid(column=0, row=5, sticky=tk.W, padx=(2, 2), pady=(0, 10))

        self.frame_scheduler = tk.LabelFrame(self, text="-> SCHEDULER <-", font=("Bradley Hand", 20), borderwidth=0,
                                             fg="white", bg="black")
        self.frame_scheduler.grid(columnspan=3, sticky=tk.N, pady=10, padx=(45, 45), column=0, row=2)

        self.frame_theory = tk.LabelFrame(self.frame_scheduler, text="| Theory |", font=("Bradley Hand", 14),
                                          bg="black", borderwidth=0, fg="white")
        self.frame_theory.grid(columnspan=2, sticky=tk.N, pady=10, padx=(10, 10), column=0, row=1)
        self.combo_theory = ttk.Combobox(self.frame_theory, state='disabled',
                                         values=percentage, width=3)
        self.combo_theory.current(0)
        self.combo_theory.grid(columnspan=2, column=0, row=0, sticky=tk.N, padx=10, pady=(15, 15))
        self.button_theory = tk.Button(self.frame_theory, text="      Set %    ", command=self.set_theory,
                                       state='disabled', font=("Bradley Hand", 12), fg="white")
        self.button_theory.grid(columnspan=2, column=0, row=1, sticky=tk.N, padx=10, pady=5)

        self.frame_exercises = tk.LabelFrame(self.frame_scheduler, text="| Exercises |", font=("Bradley Hand", 14),
                                             bg="black", borderwidth=0, fg="white")
        self.frame_exercises.grid(columnspan=2, sticky=tk.N, pady=10, padx=(10, 10), column=2, row=1)
        self.combo_exercises = ttk.Combobox(self.frame_exercises, state='disabled',
                                            values=percentage, width=3)
        self.combo_exercises.current(0)
        self.combo_exercises.grid(columnspan=2, column=2, row=0, sticky=tk.N, padx=10, pady=(15, 15))
        self.button_exercises = tk.Button(self.frame_exercises, text="      Set %    ", command=self.set_exercises,
                                          state='disabled', font=("Bradley Hand", 12), fg="white")
        self.button_exercises.grid(columnspan=2, column=2, row=1, sticky=tk.N, padx=10, pady=5)

        self.frame_test = tk.LabelFrame(self.frame_scheduler, text="| Test |", font=("Bradley Hand", 14),
                                        borderwidth=0, fg="white", bg="black")
        self.frame_test.grid(columnspan=2, sticky=tk.N, pady=10, padx=(10, 10), column=4, row=1)

        self.combo_test = ttk.Combobox(self.frame_test, state='disabled',
                                       values=percentage, width=3)
        self.combo_test.current(0)
        self.combo_test.grid(columnspan=2, column=4, row=0, sticky=tk.N, padx=10, pady=(15, 15))
        self.button_compute = tk.Button(self.frame_test, text="   Compute   ", command=self.compute_percentages,
                                        state='disabled', font=("Bradley Hand", 12), fg="white")
        self.button_compute.grid(columnspan=2, column=4, row=1, sticky=tk.N, padx=10, pady=5)

        self.frame_results = tk.LabelFrame(self.frame_scheduler, text="| Results for good grade |",
                                           font=("Bradley Hand", 14), bg="black",
                                           borderwidth=0, fg="white")
        self.frame_results.grid(columnspan=2, sticky=tk.E, pady=10, padx=(10, 10), column=6, row=1)

        self.label_theory = tk.Label(self.frame_results, text="-> Hours of Theory", font=("Bradley Hand", 12),
                                     bg="black", fg="white")
        self.label_theory.grid(column=3, row=0, sticky=tk.N, padx=10, pady=10)
        self.str_theory = tk.StringVar()
        self.text_theory = tk.Entry(self.frame_results, width=10, state='disabled', textvariable=self.str_theory)
        self.text_theory.grid(column=3, row=1, sticky=tk.N, padx=10, pady=(0, 10))

        self.label_exercises = tk.Label(self.frame_results, text="-> Hours of Exercises", font=("Bradley Hand", 12),
                                        bg="black", fg="white")
        self.label_exercises.grid(column=4, row=0, sticky=tk.N, padx=10, pady=10)
        self.str_exercises = tk.StringVar()
        self.text_exercises = tk.Entry(self.frame_results, width=10, state='disabled', textvariable=self.str_exercises)
        self.text_exercises.grid(column=4, row=1, sticky=tk.N, padx=10, pady=(0, 10))

        self.label_test = tk.Label(self.frame_results, text="-> Hours of Test", font=("Bradley Hand", 12), bg="black",
                                   fg="white")
        self.label_test.grid(column=5, row=0, sticky=tk.N, padx=10, pady=10)
        self.str_test = tk.StringVar()
        self.text_test = tk.Entry(self.frame_results, width=10, state='disabled', textvariable=self.str_test)
        self.text_test.grid(column=5, row=1, sticky=tk.N, padx=10, pady=(0, 10))


def main_program():
    main = tk.Tk()
    main.rowconfigure(9, {'minsize': 20})
    main.columnconfigure(9, {'minsize': 20})
    main.geometry("1200x900")
    main.resizable(0, 0)
    program = Studier()
    main.mainloop()


if __name__ == '__main__':
    main_program()
