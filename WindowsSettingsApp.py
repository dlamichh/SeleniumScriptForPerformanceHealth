import time
import os
import pyautogui
from pywinauto.application import Application
from pywinauto import Desktop

# Function to open the Windows Settings app
def open_application(applicationOSName):
    # Open the Settings app using the Windows shell command
    os.system(f'start {applicationOSName}')

def click_element(class_name, title, button_title):
    # Wait for the specified app window to be available
    app_window = Desktop(backend="uia").window(class_name=class_name, title=title)
    app_window.wait('visible', timeout=10)

    # Find the specified button and click it
    button = app_window.child_window(title=button_title, control_type="Text")
    button.click_input()


def input_text_on_form(class_name, title, control_title, text_input):
    # Wait for the specified app window to be available
    app_window = Desktop(backend="uia").window(class_name=class_name, title=title)
    app_window.wait('visible', timeout=10)

    # Print available child windows to find the correct control_title
    # print(app_window.print_control_identifiers())
    
    # Find the specified button and click it
    button = app_window.child_window(title=control_title, control_type="Text")
    button.click_input()
    button.type_keys(text_input)
    
def send_keyboard_form(keys):
    pyautogui.write(keys)

def send_keyboard_press(keys):
    pyautogui.press(keys)

def send_multi_keyboard_input(keys):
    print(keys)
    pyautogui.hotkey(keys)

def send_keys_combination(key1, key2):
    # Convert key names to lowercase
    key1 = key1.lower()
    key2 = key2.lower()

    # Send the combination of keys
    pyautogui.keyDown(key1)
    pyautogui.keyDown(key2)
    pyautogui.keyUp(key2)
    pyautogui.keyUp(key1)

def print_out_child_elements(class_name, title):
    # Wait for the specified app window to be available
    app_window = Desktop(backend="uia").window(class_name=class_name, title=title)
    app_window.wait('visible', timeout=10)
    print(app_window.print_control_identifiers())

# Example usage:
# Input email address in the login form of the application
#input_text_on_form("ApplicationFrameWindow", "Application Title", "example@example.com")

# Input a custom text in the Notepad app
#input_text_on_form("Notepad", "", None)

	
# Main script
if __name__ == "__main__":
    # open_application('ms-settings:')
    #input_text_on_form("ApplicationFrameWindow", "Settings", "Find a setting", "Sound")
    #click_element("ApplicationFrameWindow", "Settings", "Display")
    #send_keyboard_press("Enter")
    send_keys_combination("win", "c")



