
pushd src\noteslot && (

    pyinstaller noteslot.spec --noconfirm --workpath=../../build --distpath=../../dist
    popd
    xcopy.exe resources\icons\noteslot.ico dist\noteslot\
)
