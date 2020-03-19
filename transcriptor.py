import re
import trscp_functions as tr

def get_text_from_file():
    with open('file.txt', 'r', encoding='utf-8') as ff:
        s=ff.read()
    return s

def prepere_text(in_s):
    return re.split(r'\b', in_s)

def main():
    entered_text = get_text_from_file()
    tokens_trscript_list = prepere_text(entered_text)
    
    tokens_trscript_list = tr.transcribe_ru2pl(tokens_trscript_list)
    for i in tokens_trscript_list:
        print(i,end='')
    
if __name__ == "__main__":
    main()