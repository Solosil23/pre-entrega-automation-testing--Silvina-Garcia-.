
import pytest
from utils.sauce_page import SaucePage
import time 

VALID_USER = "standard_user"
VALID_PASSWORD = "secret_sauce"

def test_01_login_exitoso(driver_setup):
    
    driver = driver_setup
    page = SaucePage(driver)

    try:
        print("\n--- Ejecutando Test 01: Login Exitoso ---")
        # 1. Navegar a la página de login
        page.navegar_a_login()
        time.sleep(1) 

        # 2. Ingresar credenciales válidas
        page.login(VALID_USER, VALID_PASSWORD)
        time.sleep(2)

        # 3. Validar login exitoso
        page.validar_login_exitoso()

    except Exception as e:
        print(f"❌ Fallo en test_01_login_exitoso: {e}")
        driver.save_screenshot("error_login.png") 
        raise