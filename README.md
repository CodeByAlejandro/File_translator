# File_translator
Created python translator to translate files using Google translate

# Installation
Install in virtual environment using following commands:
```shell
git clone https://github.com/CodeByAlejandro/File_translator.git
cd File_translator
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
```
# Usage
Run the translate.py module and pass it a text file to translate, when asked. You can tab-complete the filepath since it uses GNU readline to get the input. This means it's possible this doesn't run nativaly on Windows (I don't care). Next, choose a language from the cmd line interface using either one of the short or long names, as shown on the screen. Finally your file will be translated into a new `./translated.txt` file.
```shell
python translate.py
```

# Uninstall
Deactivate the virtual environment using the exported shell function `deactivate`:
```shell
deactivate
```
Remove the project:
```shell
cd ..
rm -rf File_translator
```
