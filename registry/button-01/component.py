import customtkinter as ctk


class GradientButton(ctk.CTkButton):
    def __init__(self, master, **kwargs):
        super().__init__(master, corner_radius=8, **kwargs)
        # Simplified component logic for mock
