from subprocess import Popen
from robot.libraries.BuiltIn import BuiltIn
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import socket

class Debug:
    def __init__(self, chrome_path, output='C://testChrome', port='9222'):
        self.chrome_path=chrome_path
        self.output=output
        self.port=port

    def __getattr__(self, name):
        if name == 'selenium':
            self.selenium = BuiltIn().get_library_instance('SeleniumLibrary')
        return object.__getattribute__(self, name)

    def debug_browser_exist(self, address, port):
        s = socket.socket()
        try:
            s.connect((address,port))
            return True

        except socket.error:
                return False

    def action(self):
        browser_exist = self.debug_browser_exist('127.0.0.1', int(self.port))
        if not browser_exist:
            self.open_debug_browser()
        capabilities = DesiredCapabilities.CHROME.copy()
        capabilities['acceptInsecureCerts'] = True
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("debuggerAddress", f"127.0.0.1:{self.port}")
        self.selenium.create_webdriver(driver_name="Chrome", alias="debug browser", desired_capabilities=capabilities, options=chrome_options)
        url = BuiltIn().get_variable_value('${dctrackURL}')
        if not browser_exist:
            self.selenium.go_to(url)

    def open_debug_browser(self):
        p = Popen([f"{self.chrome_path}", f"--remote-debugging-port={self.port}", f'--user-data-dir={self.output}'])