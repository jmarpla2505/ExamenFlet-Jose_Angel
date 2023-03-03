import flet as ft


def main(page: ft.Page):
    page.title = "Examen Flet"

    #password="123"
    #usuario="Jose"
    #Ejercicio 6
    def funcionboton(e):
        if tfnombre.value==tfpassword.value:
            dlg = ft.AlertDialog(
            title=ft.Text("La contraseña y el usuario son correctos"))
            page.dialog = dlg
            dlg.open = True
        else:
            dlg = ft.AlertDialog(
            title=ft.Text("El usuario o la contraseña son incorrectos"))
            page.dialog = dlg
            dlg.open = True
        page.update()
    #Fin --- Ejercicio 6


    #Ejercicio 2
    img = ft.Image(
        src=f"Logo.png",
        width=100,
        height=100,
        fit=ft.ImageFit.CONTAIN,
    )
    
    #Fin --- Ejercicio 2


    #Ejercicio 3
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    #Fin --- Ejercicio 3

    page.window_height=500
    page.window_width= 250



    tfnombre = ft.TextField(label="Nombre")
    
    #Ejercicio 4
    
    tfpassword = ft.TextField(label="Contraseña", password=True, can_reveal_password=True)
    #Fin --- Ejercicio 4


    #Ejercicio 5
    btcomprobar = ft.ElevatedButton("Botón para comprobar", icon="check", on_click=funcionboton)
    #Fin-- Ejercicio 5


    page.add(img,tfnombre, tfpassword, btcomprobar)
    


ft.app(target=main,assets_dir="fotos")