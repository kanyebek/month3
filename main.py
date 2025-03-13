import flet as ft
from datetime import datetime
from datetime import time

def main(page: ft.Page):
    page.title = "Моё первое приложение"
    page.theme_mode = ft.ThemeMode.LIGHT
    
    greeting_text = ft.Text("Привет, мир!")


    greeting_history = []

    history_text = ft.Text("История приветствий:", style='bodyMedium')

    

    def on_button_click(e):
        name = name_input.value.strip()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        am6 = datetime.now().replace(hour=6, minute=0, second=0, microsecond=0).strftime("%Y-%m-%d %H:%M:%S")
        pm12 = datetime.now().replace(hour=12, minute=0, second=0, microsecond=0).strftime("%Y-%m-%d %H:%M:%S")
        pm18 = datetime.now().replace(hour=18, minute=0, second=0, microsecond=0).strftime("%Y-%m-%d %H:%M:%S")
        am0 = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0).strftime("%Y-%m-%d %H:%M:%S")
        if name:
            if am6 <= timestamp < pm12:
                greeting_text.value = f"Доброе утро, {name}!"
            elif pm12 <= timestamp < pm18:
                greeting_text.value = f"Добрый день, {name}!"
            elif pm18 <= timestamp < am0:
                greeting_text.value = f"Добрый вечер, {name}!"
            else:
                greeting_text.value = f"Доброй ночи, {name}!"
            greet_button.text = 'Поздороваться снова'
            name_input.value = ''

            greeting_history.append(f"{timestamp}: {name}")
            history_text.value = "История приветствий:\n" + "\n".join(greeting_history)
            
        else:
            greeting_text.value = "Пожалуйста, введите ваше имя!"

        page.update()

    name_input = ft.TextField(label="Введите ваше имя:", autofocus=True, on_submit=on_button_click)

    def clear_history(e):
        greeting_history.clear()
        history_text.value = "История приветствий:"
        page.update()
    
    def toggle_theme(e):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT

        page.update()


    theme_button = ft.IconButton(icon=ft.icons.BRIGHTNESS_6, tooltip="Сменить тему", on_click=toggle_theme)


    clear_button = ft.TextButton("Очистить историю", on_click=clear_history)

    clear_button_icon = ft.IconButton(icon=ft.icons.DELETE, tooltip="Очиститка", on_click=clear_history)


    greet_button = ft.ElevatedButton("Поздороваться", on_click=on_button_click)


    page.add(ft.Row([theme_button, clear_button,
             clear_button_icon], alignment=ft.MainAxisAlignment.CENTER), 
             greeting_text, 
             name_input, 
             greet_button,
             history_text
    )

ft.app(target=main)

# ft.app(target=main, view=ft.WEB_BROWSER)


