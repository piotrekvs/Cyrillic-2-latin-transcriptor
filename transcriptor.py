import re
import time
import trscp_functions as tr
import Language_packs.Languages_data as Ldata

def get_text_from_file():
    with open('Test/file.txt', mode='r', encoding='utf-8') as ff:
        s=ff.read()
    return s

def main():
    entered_text = get_text_from_file()
    
    #tokens_trscript_list = tr.seperate_words(entered_text)
    #tokens_trscript_list = tr.transcribe_ru2pl(tokens_trscript_list)
    #for i in tokens_trscript_list:
    #    print(i,end='')
    
    # Class
    ru_pl_translit = tr.SimpleTransliterationToLatin(Ldata.Cyrill2Latin_ISO_9_1995, True)
    end_text = ru_pl_translit.Cyrillic2Latin(entered_text)
    
    
    start_execution_timer = time.process_time() # TIMER FOR TESTS

    
    end_text = ru_pl_translit.Latin2Cyrillic(end_text)
    
    stop_execution_timer = time.process_time() # TIMER FOR TESTS
    
    
    print(end_text) # Print transliteration
    print("\n", (stop_execution_timer - start_execution_timer) * 100 , "ms") # TIMER FOR TESTS
    
if __name__ == "__main__":
    main()