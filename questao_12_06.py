import flet as ft
from time import sleep
import flet as ft

def main(page: ft.Page):
    page.title = "220,241"

    pg = ft.ListView(expand=1, spacing=13, padding=24, auto_scroll=True)

    count = 220

    for i in range(220, 241):
        pg.controls.append(ft.Text(f"Line {count}"))
        count += 1

    page.add(pg)


ft.app(target=main)

