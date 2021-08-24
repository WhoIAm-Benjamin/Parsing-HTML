rem Сборка .exe приложений из Python файлов

@ECHO OFF
pyinstaller -F --distpath="F:\Work\Programming\Complete programs\Parsing HTML" --name="Parsing of HTML" main.spec
set/p "s=>"