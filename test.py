import flet as ft

def main(page: ft.Page):
    page.title="Phone Calculator"
    page.bgcolor="black"
    page.window.width=350
    page.window.height=500
    page.border="1px solid black"
    page.window.resizable= True
    page.padding= 20
    page.scrollable=True
    #display area
    resulted_display= ft.Text(
        value="0", color="white", size=40, text_align=None, weight="bold"
    )

    current_operator=""

    def button_click(e):
        nonlocal current_operator
        data = e.control.data

        if data =="C":
            current_operator = ""
            resulted_display.value="0"

        elif data =="=":
            try:
                calculated_value = eval(e.control.value)
                current_operator = str(calculated_value)
                resulted_display.value=current_operator
            except Exception:
                resulted_display.value="Math Error"
                current_operator = ""

        else:
            if current_operator and data in["+","-","*","/"]:
                return
        current_operator += data
        resulted_display.value = current_operator
        resulted_display.update()

    def create_button(text, color=ft.Colors.BLACK, color_1=ft.Colors.BLACK, color_2=ft.Colors.BLUE):
        return ft.ElevatedButton(
            text=text, data=text, bgcolor=ft.Colors.GREY_50, color=color, width=45,height=45, style=ft.ButtonStyle(shape=ft.CircleBorder())
        )
    page.update()


    layout=ft.Column(
            controls=[
            ft.Container(
                content=resulted_display,
                padding=ft.padding.only(bottom=20),
                alignment=ft.alignment.center_right,
            ),
            ft.Row(
                controls=[
                    create_button("C",),
                    create_button("(",),
                    create_button(")", ),
                    create_button("/", ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_EVENLY
            ),
            ft.Row(
                controls=[
                    create_button("7",),
                    create_button("8",),
                    create_button("9",),
                    create_button("*", ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_EVENLY
            ),
            ft.Row(
                controls=[
                    create_button("4", ),
                    create_button("5", ),
                    create_button("6", ),
                    create_button("-", ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_EVENLY
            ),
            ft.Row(
                controls=[
                    create_button("1", ),
                    create_button("2", ),
                    create_button("3", ),
                    create_button("+", ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_EVENLY
            ),
            ft.Row(
                controls=[
                    create_button("[", ),
                    create_button("0", ),
                    create_button(".", ),
                    create_button("=",),
                ],
                alignment=ft.MainAxisAlignment.SPACE_EVENLY
            ),
        ],
    )
    page.add(layout),

ft.app(target=main),
