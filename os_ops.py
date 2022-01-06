import os
import subprocess as sp

paths = {
    'notepad': "/System/Applications/Notes.app",
    'calendar': "/System/Applications/Calendar.app",
    'calculator': "/System/Applications/Calculator.app"
}


def open_notepad():
    os.startfile(paths['notepad'])


def open_calendar():
    os.startfile(paths['calendar'])


def open_cmd():
    os.system('open -a Terminal .')


def open_calculator():
    sp.Popen(paths['calculator'])
