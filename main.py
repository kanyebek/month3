import flet as ft
from datetime import datetime

def main(page: ft.Page):
    page.title = "Моё первое приложение"
    page.theme_mode = ft.ThemeMode.LIGHT
    

    greeting_text = ft.Text(
        "Привет, мир!",
        size=20,
        width=ft.FontWeight.BOLD,
        opacity=0,
        animate_opacity=ft.Animation(600, 'ease_in_out'),
        animate_scale=ft.Animation(500, 'bounce_out'),
        text_align=ft.TextAlign.CENTER
        )
    

    greeting_history = []

    history_text = ft.Text(
        "История приветствий:", 
        style='bodyMedium',
        animate_opacity=ft.Animation(700, 'ease_in_out'),
    )

    def on_button_click(e):
        name = name_input.value.strip()
        timestamp = datetime.now()
        current_hour = timestamp.hour
        
        if name:
            if 6 <= current_hour < 12:
                greeting_text.value = f"Доброе утро, {name}!"
                greeting_text.color = ft.colors.YELLOW
                greet_button.bgcolor = ft.colors.YELLOW
            elif 12 <= current_hour < 18:
                greeting_text.value = f"Добрый день, {name}!"
                greeting_text.color = ft.colors.ORANGE
                greet_button.bgcolor = ft.colors.ORANGE
            elif 18 <= current_hour < 24:
                greeting_text.value = f"Добрый вечер, {name}!"
                greeting_text.color = ft.colors.RED
                greet_button.bgcolor = ft.colors.RED
            else:
                greeting_text.value = f"Доброй ночи, {name}!"
                greeting_text.color = ft.colors.BLUE
                greet_button.bgcolor = ft.colors.BLUE
                
            greet_button.text = 'Поздороваться снова'
            greeting_text.scale = 1.1
            greeting_text.opacity = 1
            

            name_input.value = ''

            greeting_history.append(f"{timestamp.strftime('%Y-%m-%d %H:%M:%S')}: {name}")
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

    clear_button_icon = ft.IconButton(icon=ft.icons.DELETE, tooltip="Очистить", on_click=clear_history)

    greet_button = ft.ElevatedButton("Поздороваться", on_click=on_button_click)


    page.add(ft.Row([theme_button, clear_button,
             clear_button_icon], alignment=ft.MainAxisAlignment.CENTER), 
             greeting_text, 
             name_input, 
             greet_button,
             history_text
    )

ft.app(target=main)
