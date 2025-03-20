
import sys

if sys.platform != "win32":
    raise ImportError("pywet is *currently* only supported on Windows")

import win32api
import win32con
import win32clipboard
import win32gui
import win32process


def main() -> None:
    print("Hello from pywet!")
    # win32api.ClipCursor((100, 100, 200, 200))
    # win32api.Beep(1000, 1000)  #
    # win32api.ClipCursor((0, 0, 0, 0))
    # for G9 ultrawide top left is (0,0), bottom right is (5119, 1439)
    print(win32api.GetCursorPos())
    print(win32api.GetDiskFreeSpaceEx("C:\\"))
    # device name
    print(win32api.GetDomainName())
    print(win32api.GetKeyboardState())
    # TIL that windows 11 is still windows 10
    print(win32api.GetVersionEx())

    # Play the system exclamation sound
    # win32api.MessageBeep(win32con.MB_ICONEXCLAMATION)

    # message box
    # win32api.MessageBox(0, "Hello", "Hello", win32con.MB_OK)

    # move cursor
    # win32api.SetCursorPos((100, 100))
    win32clipboard.OpenClipboard()
    print(win32clipboard.GetClipboardData())
    win32clipboard.SetClipboardText(
        "Helloooooooooooooo", win32clipboard.CF_UNICODETEXT)
    win32clipboard.CloseClipboard()

    # get foreground window
    # hwnd = win32gui.GetForegroundWindow()
    # move window to top left
    # win32gui.SetWindowPos(hwnd, None, 0, 0, 0, 0, win32con.SWP_NOSIZE)
    def win_enum_callback(hwnd, context):
        if not win32gui.IsWindowVisible(hwnd):
            return
        print(hex(hwnd), f'Title: "{win32gui.GetWindowText(hwnd)}"')
        print(hex(hwnd), f'Class: "{win32gui.GetClassName(hwnd)}"')
        thread_id, process_id = win32process.GetWindowThreadProcessId(hwnd)
        print(hex(hwnd), f'Thread ID: {thread_id}, Process ID: {process_id}')

    win32gui.EnumWindows(win_enum_callback, None)
