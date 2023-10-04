#import flet_fastapi
import flet as ft

from app.utils import *
from app.app import MainApp


async def main(page: ft.Page):

    # Main properties setting
    # page.show_semantics_debugger = True
    page.title = "PetList.fun"
    page.horizontal_alignment = "center"
    page.scroll = "adaptive"
    page.fonts = get_fonts()
    page.padding = 4
    await page.update_async()
    app = MainApp(page)
    await page.add_async(app)



#app = flet_fastapi.app(main)
#ft.app(target=main, view=ft.WEB_BROWSER, port=5052, assets_dir="assets", use_color_emoji=True, web_renderer=ft.WebRenderer.HTML)
ft.app(target=main, view=ft.WEB_BROWSER, port=5059, assets_dir="assets")

