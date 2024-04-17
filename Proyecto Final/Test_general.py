from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time
import datos



def test_datofaltante(): 
    browser = webdriver.Edge()
    browser.get(datos.xd.url)
    browser.find_element(By. ID, "txtNombreUsuario").send_keys(datos.xd.user +  Keys.RETURN)
    assert datos.xd.user == "234"
    time.sleep(1)
    browser.save_screenshot("Resultados//errorcontra.png")
    for _ in range(30):
        browser.find_element(By. ID, "txtNombreUsuario").send_keys(Keys.BACKSPACE)
    
    time.sleep(5)

    browser.find_element(By. ID, "txtContrasena").send_keys(datos.xd1.maluser + Keys.ENTER)
    assert datos.xd1.malpass != datos.xd.password
    browser.save_screenshot("Resultados\\errorusario.png")
    browser.quit()


def test_datosmalos():
    browser = webdriver.Edge()
    browser.maximize_window()
    browser.get(datos.xd.url)
    browser.find_element(By. ID, "txtNombreUsuario").send_keys("klkprueba" + Keys.ENTER)
    browser.find_element(By. ID, "txtContrasena").send_keys(datos.xd1.malpass + Keys.ENTER)
    assert datos.xd1.malpass != datos.xd.password
    time.sleep(1)
    browser.save_screenshot("Resultados\\errorboth.png")
    browser.quit()


def test_datoexitoso():
    browser = webdriver.Edge()
    browser.maximize_window()
    browser.get(datos.xd.url)
    browser.find_element(By. ID, "txtNombreUsuario").send_keys(datos.xd.user)
    browser.find_element(By. ID, "txtContrasena").send_keys(datos.xd.password + Keys.ENTER)
    time.sleep(5)
    assert datos.xd1.malpass != datos.xd.password
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    browser.find_element(By. LINK_TEXT, "Aceptar").click()
    main = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By. ID, "div-contenedor"))
    )
    browser.save_screenshot("Resultados\\success.png")
    browser.quit()


def test_auditoria():
    browser = webdriver.Edge()
    browser.maximize_window()
    browser.get(datos.xd.url)
    browser.find_element(By. ID, "txtNombreUsuario").send_keys(datos.xd.user)
    browser.find_element(By. ID, "txtContrasena").send_keys(datos.xd.password + Keys.ENTER)
    assert datos.xd1.malpass, datos.xd.user != datos.xd.password
    time.sleep(5)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    browser.find_element(By. LINK_TEXT, "Aceptar").click()
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By. ID, "div-contenedor"))
    )
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)
    browser.find_element(By. ID, "tipsAu").click()
    time.sleep(5)
    browser.save_screenshot("Resultados\\auditoria.png")
    browser.quit()


def test_mensaje():
    browser = webdriver.Edge()
    browser.maximize_window()
    browser.get(datos.xd.url)
    browser.find_element(By. ID, "txtNombreUsuario").send_keys(datos.xd.user)
    browser.find_element(By. ID, "txtContrasena").send_keys(datos.xd.password + Keys.ENTER)
    assert datos.xd1.malpass, datos.xd.user != datos.xd.password
    time.sleep(5)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    browser.find_element(By. LINK_TEXT, "Aceptar").click()
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By. ID, "div-contenedor"))
    )
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)
    browser.find_element(By. ID, "divMensajeAlerta").click()
    time.sleep(5)
    browser.save_screenshot("Resultados\\mensaje.png")
    browser.quit()


def test_recinto():
    browser = webdriver.Edge()
    browser.get(datos.xd.url)
    browser.maximize_window()
    assert datos.xd.url == datos.xd.url
    Select(browser.find_element(By. ID, "drpdRecinto")).select_by_value("9")
    time.sleep(1)
    browser.save_screenshot("Resultados\\recinto.png")
    browser.refresh()
    Select(browser.find_element(By. ID, "drpdRecinto")).select_by_value("10")
    browser.save_screenshot("Resultados\\recinto1.png")
    time.sleep(2)
    browser.quit()
    

