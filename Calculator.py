# This is basic duplicate of my mobile's calculator interface with its functionality

import flet as ft


def main(page: ft.Page):
    page.title = "Phone Calculator"
    page.bgcolor = "black"
    page.window.width = 400
    page.window.height = 550
    page.window.center()
    page.padding = 20
    page.scrollable = True
    page.resizable = False

    page.appbar=ft.AppBar(
        leading=ft.Icon(ft.Icons.CALCULATE_OUTLINED, color=ft.Colors.WHITE),
        center_title=True,
        bgcolor="black",
        actions=[ft.IconButton(ft.Icons.MENU, icon_color=ft.Colors.WHITE),
        ]
    )

    # Display area
    resulted_display = ft.Text(
        value="0", color="white", size=40, weight="bold", font_family=("Arial", 20),
    )
    # I created a dictionary that will serve as a container for the operator string
    state = {"current_operator": ""}
    # Event handler for the operation
    def button_click(e):
        data = e.control.data
        # This serves as the clear functionality in a calculator
        if data == "C":
            state["current_operator"] = ""
            resulted_display.value = "0"

        elif data == "=":
            try:
                # eval the stored equation, not the button value
                expression = state["current_operator"]
                if not expression:
                    return

                calculated_value = eval(expression)
                state["current_operator"] = str(calculated_value)
                resulted_display.value = state["current_operator"]
            except Exception:
                resulted_display.value = "Error"
                state["current_operator"] = ""

        # this is for the delete logic of the calculator
        elif data == "DEL":
            state["current_operator"] = state["current_operator"][:-1]
            if state["current_operator"] == "":
                resulted_display.value="0"
            else:
                resulted_display.value=state["current_operator"]
        # this is the percentage logic of the computer
        elif data == "%":
            try:
                present_value = eval(state["current_operator"])
                state["current_operator"] = str(present_value/100)
                resulted_display.value=state["current_operator"]
            except Exception:
                resulted_display.value="Error"
                state["current_operator"] = ""
        else:
            # We simply append the data here.
            state["current_operator"] += data
            resulted_display.value = state["current_operator"]

        # FIX: Update the page so the changes show up on screen!
        page.update()

    def create_button(text, text_color=ft.Colors.WHITE, bg_color=ft.Colors.GREY_900,):
        return ft.ElevatedButton(
            text=text,
            data=text,
            on_click=button_click,  # Ensure the click is linked
            bgcolor=bg_color,  # Dark Grey buttons look better on Black
            color=text_color,  # White text
            width=60,
            height=60,
            style=ft.ButtonStyle(shape=ft.CircleBorder()),
        )

    def create_button2(text, text_color=ft.Colors.WHITE, bg_color=ft.Colors.GREY_900,):
        return ft.ElevatedButton(
            text=text,
            data=text,
            on_click=button_click,  # Ensure the click is linked
            bgcolor=bg_color,  # Dark Grey buttons look better on Black
            color=text_color,  # White text
            width=60,
            height=60,
            style=ft.ButtonStyle(shape=ft.CircleBorder()),
        )

    layout = ft.Column(
        controls=[
            # ft.Row(
            #     header=ft.ElevatedButton(style=ft.ButtonStyle(color=ft.Colors.WHITE)),
            # ),
            ft.Container(
                content=resulted_display,
                padding=ft.padding.only(bottom=20),
                alignment=ft.alignment.center_right,
            ),
            ft.Row(
                controls=[
                    create_button("C", text_color=ft.Colors.RED),
                    create_button2("%",text_color=ft.Colors.BLUE),
                    create_button("DEL",text_color=ft.Colors.BLUE),
                    create_button("/",text_color=ft.Colors.BLUE),
                ],
                alignment=ft.MainAxisAlignment.SPACE_EVENLY
            ),
            ft.Row(
                controls=[
                    create_button("7"),
                    create_button("8"),
                    create_button("9"),
                    create_button("*",text_color=ft.Colors.BLUE),
                ],
                alignment=ft.MainAxisAlignment.SPACE_EVENLY
            ),
            ft.Row(
                controls=[
                    create_button("4"),
                    create_button("5"),
                    create_button("6"),
                    create_button("-",text_color=ft.Colors.BLUE),
                ],
                alignment=ft.MainAxisAlignment.SPACE_EVENLY
            ),
            ft.Row(
                controls=[
                    create_button("1"),
                    create_button("2"),
                    create_button("3"),
                    create_button("+",text_color=ft.Colors.BLUE),
                ],
                alignment=ft.MainAxisAlignment.SPACE_EVENLY
            ),
            ft.Row(
                controls=[
                    create_button2("[]"),
                    create_button("0"),
                    # Add a backspace or placeholder here to fill the grid
                    create_button("."),
                    create_button("=",text_color=ft.Colors.WHITE, bg_color=ft.Colors.BLUE),
                ],
                alignment=ft.MainAxisAlignment.SPACE_EVENLY
            ),
        ],
    )
    page.add(layout)


ft.app(target=main)