import flet as ft


def main(page: ft.Page):
    def click(e):
        page.add(ft.Checkbox(label=nueva_tarea.value))
        nueva_tarea.value = ""
        page.update()

    nueva_tarea = ft.TextField(hint_text="Escribe tu tarea", expand=True)
    vista_tareas = ft.Column()
    vista = ft.Column(
        width=600,
        controls=[
            ft.Row(
                controls=[
                    nueva_tarea,
                    ft.FloatingActionButton(icon=ft.icons.ADD, on_click=click),
                ]
            ),
            vista_tareas,
        ],
    )
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(vista)


ft.app(main)
