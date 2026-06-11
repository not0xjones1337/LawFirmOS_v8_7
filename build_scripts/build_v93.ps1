cd ..

python -m PyInstaller ^
--onedir ^
--noconsole ^
--clean ^
--add-data "runtime;runtime" ^
--add-data "app;app" ^
--add-data "logs;logs" ^
--add-data "exports;exports" ^
--paths "src" ^
src\lawfirm_os\launcher.py
