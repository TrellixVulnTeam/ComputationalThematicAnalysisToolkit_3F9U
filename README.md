# Computational Thematic Analysis Toolkit

## Installation Instructions

To Access most recent version: https://github.com/rpgauthier/ComputationalThematicAnalysisToolkit/releases/latest

Installers avaliable for Windows 10 x64 and OSX 

## To Modify or Build using pip on Windows and OSX
Download or Fork repository
Open src folder in an IDE (tested in VS Code)

### Build Commands
#### Windows:
1) pyinstaller pyinstaller-Windows10x64.spec --additional-hooks-dir=.
2) run & compile innosetup_Windows10x64.iss
#### OSX running an intel chip:
1) change paths in pyinstaller-OSX.spec to where your python site-packages are installed
2) python -m PyInstaller --windowed --additional-hooks-dir=. pyinstaller-OSX.spec
3) run & build packages_OSX_x86_64.pkgproj
### OSX running an M1 chip:
1) change paths in pyinstaller-OSX.spec to where your python site-packages are installed
2) python -m PyInstaller --windowed --additional-hooks-dir=. pyinstaller-OSX.spec
3) run & build packages_OSX_arm64.pkgproj

### Needed applications
- python 3.9
- pyinstaller 4.5.1 - For Windows
- Inno Setup Compiler - For Windows
- packages - For OSX

### Needed Packages (there may be others)
- pip install psutil
- pip install wxPython
- pip install pandas
- pip install gensim
- pip install bitermplus
- pip install spacy
- pip install nltk
- pip install tweepy
- pip install chardet
- pip install dateparser
- pip install jsonpickle
- pip install wordcloud
- pip install squarify
- pip install networkx
- pip install pyinstaller
- pip install pytz
- pip install lxml
- pip install xmlschema
- pip install scikit-learn==1.0.1

### Additional Steps
- python -m spacy download fr_core_news_sm
- python -m spacy download en_core_web_sm
