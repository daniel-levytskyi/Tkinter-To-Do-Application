import customtkinter as ctk
from CTkListbox import *
from tkinter import END

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class ToDoApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("To-Do List Application")
        self.geometry("465x500")
    
        self.create_widgets()
    
    def delete_task(self):
        selection = self.task_list.get()
        if selection:
            self.task_list.delete(self.task_list.curselection())

    def edit_task(self):
        index = self.task_list.curselection()
        if index is not None:
            task_text = self.task_list.get(index)
            EditTaskWindow(self, task_index=index, task_text=task_text)
        
    def save_tasks_to_file(self):
        with open("/home/levytskyi/Documents/Python/Tkinter/CustomTkinter/cTK Task Manager/tasks.txt","w") as file:
            for i in range(self.task_list.size()):
                tasks = self.task_list.get(i)
                file.write(tasks + "\n")
            self.save_text.configure(text="Tasks have been saved.")

    def load_tasks_from_file(self):
        try:
            with open("/home/levytskyi/Documents/Python/Tkinter/CustomTkinter/cTK Task Manager/tasks.txt", "r") as file:
                for line in file:
                    self.task_list.insert(END, line.strip())
        except FileNotFoundError:
            pass


    def create_widgets(self):
        self.button_frame = ctk.CTkFrame(self)
        self.button_frame.grid(row=0, column=0, padx=10, pady=10, sticky='n')

        self.task_list = CTkListbox(self, width=250, height=450)
        self.task_list.grid(column=1, row=0, columnspan=2, rowspan=2, padx=10, pady=10, sticky='n')

        self.add_task_button = ctk.CTkButton(self.button_frame, text="Add Task", command=self.add_task)
        self.add_task_button.grid(row=1, column=0, pady=5,sticky='n')

        self.edit_task_button = ctk.CTkButton(self.button_frame, text="Edit Task", command=self.edit_task)
        self.edit_task_button.grid(row=2, column=0, pady=5, sticky='n')

        self.remove_task_button = ctk.CTkButton(self.button_frame, text="Remove Task", command=self.delete_task)
        self.remove_task_button.grid(row=3, column=0,pady=5, sticky='n')

        self.save_tasks_button = ctk.CTkButton(self.button_frame, text="Save Tasks", command=self.save_tasks_to_file)
        self.save_tasks_button.grid(row=4, pady=5, sticky='s')

        self.exit_button = ctk.CTkButton(self.button_frame, text="Exit", command=self.destroy)
        self.exit_button.grid(row=5, pady=5, sticky='s')

        self.save_text = ctk.CTkLabel(self.button_frame, text="")
        self.save_text.grid(row=6, pady=5, sticky='n')

        self.load_tasks_from_file()
        
    def add_task(self):
        AddTaskWindow(self)

