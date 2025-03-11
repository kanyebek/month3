import flet as ft

def main(page: ft.Page):
    page.title = 'My first app'

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

    greet_button = ft.ElevatedButton('Greet', on_click=on_button_click)

    page.add(greeting_text, name_input, greet_button)
ft.app(target=main)
# ft.app(target=main, view=ft.WEB_BROWSER)
