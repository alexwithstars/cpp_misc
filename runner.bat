@echo off
setlocal enabledelayedexpansion

set flag=%1
set compile=%2
set input=%3
set output=%4
set res=

if not defined compile (
	echo Not file provided or wrong syntax
	exit /b 1
)
if not exist %compile%.* (
	echo file %compile% doesn't exist
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
g++ %flag% %compile%.* -o %compile%
if errorlevel 1 (
	exit /b 1
)
echo runing...
%res%
del %compile%.exe