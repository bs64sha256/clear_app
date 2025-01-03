import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os
import shutil
import pathlib
import platform

def get_browser_paths():
    system = platform.system()
    browser_paths = {}

    if system == "Windows":
        browser_paths["Chrome"] = {
            "cache": os.path.expanduser("~/AppData/Local/Google/Chrome/User Data/Default/Cache"),
            "cookies": os.path.expanduser("~/AppData/Local/Google/Chrome/User Data/Default/Cookies")
        }
        browser_paths["Firefox"] = {
            "cache": os.path.expanduser("~/AppData/Roaming/Mozilla/Firefox/Profiles/*default*/cache2"),
            "cookies": os.path.expanduser("~/AppData/Roaming/Mozilla/Firefox/Profiles/*default*/cookies.sqlite")
        }
    return browser_paths


def clean_data(browser, paths):
    deleted_files = 0

    try:
        if "cache" in paths and os.path.exists(paths["cache"]):
            shutil.rmtree(paths["cache"])
            deleted_files += 1

        if "cookies" in paths and os.path.exists(paths["cookies"]):
            os.remove(paths["cookies"])
            deleted_files += 1

        if deleted_files > 0:
            return f"Удалено данные {browser}: {deleted_files}"
        else:
            return f"Данные {browser} не найдены или удаление невозможно."
    except Exception as e:
        return f"Ошибка при очистке {browser}: {e}"


def clean_cache_and_cookies():

    browser_paths = get_browser_paths()
    result = ""
    for browser, paths in browser_paths.items():
      if browser_var.get() == browser:
        result += clean_data(browser, paths) + "\n"


    if result:
      messagebox.showinfo("Результат", result)
    else:
      messagebox.showinfo("Информация", "Не выбран браузер или браузер не поддерживается.")


root = tk.Tk()
root.title("Очистка кеша и cookie")

browsers = list(get_browser_paths().keys())

browser_var = tk.StringVar(root)
browser_var.set(browsers[0] if browsers else "")
browser_dropdown = ttk.Combobox(root, textvariable=browser_var, values=browsers)
browser_dropdown.pack(pady=10)

clean_button = ttk.Button(root, text="Очистить", command=clean_cache_and_cookies)
clean_button.pack(pady=10)

root.mainloop()

