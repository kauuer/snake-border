import flet as ft
import math
from asyncio import sleep

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    animated_border = ft.Ref[ft.Container] ()
    
    snake_border = ft.Container(
        width = 900,
        height = 200,
        bgcolor = ft.colors.BLACK,
        border_radius = ft.border_radius.all(20),   
        content = ft.Stack(
            aspect_ratio=16/9,
            controls = [
                ft.Container(
                    ref=animated_border,
                    margin=ft.margin.symmetric(vertical=50),
                    gradient=ft.LinearGradient(
                        colors=[ft.colors.PINK, ft.colors.CYAN]
                    ),
                    scale=ft.Scale(scale_x=1.2),
                    animate_rotation=ft.Animation(duration=3000, curve=ft.AnimationCurve.LINEAR),
                    rotate=ft.Rotate(angle=0.3),
                ),
                ft.Container(
                    bgcolor=ft.colors.BLACK,
                    padding=ft.padding.all(20),
                    margin=ft.margin.all(10),
                    border_radius=ft.border_radius.all(15),
                    alignment=ft.alignment.center,
                    content=ft.Image(src='https://www.ipm.com.br/wp-content/uploads/2021/03/26-02-imagem-blog-2-1024x430.png')
                )
            ]
        )
    )
    
    async def infinite_rotate():
        while True:
            animated_border.current.rotate.angle += math.radians(360)
            animated_border.current.update()
            await sleep(3)
            
    page.add(snake_border)
    page.run_task(infinite_rotate)
    
if __name__ == '__main__':
    ft.app(target = main)