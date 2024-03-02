@echo off
setlocal enabledelayedexpansion

set compile=%1
set input=%2
set output=%3
set res=

if not defined compile (
	echo Not file provided or wrong syntax
	exit /b 1
)
if not exist %compile%.cpp (
	echo file %compile%.cpp doesn't exist
	exit /b 1
)
set res=%compile%
if defined input (
	if not exist !input! (
		echo file %input% doesn't exist
		exit /b 1
	)
	set "res=%res% < %input%"
)
if defined output (
	set "res=%res% > %output%"
)

echo compiling...
g++ %compile%.cpp -o %compile%
if errorlevel 1 (
	exit /b 1
)
echo runing...
%res%
del %compile%.exe