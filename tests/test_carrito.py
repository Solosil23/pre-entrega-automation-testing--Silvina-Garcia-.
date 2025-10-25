
import pytest
from utils.sauce_page import SaucePage

VALID_USER = "standard_user"
VALID_PASSWORD = "secret_sauce"

def test_03_interaccion_y_verificacion_carrito(driver_setup):
    
    driver = driver_setup
    page = SaucePage(driver)
    
    print("\n--- Ejecutando Test 03: Interacción con Carrito ---")

    # 1. Login para garantizar la independencia del test
    page.navegar_a_login()
    page.login(VALID_USER, VALID_PASSWORD)
    page.validar_login_exitoso()
    
    # 2. Obtener el nombre del producto (implica verificar la presencia del catálogo)
    nombre_producto_a_agregar = page.verificar_catalogo() 
    
    # 3. Añadir producto y verificar contador
    page.interaccion_con_productos()

    # 4. Navegar al carrito y verificar la presencia del ítem
    page.verificar_producto_en_carrito(nombre_producto_a_agregar)