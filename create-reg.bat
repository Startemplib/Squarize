@echo off
rem 获取当前批处理文件的完整路径（包含驱动器）
set currentDir=%~dp0

rem 调用 Python 脚本，并将完整路径作为参数传递
create-reg.exe "%currentDir%"
