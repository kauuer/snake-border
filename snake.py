import flet as ft

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    snake_border = ft.Container(
        width = 900,
        height = 200,
        bgcolor = ft.colors.BLACK,
        border_radius = ft.border_radius.all(20),   
        content = ft.Stack(
            controls = [
                ft.Container(
                    margin=ft.margin.symmetric(vertical=50),
                    gradient=ft.LinearGradient(
                        colors=[ft.colors.PINK, ft.colors.CYAN]
                    )
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
    
    page.add(snake_border)
    
if __name__ == '__main__':
    ft.app(target = main)