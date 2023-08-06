import os
import time
import pyautogui
from pywinauto.application import Application
from pywinauto import Desktop

# Eg: open_application('ms-settings:')
def open_application(applicationOSName):
    os.system(f'start {applicationOSName}')
    sleep_after_functions(f"Opening Application {applicationOSName}")

# Eg: click_element("ApplicationFrameWindow", "Settings", "Display", "Button")
def click_element(class_name, title, button_title, control_type):
    # Wait for the specified app window to be available
    app_window = Desktop(backend="uia").window(class_name=class_name, title=title)
    app_window.wait('visible', timeout=10)

    # Find the specified button and click it
    button = app_window.child_window(title=button_title, control_type=control_type)
    button.click_input()
    sleep_after_functions(f"Clicking Element {button_title}")

# Eg: input_text_on_form("ApplicationFrameWindow", "Settings", "Find a setting", "Text", "Sound")
def input_text_on_form(class_name, title, control_title, control_type, text_input):
    # Wait for the specified app window to be available
    app_window = Desktop(backend="uia").window(class_name=class_name, title=title)
    app_window.wait('visible', timeout=10)
    
    # Find the specified button and click it
    button = app_window.child_window(title=control_title, control_type=control_type)
    button.click_input()
    button.type_keys(text_input)
    sleep_after_functions(f"Inputing Text on Form {control_title}")

# Eg: send_keys("enter")
def send_keys(keys):
    pyautogui.press(keys)
    sleep_after_functions(f"Sending Keys {keys}")

# Eg: send_keys_combination("win", "c")
def send_keys_combination(key1, key2):
    # Convert key names to lowercase
    key1 = key1.lower()
    key2 = key2.lower()

    # Send the combination of keys
    pyautogui.keyDown(key1)
    pyautogui.keyDown(key2)
    pyautogui.keyUp(key2)
    pyautogui.keyUp(key1)
    sleep_after_functions(f"Sending Keys Combinations {key1} + {key2}")

# Eg: print_out_child_elements("ApplicationFrameWindow", "Settings")
def print_out_child_elements(class_name, title):
    # Wait for the specified app window to be available
    app_window = Desktop(backend="uia").window(class_name=class_name, title=title)
    app_window.wait('visible', timeout=10)
    print(app_window.print_control_identifiers())

def set_sleep_seconds():
    global sleep_seconds
    sleep_seconds = 2

def sleep_after_functions(function):
    set_sleep_seconds()
    print(f"Sleeping {sleep_seconds}  seconds after {function}")
    time.sleep(sleep_seconds)