import flet as ft
from flet.core import page


def main(page: ft.Page):
    page.title= "Dictionary"
    page.scroll = "auto"
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.vertical_alignment = "Center"
    page.window.height = 600
    page.window.width = 450
    page.window.center()
    page.window.maximized = False
    page.window.resizable = False
    page.bgcolor =ft.Colors.GREEN
    page.padding = 20


coll_of_word = {
    "boy": "A male child or adolescent",
    "girl": "A female child or adolescent",
    "book": "a written or printed work consisting of pages glued or sewn together along one side and bound in covers",
    "car":"a four-wheeled road vehicle that is powered by an engine and is able to carry a small number of people.",
    "bus":"a large motor vehicle carrying passengers by road, typically one serving the public on a fixed route and for a fare.",
    "cat":"a small domesticated carnivorous mammal with soft fur, a short snout, and retractable claws. It is widely kept as a pet or for catching mice, and many breeds have been developed.",
    "dog":"a domesticated carnivorous mammal that typically has a long snout, an acute sense of smell, non-retractable claws, and a barking, howling, or whining voice",
    "fish":"a limbless cold-blooded vertebrate animal with gills and fins living wholly in water",
    "plate":"a flat dish, typically circular and made of china, from which food is eaten or served",
}

button =

# Check if the term exists in the dictionary first
def search():
    if term in coll_of_word:
        # Print the definition associated with that term
        print(coll_of_word[term])
        definitions = ft.TextField(coll_of_word[term], )
    else:
        print("Sorry, that term is not in the dictionary.")
    page.update()

    page.add(
        ft.Column([
                ft.Container(
                    content=term,
                    bgcolor=ft.Colors.WHITE
            ),
        ]),
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )



ft.app(target=main)