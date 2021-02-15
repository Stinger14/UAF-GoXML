./Scripts/activate
pyinstaller src/wsgi.py -F `
--name "UAF-GOXML" `
--add-data "src\data\*;data" `
--add-data "src\data\*.xlsx;data" `
--add-data "src\data\*.xml;data" `
--hidden-import waitress `
--clean
