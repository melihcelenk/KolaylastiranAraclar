@echo off
REM Android geliştirmede Wi-Fi üzerinden Debug yapmak için hızlı bağlantı sağlayan batch dosyası
REM kullanılan IP yerine Android cihazınıza yönlendiriciniz üzerinden atadığınız sabit IP adresini giriniz

cd\
cd d:
cd D:\Program Files\Android\platform-tools

set /p Input=Port giriniz: 

adb connect 192.168.1.3:%Input%

:End
cmd /k
