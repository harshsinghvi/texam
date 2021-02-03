@echo off 
dir 
pyinstaller quiz.py -n quiz-windows -F  -i favicon.ico
exit 