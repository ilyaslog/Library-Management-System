import customtkinter as ctk


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Student Dashboard")
        self.geometry(f"{650}x{380}")

        username_label = ctk.CTkLabel(self, text="Username")
        username_label.pack()

        username_entry = ctk.CTkEntry(self)
        username_entry.pack()

        password_label = ctk.CTkLabel(self, text="Password")
        password_label.pack()

        password_entry = ctk.CTkEntry(self, show="*")
        password_entry.pack()

        login_button = ctk.CTkButton(self, text="Login")
        login_button.pack()


if __name__ == "__main__":
    app = App()
    app.mainloop()
