
import pytest
from selenium import webdriver

@pytest.fixture(scope="module")
def driver_setup():
    driver = webdriver.Chrome() 
    driver.maximize_window()
    print("\n🌐 Inicializando WebDriver (desde conftest.py)...")
    
    yield driver 

    print("\n✖️ Cerrando WebDriver (desde conftest.py)...")
    driver.quit()

