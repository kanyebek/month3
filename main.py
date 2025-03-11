import flet as ft

def main(page: ft.Page):
    page.title = 'My first app'
    page.theme_mode = ft.ThemeMode.LIGHT
    greeting_text = ft.Text('Hello, world!')

    name_input = ft.TextField(label='Name:', autofocus=True)

    def on_button_click(e):
        name = name_input.value.strip()

        if name:
            greeting_text.value = f'Hello, {name}!'
            greet_button.text = 'Greet again'
            name_input.value = ''
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

    greet_button = ft.ElevatedButton('Greet', on_click=on_button_click)

    page.add(greeting_textft.Row([theme_button], 
            name_input,
            greet_button)
             )
ft.app(target=main)
# ft.app(target=main, view=ft.WEB_BROWSER)
