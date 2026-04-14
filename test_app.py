from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from app import app

def test_header_presence(dash_duo):
    dash_duo.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#header", timeout=10)
    assert dash_duo.find_element("#header").text == "Pink Morsel Visualiser"

def test_visualisation_presence(dash_duo):
    dash_duo.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#sales-line-chart", timeout=10)
    assert dash_duo.find_element("#sales-line-chart") is not None

def test_region_picker_presence(dash_duo):
    dash_duo.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#region-filter", timeout=10)
    assert dash_duo.find_element("#region-filter") is not None