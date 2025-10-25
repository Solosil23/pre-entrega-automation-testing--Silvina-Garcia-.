
import pytest
from utils.sauce_page import SaucePage


VALID_USER = "standard_user"
VALID_PASSWORD = "secret_sauce"

def test_02_verificacion_catalogo(driver_setup):
    
    driver = driver_setup
    page = SaucePage(driver)
    
    print("\n--- Ejecutando Test 02: Verificación de Catálogo ---")
    
    # 1. Login para garantizar la independencia del test
    page.navegar_a_login()
    page.login(VALID_USER, VALID_PASSWORD)
    page.validar_login_exitoso() 

    # 2. Verificar el catálogo (incluye validación de título, presencia de productos y listado de info)
    page.verificar_catalogo()