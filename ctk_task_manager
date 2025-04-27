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
        
    def create_widgets(self):
        self.button_frame = ctk.CTkFrame(self)
        self.button_frame.grid(row=0, column=0, padx=10, pady=10, sticky='n')

        self.task_list = CTkListbox(self, width=250, height=450)
        self.task_list.grid(column=1, row=0, columnspan=2, rowspan=2, padx=10, pady=10, sticky='n')

        self.add_task_button = ctk.CTkButton(self.button_frame, text="Add Task", command=self.add_task)
        self.add_task_button.grid(row=1, column=0, pady=5,sticky='n')

        self.remove_task_button = ctk.CTkButton(self.button_frame, text="Remove Task", command=self.delete_task)
        self.remove_task_button.grid(row=2, column=0,pady=5, sticky='n')
    
    def add_task(self):
        AddTaskWindow(self)

class AddTaskWindow:
    def __init__(self, parent):   
        self.parent = parent

        def optionmenu_callback(choice):
            print("optionmenu dropdown clicked:", choice)

        def task_to_list():
            task_name = self.task_name_textbox.get()
            progress_status = self.task_status_choice.get()
            if task_name:
                self.parent.task_list.insert(END, f"{task_name} - {progress_status}")
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

        self.task_status_choice = ctk.CTkOptionMenu(self.text_frame,values=["Not Started", "In Progress", "Completed"],command=optionmenu_callback,fg_color="white",text_color="black", dropdown_text_color="black",button_color=theme_blue)
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
