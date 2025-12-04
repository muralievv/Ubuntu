# import flet as ft
# def main(page: ft.Page):
#     page.title = 'Moe pervoe prilojenie'
#     page.theme_mode = ft.ThemeMode.LIGHT
#     greeting_text = ft.Text(value='Hello world', color=ft.Colors.RED)
#     # greeting_text.value = 'Privet mir'
#     # greeting_text.color = ft.Colors.GREEN
#     def on_button_click(_):
#          print(name_input.value)
#          name = name_input.value
#          greeting_text.value = f'Hello {name}'
#          print(greeting_text)
#          page.update()
#     name_input = ft.TextField(label='Vvedite imya', on_submit=on_button_click)

#     page.add(greeting_text, name_input)
# ft.app(target=main)
# from datetime import date
# from flet import Text, TextField

import flet as ft

def main(page: ft.Page):
    page.title = 'Мое первое приложение'
    page.theme_mode = ft.ThemeMode.LIGHT
    greeting_text = ft.Text(value='Hello world')

    # greeting_text.value = 'Привет мир'
    # greeting_text.color = ft.Colors.GREEN

    def on_button_click(_):
        print(name_input.value)
        name = name_input.value.strip()

        if name:
            greeting_text.value = f'Hello {name}'
            greeting_text.color = None
        else:
            greeting_text.value = 'Введите корректное имя'
            greeting_text.color = ft.Colors.RED
        page.update()
    def on_button_click_mode(_):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
        page.update()
    

    

    name_input = ft.TextField(label='Введите имя', on_submit=on_button_click)

    text_button = ft.TextButton(text='send', on_click=on_button_click, icon=ft.Icons.SEND)
    elevated_button = ft.ElevatedButton(text="send", on_click=on_button_click, icon=ft.Icons.SEND, color=ft.Colors.GREEN, icon_color=ft.Colors.RED)

    icon_button = ft.IconButton(icon=ft.Icons.BRIGHTNESS_6, on_click=on_button_click)

    icon_button_mode = ft.IconButton(icon=ft.Icons.BRIGHTNESS_6, on_click=on_button_click_mode)

    

    page.add(greeting_text, name_input, text_button, icon_button_mode)

ft.app(target=main)