class EditTaskWindow:
    def __init__(self, parent, task_index=None, task_text=None):   
        self.parent = parent
        self.task_index = task_index

        def task_to_list():
            task_name = self.task_name_textbox.get()
            progress_status = self.task_status_choice.get()
            new_text = f"{task_name} - {progress_status}"
            if task_name:
                if task_index is not None:
                    self.parent.task_list.delete(self.task_index)
                    self.parent.task_list.insert(self.task_index, new_text)
                else:
                    self.parent.task_list.insert(END, new_text)
                self.task_window.destroy()

        self.task_window = ctk.CTkToplevel(parent)
        self.task_window.title("Edit Task")
        self.task_window.geometry("400x155")

        self.task_window.grid_columnconfigure(0, weight=1)

        self.text_frame = ctk.CTkFrame(self.task_window)
        self.text_frame.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

        self.text_frame.grid_columnconfigure(1, weight=1)

        self.task_text = ctk.CTkLabel(self.text_frame, text="Task name: ")
        self.task_text.grid(row=1, column=0, pady=5, padx=5, sticky='e')

        self.task_name_textbox = ctk.CTkEntry(self.text_frame)
        self.task_name_textbox.grid(row=1, column=1, pady=5, padx=5, sticky='ew')

        self.task_status_text = ctk.CTkLabel(self.text_frame, text="Task status: ")
        self.task_status_text.grid(row=2, column=0, pady=5, padx=5, sticky='n')

        theme_blue = ctk.ThemeManager.theme["CTkButton"]["fg_color"] 

        self.task_status_choice = ctk.CTkOptionMenu(self.text_frame,values=["Not Started", "In Progress", "Completed"],fg_color="white",text_color="black", dropdown_text_color="black",button_color=theme_blue)
        self.task_status_choice.grid(row=2, column=1, pady=5, padx=5, sticky='ew')

        if task_text:
            if " - " in task_text:
                name, status = task_text.split(" - ", 1)
                self.task_name_textbox.insert(0, name)
                self.task_status_choice.set(status)


        self.button_frame = ctk.CTkFrame(self.task_window, fg_color="transparent")
        self.button_frame.grid(row=2, column=0, padx=10, pady=10, sticky='nsew')
        self.button_frame.grid_columnconfigure(0, weight=1)
        self.button_frame.grid_columnconfigure(1, weight=1)
        self.button_frame.grid_columnconfigure(2, weight=1)
        self.button_frame.grid_columnconfigure(3, weight=1)

        self.task_complete_button = ctk.CTkButton(self.button_frame, text="Save Changes", command=task_to_list)
        self.task_complete_button.grid(row=0, column=1, pady=1, padx=1, sticky='s')

        self.task_cancel_button = ctk.CTkButton(self.button_frame, text="Cancel", command=self.task_window.destroy)
        self.task_cancel_button.grid(row=0, column=2, pady=1, padx=1, sticky='s')

class AddTaskWindow:
    def __init__(self, parent):   
        self.parent = parent

        def task_to_list():
            task_name = self.task_name_textbox.get()
            progress_status = self.task_status_choice.get()
            new_text = f"{task_name} - {progress_status}"
            if task_name:
                self.parent.task_list.insert(END, new_text)
                self.task_window.destroy()

        self.task_window = ctk.CTkToplevel(parent)
        self.task_window.title("Add a Task")
        self.task_window.geometry("400x155")

        self.task_window.grid_columnconfigure(0, weight=1)

        self.text_frame = ctk.CTkFrame(self.task_window)
        self.text_frame.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

        self.text_frame.grid_columnconfigure(1, weight=1)

        self.task_text = ctk.CTkLabel(self.text_frame, text="Task name: ")
        self.task_text.grid(row=1, column=0, pady=5, padx=5, sticky='e')

        self.task_name_textbox = ctk.CTkEntry(self.text_frame)
        self.task_name_textbox.grid(row=1, column=1, pady=5, padx=5, sticky='ew')

        self.task_status_text = ctk.CTkLabel(self.text_frame, text="Task status: ")
        self.task_status_text.grid(row=2, column=0, pady=5, padx=5, sticky='n')

        theme_blue = ctk.ThemeManager.theme["CTkButton"]["fg_color"] 

        self.task_status_choice = ctk.CTkOptionMenu(self.text_frame,values=["Not Started", "In Progress", "Completed"],fg_color="white",text_color="black", dropdown_text_color="black",button_color=theme_blue)
        self.task_status_choice.grid(row=2, column=1, pady=5, padx=5, sticky='ew')

        self.button_frame = ctk.CTkFrame(self.task_window, fg_color="transparent")
        self.button_frame.grid(row=2, column=0, padx=10, pady=10, sticky='nsew')
        self.button_frame.grid_columnconfigure(0, weight=1)
        self.button_frame.grid_columnconfigure(1, weight=1)
        self.button_frame.grid_columnconfigure(2, weight=1)
        self.button_frame.grid_columnconfigure(3, weight=1)

        self.task_complete_button = ctk.CTkButton(self.button_frame, text="Add Task", command=task_to_list)
        self.task_complete_button.grid(row=0, column=1, pady=1, padx=1, sticky='s')

        self.task_cancel_button = ctk.CTkButton(self.button_frame, text="Cancel", command=self.task_window.destroy)
        self.task_cancel_button.grid(row=0, column=2, pady=1, padx=1, sticky='s')

if __name__ == "__main__":
    root = ToDoApp()
    root.mainloop()
