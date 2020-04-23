# Cyrillic alphabets to latin alphabets transcriptor

__Available transliterations__  
ISO 9:1995
GOST 7.79 System B (Official Russian & Belarusian, Unofficial Ukrainian)
Official Bulgarian
Official Macedonian
Official Serbian

__Available transcriptions__  
Russian to Polish (PWN)

>__Polish transcription rules source__  
<https://sjp.pwn.pl/zasady/X-Transliteracja-i-transkrypcja-slowianskich-alfabetow-cyrylickich;629693.html>
<http://ksng.gugik.gov.pl/pliki/latynizacja/rosyjski.pdf>  
>__International transliteration rules__  
<https://www.gov.uk/government/publications/romanization-systems>
<http://transliteration.eki.ee>
<https://en.wikipedia.org/wiki/ISO_9>
<https://en.wikipedia.org/wiki/Scientific_transliteration_of_Cyrillic>
<https://en.wikipedia.org/wiki/GOST_16876-71>

## Requirements

* python3.6
* virtualenv

## Instalation

If you don't have venv installed use this command:

```bash
sudo apt install python3-pip
pip3 install virtualenv
```

When you have virtualenv installed, use Python 3.6 with virtual environment and install required packages:

```bash
virtualenv -p python3.6 venv
source venv/bin/activate
pip install -r requirements.txt
```

Run:  
`python transcriptor.py`
