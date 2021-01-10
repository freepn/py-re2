@echo off

set WHEEL=%1
set DEST_DIR=%2

pip install pefile machomachomangler
python ci/wheel_repair.py %WHEEL% -w %DEST_DIR%