def test_recuperarclave(): 
    browser = webdriver.Edge()
    browser.get(datos.xd.url)
    browser.maximize_window()
    browser.find_element(By.LINK_TEXT, "Olvidaste tu clave?").click()
    browser.find_element(By.ID, "txtUsuario").send_keys(datos.xd1.shortuser)
    browser.find_element(By.CLASS_NAME, "espacio-d20").click()
    browser.save_screenshot("Resultados\\recuperarclave.png")
    for _ in range(2):
        browser.find_element(By.ID, "txtUsuario").send_keys(Keys.BACKSPACE)
    time.sleep(2)
    browser.find_element(By.ID, "txtUsuario").send_keys(datos.xd1.maluser)
    browser.find_element(By.CLASS_NAME, "espacio-d20").click()
    assert datos.xd1.shortuser != datos.xd1.maluser
    browser.save_screenshot("Resultados\\recuperarclave1.png")
    browser.quit()


def test_recuperarusuario():
    browser = webdriver.Edge()
    browser.get(datos.xd.url)
    browser.maximize_window()
    browser.find_element(By.LINK_TEXT, "Olvidaste tu usuario?").click()
    detalle = browser.find_element(By.ID, "txtCorreo")
    detalle.send_keys(datos.xd1.shortuser)
    browser.find_element(By.CLASS_NAME, "espacio-d20").click()
    browser.save_screenshot("Resultados\\Recuperarusuario.png")
    time.sleep(5)
    detalle.send_keys(Keys.BACKSPACE)
    browser.refresh
    browser.find_element(By.ID, "txtCorreo").send_keys(datos.xd1.maluser)
    assert datos.xd1.shortuser != datos.xd1.maluser
    browser.find_element(By.CLASS_NAME, "espacio-d20").click()
    browser.save_screenshot("Resultados\\Recuperarusuario1.png")
    time.sleep(5)
    browser.quit()


def test_registro():
    browser = webdriver.Edge()
    browser.maximize_window()
    browser.get(datos.xd.url)
    assert datos.xd.url != "https://www.tecnoparque.gov.co/"
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    browser.find_element(By. LINK_TEXT, "Registro Tecnólogo").click()
    browser.find_element(By. CLASS_NAME, "px-3").click()
    browser.save_screenshot("Resultados\\registro.png")
    browser.quit()

    
def test_cajab():
    browser = webdriver.Edge()
    browser.maximize_window()
    browser.get(datos.xd.url)
    browser.find_element(By. ID, "txtNombreUsuario").send_keys(datos.xd.user)
    browser.find_element(By. ID, "txtContrasena").send_keys(datos.xd.password + Keys.ENTER)
    assert datos.xd.user != datos.xd.password
    time.sleep(3)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    browser.find_element(By. LINK_TEXT, "Aceptar").click()
    time.sleep(5)
    browser.find_element(By. LINK_TEXT, "MI MENÚ").click()
    browser.find_element(By. ID, "mCaja").click()
    time.sleep(2)
    browser.find_element(By. LINK_TEXT, "Balance Pendiente").click()
    time.sleep(3)
    browser.save_screenshot("Resultados\\caja.png")
    browser.quit()


def test_cajap():
    browser = webdriver.Edge()
    browser.maximize_window()
    browser.get(datos.xd.url)
    browser.find_element(By. ID, "txtNombreUsuario").send_keys(datos.xd.user)
    browser.find_element(By. ID, "txtContrasena").send_keys(datos.xd.password + Keys.ENTER)
    assert datos.xd.user != datos.xd.password
    time.sleep(3)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    browser.find_element(By. LINK_TEXT, "Aceptar").click()
    time.sleep(5)
    browser.find_element(By. LINK_TEXT, "MI MENÚ").click()
    browser.find_element(By. ID, "mCaja").click()
    time.sleep(2)
    browser.find_element(By. LINK_TEXT, "Pago en línea").click()
    time.sleep(3)
    browser.save_screenshot("Resultados\\cajap.png")
    browser.quit()


