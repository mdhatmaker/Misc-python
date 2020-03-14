from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys         # for keyboard
import pyautogui
import sys

### https://pyautogui.readthedocs.io/en/latest/
### https://stackoverflow.com/questions/11825322/python-code-to-automate-desktop-activities-in-windows
### https://stackoverflow.com/questions/47158434/how-to-run-selenium-tests-on-the-brave-web-browser
### https://stackoverflow.com/questions/49788257/what-is-default-location-of-chromedriver-and-for-installing-chrome-on-windows
### https://stackoverflow.com/questions/8344776/can-selenium-interact-with-an-existing-browser-session
### https://stackoverflow.com/questions/18897070/getting-the-current-tabs-url-from-google-chrome-using-c-sharp/18983677#18983677
### https://www.youtube.com/watch?v=wddZ5I_E2J4
### https://automatetheboringstuff.com/chapter11/
### https://stackoverflow.com/questions/7814027/how-can-i-get-urls-of-open-pages-from-chrome-and-firefox
### https://pywinauto.github.io/
### https://docs.microsoft.com/en-us/dotnet/api/system.windows.automation?redirectedfrom=MSDN&view=netframework-4.8
### https://stackoverflow.com/questions/31967430/microsoft-edge-get-window-url-and-title?lq=1


# executor_url = driver.command_executor._url
# session_id = driver.session_id
def attach_to_session(executor_url, session_id):
    original_execute = WebDriver.execute
    def new_command_execute(self, command, params=None):
        if command == "newSession":
            # Mock the response
            return {'success': 0, 'value': None, 'sessionId': session_id}
        else:
            return original_execute(self, command, params)
    # Patch the function before creating the driver object
    WebDriver.execute = new_command_execute
    driver = webdriver.Remote(command_executor=executor_url, desired_capabilities={})
    driver.session_id = session_id
    # Replace the patched function with original function
    WebDriver.execute = original_execute
    return driver
    # ^^^ example of how to use the above function: 
    # bro = attach_to_session('http://127.0.0.1:64092', '8de24f3bfbec01ba0d82a7946df1d1c3')
    # bro.get('http://ya.ru/')


def pyautogui_demo():
    print("FUNCTION: pyautogui_demo()")

    screenWidth, screenHeight = pyautogui.size()    # Get the size of the primary monitor

    currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse

    pyautogui.moveTo(100, 150)  # Move the mouse to XY coordinates

    sys.exit()

    pyautogui.click()           # Click the mouse
    pyautogui.click(100, 200)   # Move the mouse to XY coordinates and click it
    pyautogui.click('button.png')   # Find where button.png appears on the screen and click it

    pyautogui.move(0, 10)       # Move mouse 10 pixels down from its current position
    pyautogui.doubleClick()     # Double click the mouse
    pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad)   # Use tweening/easing function to move mouse over 2 seconds

    pyautogui.write('Hello world!', interval=0.25)  # type with quarter-second pause in between each key
    pyautogui.press('esc')      # Press the Esc key. ALL key names are in pyautogui.KEY_NAMES

    pyautogui.keyDown('shift')  # Press the Shift key down and hold it
    pyautogui.press(['left', 'left', 'left', 'left'])   # Press the left arrow key 4 times
    pyautogui.keyUp('shift')    # Let go of the Shift key

    pyautogui.hotkey('ctrl', 'c')   # Press the Ctrl-C hotkey combination

    pyautogui.alert('This is the message to display.')  # Make an alert box appear and pause the program until OK is clicked


def get_driver():
    return webdriver.Chrome(executable_path=r'C:\Program Files (x86)\__portable-apps\chromedriver.exe')

# Extract session id and url from driver object
def get_current_session(driver):
    url = driver.command_executor._url      #"http://127.0.0.1:60622/hub"
    session_id = driver.session_id          #'4e167f26-dc1d-4f51-a207-f761eaf73c31'  
    return (url, session_id)

def selenium_demo():
    print("FUNCTION: selenium_demo()")

    # Open a driver:
    driver = get_driver()
    # Get session id and url from driver object
    _url, _id = get_current_session(driver)
    print("url: '{}'         session_id: '{}'", _url, _id)
    
    bro = attach_to_session(_url, _id)
    bro.get('http://www.firefox.com/')

    # Use these two parameters to connect to your driver:
    #driver = webdriver.Remote(command_executor=_url,desired_capabilities={})
    #driver.session_id = _id
    # And driver is connected to your existing browser, so try opening a site:
    #driver.get("http://www.amazon.com")

    sys.exit()

    # Optional argument : if not specified WebDriver will search your system PATH environment variable for locating the chromedriver
    #driver = webdriver.Chrome(executable_path=r'C:\path\to\chromedriver.exe')
    #driver = webdriver.Firefox()
    driver = get_driver()
    
    # Navigate url
    driver.get("http://www.bing.com")

    # Enter "webdriver" text and perform "ENTER" keyboard action
    driver.find_element_by_name("q").send_keys("What is valentine"+Keys.ENTER)

    driver.get('https://www.google.com')
    print("Page Title is : %s" %driver.title)
    driver.quit()
    
    sys.exit()

    options = Options()
    # Browser Location
    #options.binary_location = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'
    options.binary_location = r'C:\Program Files (x86)\BraveSoftware\Brave-Browser\Application'
    # Driver Location (i.e. "chromedriver.exe")
    #driver_path = '/usr/local/bin/chromedriver'
    driver_path = r'C:\Program Files (x86)\__portable-apps\chromedriver.exe'

    drvr = webdriver.Chrome(options = options, executable_path = driver_path)
    drvr.get('https://stackoverflow.com')



if __name__ == "__main__":

    #pyautogui_demo()
    
    selenium_demo()
    