rm -rf dist
pyinstaller main.py -F --hiddenimport six --hiddenimport appdirs --hiddenimport packaging --hiddenimport packaging.version --hiddenimport packaging.specifiers --hiddenimport packaging.requirements
rm -rf build
cp -r assets dist/
mv dist/main dist/doctorWave.run
mv dist doctorWave
tar -cvzf doctorWave.tar.gz doctorWave
