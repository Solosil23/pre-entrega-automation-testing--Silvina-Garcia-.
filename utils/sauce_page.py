
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SaucePage:
    
    URL = "https://www.saucedemo.com/"
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    # Inventario
    INVENTORY_URL_PART = "inventory.html"
    INVENTORY_TITLE = (By.XPATH, "//span[@class='title' and text()='Products']")
    PRODUCT_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    PRODUCT_ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")
    ADD_TO_CART_BUTTON = (By.XPATH, "(//button[starts-with(@id, 'add-to-cart-')])[1]")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    SHOPPING_CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")

    # Carrito
    CART_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10) 
   
    def navegar_a_login(self):
        """Navega a la página de login de SauceDemo."""
        self.driver.get(self.URL)
        self.wait.until(EC.title_is("Swag Labs"))
        print(f"Título de la página: {self.driver.title}")

    def login(self, username, password):
        """Ingresa credenciales y hace clic en el botón de login."""
        self.wait.until(EC.presence_of_element_located(self.USERNAME_INPUT)).send_keys(username)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def validar_login_exitoso(self):
        """Verifica la redirección a la página de inventario y el título 'Products'."""
        self.wait.until(EC.url_contains(self.INVENTORY_URL_PART))
        products_title = self.wait.until(EC.presence_of_element_located(self.INVENTORY_TITLE))
        
        assert self.INVENTORY_URL_PART in self.driver.current_url
        assert products_title.text == "Products"
        print("✅ Login exitoso y validación de URL/Título completada.")

    def verificar_catalogo(self):
        """Verifica la presencia de elementos del catálogo y lista el primer producto."""
        
        assert self.driver.title == "Swag Labs"
        primer_producto = self.wait.until(EC.presence_of_element_located(self.PRODUCT_ITEM_NAME))
        assert primer_producto.is_displayed()

        self.wait.until(EC.presence_of_element_located(self.MENU_BUTTON))
        
        primer_precio = self.driver.find_element(*self.PRODUCT_ITEM_PRICE)
        print(f"\n🏷️ Información del Primer Producto: Nombre: {primer_producto.text}, Precio: {primer_precio.text}")
        return primer_producto.text 

    def interaccion_con_productos(self):
        """Añade el primer producto al carrito y verifica el contador."""
        
        add_button = self.wait.until(EC.element_to_be_clickable(self.ADD_TO_CART_BUTTON))
        add_button.click()
        print("✅ Primer producto añadido al carrito.")
        
        self.wait.until(EC.text_to_be_present_in_element(self.CART_BADGE, "1"))
        contador = self.driver.find_element(*self.CART_BADGE).text
        assert contador == "1"
        print(f"✅ Contador del carrito verificado: {contador}.")

    def verificar_producto_en_carrito(self, nombre_producto_esperado):
        """Navega al carrito y verifica la presencia del producto."""
        
        self.driver.find_element(*self.SHOPPING_CART_LINK).click()
        self.wait.until(EC.url_contains("/cart.html"))
        print("✅ Navegación al carrito de compras exitosa.")

        cart_product_name = self.wait.until(EC.presence_of_element_located(self.CART_ITEM_NAME)).text
        
        assert cart_product_name == nombre_producto_esperado
        print(f"✅ Producto '{cart_product_name}' verificado en el carrito.")

