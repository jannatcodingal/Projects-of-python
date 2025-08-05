from tkinter import *
def clear_all():
    principal_field.delete(0, END)
    rate_field.delete(0, END)
    time_field.delete(0, END)
    simple_field.delete(0, END)
    compound_field.delete(0, END)
    principal_field.focus_set()
def calculate_compound_interest():
    principal = float(principal_field.get())
    rate= float(rate_field.get())
    time=int(time_field.get())
    CI= principal * (pow((1 + rate / 100), time))
    compound_field.insert(10, CI)
def calculate_simple_interest():
    principal = float(principal_field.get())
    rate = float(rate_field.get())
    time = int(time_field.get())
    SI = (principal * rate * time) / 100
    simple_field.insert(10, SI)
if __name__ == "__main__":
    root = Tk()
    root.title("Interest Calculator")
    root.geometry("500x500")
    root.config(bg="white")

    principal_label = Label(root, text="Principal Amount:")
    principal_label.pack(pady=5)
    principal_field = Entry(root)
    principal_field.pack(pady=5)

    rate_label = Label(root, text="Rate of Interest:")
    rate_label.pack(pady=5)
    rate_field = Entry(root)
    rate_field.pack(pady=5)

    time_label = Label(root, text="Time (in years):")
    time_label.pack(pady=5)
    time_field = Entry(root)
    time_field.pack(pady=5)
    interest_button = Button(root, text="Calculate Interest",font="Black", fg="blue", command=lambda: [calculate_compound_interest(), calculate_simple_interest()])
    interest_button.pack(pady=10, padx=10)
    compound_label = Label(root, text="Compound Interest:")
    compound_label.pack(pady=5, padx=10)
    compound_field = Entry(root)
    compound_field.pack(pady=5, padx=10)
    simple_label = Label(root, text="Simple Interest:")
    simple_label.pack(pady=5, padx=10)
    simple_field = Entry(root)
    simple_field.pack(pady=5, padx=10)

    clear_button = Button(root, text="Clear All", command=clear_all)
    clear_button.pack(pady=10)

    root.mainloop()