def test_gestiondocencia1():
    browser = webdriver.Edge()
    browser.maximize_window()
    browser.get(datos.xd.url)
    browser.find_element(By. ID, "txtNombreUsuario").send_keys(datos.xd.user)
    browser.find_element(By. ID, "txtContrasena").send_keys(datos.xd.password + Keys.ENTER)
    assert datos.xd.user != datos.xd.password
    time.sleep(3)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    browser.find_element(By. LINK_TEXT, "Aceptar").click()
    time.sleep(5)
    browser.find_element(By. LINK_TEXT, "MI MENÚ").click()
    browser.find_element(By. LINK_TEXT, "Gestión Docencia").click()
    browser.find_element(By. LINK_TEXT, "Consulta Calificación").click()
    browser.save_screenshot("Resultados\\gestiondocencia1.png")
    browser.quit()


def test_gestiondocencia2():
    browser = webdriver.Edge()
    browser.maximize_window()
    browser.get(datos.xd.url)
    browser.find_element(By. ID, "txtNombreUsuario").send_keys(datos.xd.user)
    browser.find_element(By. ID, "txtContrasena").send_keys(datos.xd.password + Keys.ENTER)
    assert datos.xd.user != datos.xd.password
    time.sleep(3)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    browser.find_element(By. LINK_TEXT, "Aceptar").click()
    time.sleep(5)
    browser.find_element(By. LINK_TEXT, "MI MENÚ").click()
    browser.find_element(By. LINK_TEXT, "Gestión Docencia").click()
    browser.find_element(By. LINK_TEXT, "Histórico Calificación").click()
    browser.save_screenshot("Resultados\\gestiondocencia2.png")
    browser.quit()

    
def test_solicitud():
    browser = webdriver.Edge()
    browser.maximize_window()
    browser.get(datos.xd.url)
    browser.find_element(By. ID, "txtNombreUsuario").send_keys(datos.xd.user)
    browser.find_element(By. ID, "txtContrasena").send_keys(datos.xd.password + Keys.ENTER)
    assert datos.xd.user != datos.xd.password
    time.sleep(3)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    browser.find_element(By. LINK_TEXT, "Aceptar").click()
    time.sleep(5)
    browser.find_element(By. LINK_TEXT, "MI MENÚ").click()
    browser.find_element(By. LINK_TEXT, "Solicitud").click()
    browser.find_element(By. LINK_TEXT, "Cambio Carrera").click()
    browser.save_screenshot("Resultados\\solicitud.png")
    browser.quit()


def test_logout():
    browser = webdriver.Edge()
    browser.maximize_window()
    browser.get(datos.xd.url)
    browser.find_element(By. ID, "txtNombreUsuario").send_keys(datos.xd.user)
    browser.find_element(By. ID, "txtContrasena").send_keys(datos.xd.password + Keys.ENTER)
    assert datos.xd.user != datos.xd.password
    time.sleep(3)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    browser.find_element(By. LINK_TEXT, "Aceptar").click()
    time.sleep(5)
    browser.find_element(By. ID, "cerrar-sesion").click()
    browser.save_screenshot("Resultados\\logout1.png")
    browser.find_element(By. CLASS_NAME, "fast_confirm_proceed").click()
    browser.save_screenshot("Resultados\\logout2.png")
    browser.quit()


