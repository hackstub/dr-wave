rm -rf dist
pyinstaller main.py -F --hiddenimport six --hiddenimport appdirs --hiddenimport packaging --hiddenimport packaging.version --hiddenimport packaging.specifiers --hiddenimport packaging.requirements --windowed
rm -rf build
cp -r assets dist/
mv dist/main dist/doctorWave.run
rm -rf doctorWave
mv dist doctorWave
cp highscore.txt doctorWave/
rm -rf doctorWave/main.app
tar -cvzf doctorWave.tar.gz doctorWave
