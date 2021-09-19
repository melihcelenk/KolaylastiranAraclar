@echo off 


SETLOCAL ENABLEDELAYEDEXPANSION

SET count=1
FOR /F "tokens=* USEBACKQ" %%F IN (`netsh wlan show profiles`) DO (

	for /F "tokens=1* delims=:" %%a in ("ham[!count!]=%%F") do (echo !count! = %%b  	
		SET dizi[!count!]=%%b
	)
  
  SET /a count=!count!+1
)

echo\
set /p Input=Sayi giriniz: 
echo\

set giris=!dizi[%Input%]!
for %%a in (%giris%) do set girisBosluksuz=%%a

echo\
echo SSID:!girisBosluksuz!
echo\

set komut=netsh wlan show profile name="!girisBosluksuz!" key=clear

echo !komut!

set sonKomut=!komut! ^| findstr /C:"Key Content"

echo off

set sayi=1
FOR /F "tokens=* USEBACKQ" %%F IN (`!sonKomut!`) DO (

	for /F "tokens=1* delims=:" %%a in ("son[!sayi!]=%%F") do (
		set parola=%%b
	)
  
  SET /a sayi=!sayi!+1
)

for %%a in (%parola%) do set parolaBosluksuz=%%a
echo\
echo Parola:!parolaBosluksuz!
echo\

ENDLOCAL




:End
cmd /k