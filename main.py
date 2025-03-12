import flet as ft
import datetime

def main(page: ft.Page):
    page.title = 'My first app'
    page.theme_mode = ft.ThemeMode.LIGHT
    greeting_text = ft.Text('Hello, world!')

    history = []
    history_text = ft.Text('История приветствий:',style='bodyMedium')



    def clear_history(e):
        history.clear()
        history_text.value = 'История приветствий:'
        page.update()

    def on_button_click(e):
        name = name_input.value.strip()
        timemark = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if name:
            greeting_text.value = f'Hello, {name}!'
            greet_button.text = 'Greet again'
            name_input.value = ''
            history.append(f'{timemark}:{name}')
            history_text.value = 'История приветствий:\n' + '\n'.join(history)
        else:
            greeting_text.value = 'Write your name plz'

        page.update()
    
    def toggle_theme(e):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
        page.update()

    theme_button = ft.IconButton(icon=ft.icons.BRIGHTNESS_6, tooltip="Сменить тему", on_click=toggle_theme)

    name_input = ft.TextField(label='Name:', autofocus=True, on_submit=on_button_click)
    greet_button = ft.ElevatedButton('Greet', on_click=on_button_click)
    clear_history_button = ft.TextButton('Clear history', on_click=clear_history)
    clear_history_icon = ft.IconButton(icon=ft.icons.DELETE, on_click=clear_history)


    page.add( ft.Row([theme_button,clear_history_button, clear_history_icon], alignment=ft.MainAxisAlignment.CENTER),
            greeting_text, 
            name_input,
            greet_button, 
            history_text, 
            )
ft.app(target=main)
# ft.app(target=main, view=ft.WEB_BROWSER)
