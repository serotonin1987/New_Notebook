import tkinter as tk
from tkinter import filedialog, messagebox
import random


class NotepadApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Блокнот на ООП")
        self.window.geometry("700x600")

        self.current_file = None
        self.current_theme = "light"
        self.neon_color = "#00ff00"  # по умолчанию зелёный неон

        self.create_widgets()
        self.create_text_area()
        self.apply_theme("light")

        self.window.mainloop()

    def create_widgets(self):
        self.theme_frame = tk.Frame(self.window)
        self.theme_frame.pack(fill='x', pady=5)

        self.light_btn = tk.Button(self.theme_frame, text="Светлая 🌞", command=lambda: self.apply_theme("light"))
        self.light_btn.pack(side='left', padx=5)

        self.dark_btn = tk.Button(self.theme_frame, text="Ночная 🌙", command=lambda: self.apply_theme("dark"))
        self.dark_btn.pack(side='left', padx=5)

        self.neon_green_btn = tk.Button(self.theme_frame, text="Зелёный Неон 🧩", command=lambda: self.apply_theme("neon", "#00ff00"))
        self.neon_green_btn.pack(side='left', padx=5)

        self.neon_red_btn = tk.Button(self.theme_frame, text="Красный Неон 🔴", command=lambda: self.apply_theme("neon", "#ff0000"))
        self.neon_red_btn.pack(side='left', padx=5)

        self.neon_blue_btn = tk.Button(self.theme_frame, text="Синий Неон 🔵", command=lambda: self.apply_theme("neon", "#007bff"))
        self.neon_blue_btn.pack(side='left', padx=5)

        self.neon_cyan_btn = tk.Button(self.theme_frame, text="Голубой Неон 🔷", command=lambda: self.apply_theme("neon", "#00ffff"))
        self.neon_cyan_btn.pack(side='left', padx=5)

        self.file_frame = tk.Frame(self.window)
        self.file_frame.pack(fill='x', pady=5)

        self.new_btn = tk.Button(self.file_frame, text="Новый", width=10, command=self.new_file)
        self.new_btn.pack(side='left', padx=5)

        self.open_btn = tk.Button(self.file_frame, text="Открыть", width=10, command=self.open_file)
        self.open_btn.pack(side='left', padx=5)

        self.save_btn = tk.Button(self.file_frame, text="Сохранить", width=10, command=self.save_file)
        self.save_btn.pack(side='left', padx=5)

        self.exit_btn = tk.Button(self.file_frame, text="Выход", width=10, command=self.exit_app)
        self.exit_btn.pack(side='right', padx=5)

    def create_text_area(self):
        self.text_area = tk.Text(self.window, font=("Consolas", 14), wrap='word')
        self.text_area.pack(expand=True, fill='both', padx=10, pady=10)

    def new_file(self):
        self.text_area.delete(1.0, tk.END)
        self.current_file = None
        self.window.title("Блокнот - Новый файл")

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Текстовые файлы", "*.txt")])
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    self.text_area.delete(1.0, tk.END)
                    content = f.read()
                    self.text_area.insert(tk.END, content)
                    self.current_file = file_path
                    self.window.title(f"Блокнот - {file_path}")
                    if self.current_theme == "neon":
                        self.colorize_text(self.neon_color)
            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось открыть файл:\n{e}")

    def save_file(self):
        content = self.text_area.get("1.0", tk.END)
        if self.current_file:
            try:
                with open(self.current_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                    messagebox.showinfo("Успех", "Файл сохранён!")
            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось сохранить файл:\n{e}")
        else:
            self.save_file_as()

    def save_file_as(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Текстовые файлы", "*.txt")])
        if file_path:
            self.current_file = file_path
            self.save_file()

    def exit_app(self):
        if messagebox.askokcancel("Выход", "Вы действительно хотите выйти?"):
            self.window.destroy()

    def apply_theme(self, theme_name, neon_color=None):
        self.current_theme = theme_name
        self.neon_color = neon_color if neon_color else "#00ff00"  # по умолчанию зелёный

        if theme_name == "light":
            bg, fg, btn_bg = "white", "black", "lightgray"
        elif theme_name == "dark":
            bg, fg, btn_bg = "#121212", "#e0e0e0", "#1f1f1f"
        elif theme_name == "neon":
            bg, fg, btn_bg = "#000000", self.neon_color, "#111111"

        # Обновление внешнего вида
        self.window.config(bg=bg)
        self.text_area.config(bg=bg, fg=fg, insertbackground=fg)

        self.theme_frame.config(bg=bg)
        self.file_frame.config(bg=bg)

        for widget in self.theme_frame.winfo_children() + self.file_frame.winfo_children():
            widget.config(bg=btn_bg, fg=fg, activebackground=bg, activeforeground=fg)

        self.text_area.tag_delete("color")  # убрать старые стили

        if theme_name == "neon":
            self.colorize_text(self.neon_color)

    def colorize_text(self, color):
        content = self.text_area.get("1.0", tk.END)
        self.text_area.delete("1.0", tk.END)

        for i, char in enumerate(content):
            tag = f"color{i}"
            self.text_area.insert(tk.END, char, tag)
            self.text_area.tag_config(tag, foreground=color)


if __name__ == "__main__":
    NotepadApp()