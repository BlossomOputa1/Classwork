import flet as ft

def main(page: ft.Page):
    page.title = "Flet Dictionary App"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor ="#313B2F"
    page.padding = 20
    # page.window.height = 600
    # page.window.width = 450
    page.window.center()
    page.window.maximized = True
    page.window.resizable = True

    # The Data Source (Local Dictionary)
    dictionary_data = {
        "Bus": "A large motor vehicle carrying passengers by road, typically one serving the public on a fixed route and for a fare.",
        "Cat": "A small domesticated carnivorous mammal with soft fur, a short snout, and retractable claws. It is widely kept as a pet or for catching mice, and many breeds have been developed.",
        "Dog": "A domesticated carnivorous mammal that typically has a long snout, an acute sense of smell, non-retractable claws, and a barking, howling, or whining voice",
        "Fish": "A limbless cold-blooded vertebrate animal with gills and fins living wholly in water",
        "Plate": "A flat dish, typically circular and made of china, from which food is eaten or served",
        "Bag":"A flexible container with a single opening",
        "Color":"The property possessed by an object of producing different sensations on the eye as a result of the way it reflects or emits light.",
        "Empathy":"The ability to understand and share the feelings of another",
        "Sympathy":"Feeling of pity and sorrow for someone else's misfortune.",
        "Encourage":"To give support, confidence, or hope to someone",
        "Nutrition": "The process of providing or obtaining the food necessary for health and growth",
    }

    # 2. Right Side: The Display Area Controls
    word_title = ft.Text(
        value="Select a word",
        size=40,
        weight=ft.FontWeight.BOLD,
        color="#FBA002",
    )

    word_definition = ft.Text(
        value="Click on a button on the left to see its definition here.",
        size=18,
        selectable=True,  # Allows user to copy text
        color="#FBA002"
    )
    # Header=ft.Text(
    #     value="Welcome to DictVision",
    #     size=40,
    #     weight=ft.FontWeight.BOLD,
    #     top=100
    # )

# the event handler for the dictionary
    def display_word(e):
        selected_word = e.control.text
        # Update the right side controls
        word_title.value = selected_word
        word_definition.value = dictionary_data[selected_word]
        page.update()

# buttons
    button_list = ft.ListView(
        expand=True,
        spacing=10,
        padding=10,
        auto_scroll=True,
    )

    for term in dictionary_data:
        button_list.controls.append(
            ft.OutlinedButton(
                text=term,
                on_click=display_word,
                # on_hover=display_word,
                height=50,
                style=ft.ButtonStyle(
                    shape=ft.BeveledRectangleBorder(radius=10),
                    color=ft.Colors.YELLOW_600,
                    bgcolor="#313B2F",
                ),
            ),
        )
    styling_layout = ft.Row(
        controls=[
            ft.Container(
                content=button_list,
                width=350,
                border=ft.border.only(right=ft.BorderSide(2, ft.Colors.BROWN_900)),
                padding=ft.padding.only(right=30),
                bgcolor="#FBA002",
            ),
           # ft.Container(
           #     content=ft.Row(
           #         controls=[Header,
           #                   ]
           #     ),
           # ),
            ft.Container(
                content=ft.Column(
                    controls=[
                        word_title,
                        ft.Divider(color="#FBA002", height=20, thickness=20),
                        word_definition,
                        ft.Divider(color="#FBA002"),
                    ],
                    scroll=ft.ScrollMode.AUTO,
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                expand=True,
                padding=ft.padding.only(left=20, top=10),
            )
        ],
        expand=True
    )

    page.add(styling_layout)


ft.app(target=main)