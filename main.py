# # import flet as ft
# # def main(page: ft.Page):
# #     page.title = 'Moe pervoe prilojenie'
# #     page.theme_mode = ft.ThemeMode.LIGHT
# #     greeting_text = ft.Text(value='Hello world', color=ft.Colors.RED)
# #     # greeting_text.value = 'Privet mir'
# #     # greeting_text.color = ft.Colors.GREEN
# #     def on_button_click(_):
# #          print(name_input.value)
# #          name = name_input.value
# #          greeting_text.value = f'Hello {name}'
# #          print(greeting_text)
# #          page.update()
# #     name_input = ft.TextField(label='Vvedite imya', on_submit=on_button_click)

# #     page.add(greeting_text, name_input)
# # ft.app(target=main)
# # from datetime import date
# # from flet import Text, TextField

# import flet as ft
# from datetime import datetime

# def main(page: ft.Page):
#     page.title = 'Мое первое приложение'
#     page.theme_mode = ft.ThemeMode.LIGHT
#     greeting_text = ft.Text(value='Hello world')

#     greeting_history = []
#     history_text = ft.Text("История приветствий:")

#     # greeting_text.value = 'Привет мир'
#     # greeting_text.color = ft.Colors.GREEN

#     def on_button_click(_):
#         print(name_input.value)
#         name = name_input.value.strip()
#         time = datetime.now()

#         if name:
#             greeting_text.value = f'Hello {name}, {time}'
#             greeting_text.color = None
#             name_input.value = None

#             greeting_history.append(name)
#             print(greeting_history)
#             history_text.value = "История приветствий:\n" + "\n".join(greeting_history), f'{time}'
#         else:
#             greeting_text.value = 'Введите корректное имя'
#             greeting_text.color = ft.Colors.RED
#         page.update()
#     def on_button_click_mode(_):
#         if page.theme_mode == ft.ThemeMode.LIGHT:
#             page.theme_mode = ft.ThemeMode.DARK
#         else:
#             page.theme_mode = ft.ThemeMode.LIGHT
#         page.update()
    

    

#     name_input = ft.TextField(label='Введите имя', on_submit=on_button_click, expand=True)

#     text_button = ft.TextButton(text='send', on_click=on_button_click, icon=ft.Icons.SEND)
#     elevated_button = ft.ElevatedButton(text="send", on_click=on_button_click, icon=ft.Icons.SEND, color=ft.Colors.GREEN, icon_color=ft.Colors.RED)

#     icon_button = ft.IconButton(icon=ft.Icons.BRIGHTNESS_6, on_click=on_button_click)

#     icon_button_mode = ft.IconButton(icon=ft.Icons.BRIGHTNESS_7, on_click=on_button_click_mode)

#     def clear_history(_):
#         greeting_history.clear()
#         history_text.value = "История приветствий:"
#         page.update()

#     clear_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=clear_history)

    

#     # page.add(greeting_text, name_input, text_button, elevated_button, icon_button_mode)
#     page.add(greeting_text, ft.Row([name_input,elevated_button]), history_text)

# ft.app(target=main)


# from datetime import date
# from flet import Text, TextField

import flet as ft

def main(page: ft.Page):
    page.title = 'Мое первое приложение'
    page.theme_mode = ft.ThemeMode.LIGHT
    greeting_text = ft.Text(value='Hello world')

    greeting_history = []
    history_text = ft.Text(value='История приветствий:')
    greeting_history_favourite = []
    history_text_favourite = ft.Text(value='История любимых:')

    # greeting_text.value = 'Привет мир'
    # greeting_text.color = ft.Colors.GREEN

    def on_button_click(_):
        print(name_input.value)
        name = name_input.value.strip()

        if name:
            greeting_text.value = f'Hello {name}'
            greeting_text.color = None
            name_input.value = None

            greeting_history.append(name)
            print(greeting_history)
            history_text.value = "История приветствий: \n" + "\n".join(greeting_history[-5:])
            with open("history.txt", "a") as f:
                f.write(name+"\n")
        else:
            greeting_text.value = 'Введите корректное имя'
            greeting_text.color = ft.Colors.RED
        page.update()
        

    name_input = ft.TextField(label='Введите имя', on_submit=on_button_click, expand=True)

    # name_input.expand = False

    elevated_button = ft.ElevatedButton(text="send", on_click=on_button_click, icon=ft.Icons.SEND, color=ft.Colors.GREEN, icon_color=ft.Colors.RED)

    text_button = ft.TextButton(text='send', on_click=on_button_click, icon=ft.Icons.SEND)

    icon_button = ft.IconButton(icon=ft.Icons.BRIGHTNESS_6, on_click=on_button_click)
    
    def on_button_click_favourite(_):
            greeting_history_favourite.append(greeting_history[-1])
            print(greeting_history_favourite)
            history_text_favourite.value = "История любимых: \n" + "\n".join(greeting_history_favourite)
        
            greeting_text.value = 'Введите корректное имя'
            greeting_text.color = ft.Colors.RED
            page.update()

           
    

    elevated_button_favourite = ft.ElevatedButton(text="Favourite", on_click=on_button_click_favourite, icon=ft.Icons.FAVORITE, color=ft.Colors.BLUE, icon_color=ft.Colors.YELLOW)


    def on_click_button_mode(_):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
        else:
                page.theme_mode=ft.ThemeMode.LIGHT
        page.update()
    icon_button_mode = ft.IconButton(icon=ft.Icons.BRIGHTNESS_7, on_click=on_click_button_mode)




    def clear_history(_):
        greeting_history.clear()
        history_text.value = 'История приветствий:'
        greeting_text.value = 'История очищена'
        page.update()

    # name_input.on_submit = clear_history

    clear_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=clear_history)

    # page.add(greeting_text, name_input, text_button, elevated_button, icon_button)

    page.add(greeting_text, ft.Row([name_input, elevated_button, clear_button]), history_text, elevated_button_favourite, history_text_favourite, icon_button_mode)

ft.app(target=main)