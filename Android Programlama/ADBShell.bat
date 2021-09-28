@ECHO OFF
D:
cd D:\Program Files\Android\platform-tools

set cihazadi="emulator"
echo Cihazlar
for /f "usebackq tokens=1" %%a in (`adb devices ^| findstr /c:%cihazadi%`) do (echo Cihaz: %%a & adb -s %%a shell && exit)


PAUSE