# Cyrillic alphabets to latin alphabets transcriptor

For now transcriptions only to Polish

>__Polish transcription rules source:__
https://sjp.pwn.pl/zasady/X-Transliteracja-i-transkrypcja-slowianskich-alfabetow-cyrylickich;629693.html

## Requirements:

* python3.7
* virtualenv

## Instalation:

If you don't have venv installed use this command:
```
sudo apt install python3-pip
pip3 install virtualenv
```

When you have virtualenv installed, use Python 3.7 with virtual environment and install required packages:

```
virtualenv -p python3.7 venv
source venv/bin/activate
pip install -r requirements.txt
```

Run:  
`python transcriptor.py`