def test_lineadetiempo():
    browser = webdriver.Edge()
    browser.maximize_window()
    browser.get(datos.xd.url)
    browser.find_element(By. ID, "txtNombreUsuario").send_keys(datos.xd.user)
    browser.find_element(By. ID, "txtContrasena").send_keys(datos.xd.password + Keys.ENTER)
    assert datos.xd.user != datos.xd.password
    time.sleep(3)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    browser.find_element(By. LINK_TEXT, "Aceptar").click()
    time.sleep(5)
    browser.find_element(By. LINK_TEXT, "MI MENÚ").click()
    browser.find_element(By. ID, "mAcadémico").click()
    browser.find_element(By. LINK_TEXT, "Consulta Estudiante Línea de Tiempo").click()
    browser.save_screenshot("Resultados\\lineadetiempo.png")
    browser.quit()
 

def test_admisiones():
    browser = webdriver.Edge()
    browser.maximize_window()
    browser.get(datos.xd.url)
    browser.find_element(By. ID, "txtNombreUsuario").send_keys(datos.xd.user)
    browser.find_element(By. ID, "txtContrasena").send_keys(datos.xd.password + Keys.ENTER)
    assert datos.xd.user != datos.xd.password
    time.sleep(3)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    browser.find_element(By. LINK_TEXT, "Aceptar").click()
    time.sleep(5)
    browser.find_element(By. LINK_TEXT, "MI MENÚ").click()
    browser.find_element(By. LINK_TEXT, "Admisiones").click()
    browser.find_element(By. LINK_TEXT, "Documento Admisión").click()
    browser.save_screenshot("Resultados\\admisiones.png")
    browser.quit()
    
def test_inscripcion():
    browser = webdriver.Edge()
    browser.maximize_window()
    browser.get(datos.xd.url)
    browser.find_element(By. ID, "txtNombreUsuario").send_keys(datos.xd.user)
    browser.find_element(By. ID, "txtContrasena").send_keys(datos.xd.password + Keys.ENTER)
    assert datos.xd.user != datos.xd.password
    time.sleep(3)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    browser.find_element(By. LINK_TEXT, "Aceptar").click()
    time.sleep(5)
    browser.find_element(By. LINK_TEXT, "MI MENÚ").click()
    browser.find_element(By. LINK_TEXT, "Educación Permanente").click()
    browser.find_element(By. LINK_TEXT, "Inscripción Permanente").click()
    browser.save_screenshot("Resultados\\inscripcion.png")
    browser.quit()
   

def test_residenciasalida():
    browser = webdriver.Edge()
    browser.maximize_window()
    browser.get(datos.xd.url)
    browser.find_element(By. ID, "txtNombreUsuario").send_keys(datos.xd.user)
    browser.find_element(By. ID, "txtContrasena").send_keys(datos.xd.password + Keys.ENTER)
    assert datos.xd.user != datos.xd.password
    time.sleep(3)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    browser.find_element(By. LINK_TEXT, "Aceptar").click()
    time.sleep(5)
    browser.find_element(By. LINK_TEXT, "MI MENÚ").click()
    browser.find_element(By. LINK_TEXT, "Residencia").click()
    browser.find_element(By. LINK_TEXT, "Solicitud Salida De Residencia").click()
    browser.save_screenshot("Resultados\\residenciasalida.png")
    browser.quit()
    

def test_residenciasolicitud():
    browser = webdriver.Edge()
    browser.maximize_window()
    browser.get(datos.xd.url)
    browser.find_element(By. ID, "txtNombreUsuario").send_keys(datos.xd.user)
    browser.find_element(By. ID, "txtContrasena").send_keys(datos.xd.password + Keys.ENTER)
    assert datos.xd.user != datos.xd.password
    time.sleep(3)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    browser.find_element(By. LINK_TEXT, "Aceptar").click()
    time.sleep(5)
    browser.find_element(By. LINK_TEXT, "MI MENÚ").click()
    browser.find_element(By. LINK_TEXT, "Residencia").click()
    browser.find_element(By. LINK_TEXT, "Solicitud Vivienda").click()
    browser.save_screenshot("Resultados\\residenciasolicitud.png")
    browser.quit()
    