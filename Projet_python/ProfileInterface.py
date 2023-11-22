import tkinter
import tkinter.messagebox
import customtkinter

customtkinter.set_appearance_mode(
    "System"
)  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme(
    "blue"
)  # Themes: "blue" (standard), "green", "dark-blue"


class App1(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Profile")
        self.geometry(f"{650}x{380}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        # Changer le nom en haut de la page
        self.label = customtkinter.CTkLabel(
            self.sidebar_frame,
            text="Profile",
            font=customtkinter.CTkFont(size=20, weight="bold"),
        )
        self.label.grid(row=0, column=0, padx=20, pady=(20, 10))
        # Premier bouton ammenant ou profile
        self.Profile_button = customtkinter.CTkButton(
            self.sidebar_frame,
            text="Profile",  # command=
        )
        # caracteristique de boutton
        self.Profile_button.grid(row=1, column=0, padx=20, pady=10)
        # Deuxieme boutton du catalogue
        self.Catalogue_button = customtkinter.CTkButton(
            self.sidebar_frame,
            text="Catalogue",  # command=
        )
        # caracteristique de boutton
        self.Catalogue_button.grid(row=2, column=0, padx=20, pady=10)
        # Troisieme Boutton emprunt
        self.Emprunt_button = customtkinter.CTkButton(
            self.sidebar_frame,
            text="Liste Emprunt",  # command=
        )
        # caracteristique de boutton
        self.Emprunt_button.grid(row=3, column=0, padx=20, pady=10)
        # bouton Deconexion
        self.Deconexion_button = customtkinter.CTkButton(
            self.sidebar_frame,
            text="Deconexion",  # command=
        )
        # caracteristique de boutton
        self.Deconexion_button.grid(row=6, column=0, padx=20, pady=10)


if __name__ == "__main__":
    app = App1()
    app.mainloop()
