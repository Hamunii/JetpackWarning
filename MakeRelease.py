#!/usr/bin/env python
import os
import json
from zipfile import ZipFile

# I don't even know python and I made this to automate the process of making a zip file. So much time saved, yay!

thisPath = os.getcwd()
metadataFile = open('manifest.json')
metadata = json.load(metadataFile)
metadataFile.close()
releasePath = f'{thisPath}/releases/JetpackWarning{metadata['version_number']}.zip'

if not os.path.exists(f'{thisPath}/releases'):
   os.mkdir('releases')

if os.path.exists(releasePath):
    print(f'A release with the version number {metadata['version_number']} already exists!')
    exit()

print('Making a zip file...')

with ZipFile(releasePath, 'w') as zip_object:
   # Adding files that need to be zipped
   zip_object.write(f'{thisPath}/bin/Release/netstandard2.1/JetpackWarning.dll', '/JetpackWarning.dll')
   zip_object.write(f'{thisPath}/icon.png', '/icon.png')
   zip_object.write(f'{thisPath}/README.md', '/README.md')
   zip_object.write(f'{thisPath}/CHANGELOG.md', '/CHANGELOG.md')
   zip_object.write(f'{thisPath}/manifest.json', '/manifest.json')

if os.path.exists(releasePath):
   print(f'Zip file created at "releases/JetpackWarning{metadata['version_number']}.zip"')
else:
   print(f'Zip file could NOT be created at "{releasePath}"!!1')