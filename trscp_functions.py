import re

def transcribe_ru2pl(text2t):
    # Complex transcription
    ru_vowels= ('А', 'а', 'Э', 'э', 'Ы', 'ы', 'У', 'у', 'О', 'о', 
                'Я', 'я', 'Е', 'е', 'Ё', 'ё', 'Ю', 'ю', 'И', 'и')
    ru_silent= ('Ъ', 'ъ', 'Ь', 'ь')
    # Ru je jo
    ru_second_je_jo= ('Ж', 'ж', 'Л', 'л', 'Ч', 'ч', 'Ш', 'ш', 'Щ', 'щ')
    ru_second_je_only= ('Ц', 'ц')
    ru2pl_first_je_jo= {'Е':'Je','е':'je', 'Ё':'Jo', 'ё':'jo'}
    ru2pl_second_je_jo= {'Е':'E','е':'e', 'Ё':'O', 'ё':'o'}
    ru2pl_other_je_jo= {'Е':'Ie','е':'ie', 'Ё':'Io', 'ё':'io'} 
    # Ru ju ja
    ru_second_ju_ja= ('Л', 'л')
    ru2pl_first_ju_ja= {'Ю':'Ju', 'ю':'ju', 'Я':'Ja', 'я':'ja'}
    ru2pl_second_ju_ja= {'Ю':'U', 'ю':'u', 'Я':'A', 'я':'a'}
    ru2pl_other_ju_ja= {'Ю':'Iu', 'ю':'iu', 'Я':'Ia', 'я':'ia'}
    # Ru ji
    ru_second_ji= ('Ь', 'ь')
    ru_third_ji= ('Ж', 'ж', 'Ш', 'ш', 'Ц', 'ц')
    ru2pl_other_ji= {'И':'I', 'и':'i'}
    ru2pl_second_ji= {'И':'Ji', 'и':'ji'}
    ru2pl_third_ji= {'И':'Y', 'и':'y'}
    # Ru l
    ru_first_l= ('Е', 'е', 'Ё', 'ё', 'И', 'и', 'Ь', 'ь', 'Ю', 'ю', 'Я', 'я')
    ru2pl_first_l= {'Л':'L', 'л':'l'}
    ru2pl_second_l= {'Л':'Ł', 'л':'ł'}
    # Ru soft
    ru2pl_first_soft={'Ь':"'", 'ь':"'"}
    ru_second_soft= ('Ж', 'ж', 'Л', 'л', 'Ч', 'ч', 'Ш', 'ш', 'Щ', 'щ')

    # Simple transliteration
    ru2pl_lexicon= {'А':'A', 'а':'a', 'Б':'B', 'б':'b', 'В':'W', 'в':'w', 
                    'Г':'G', 'г':'g', 'Д':'D', 'д':'d', 'Ж':'Ż', 'ж':'ż',
                    'З':'Z', 'з':'z', 'Й':'J', 'й':'j', 'К':'K', 'к':'k',
                    'М':'M', 'м':'m', 'Н':'N', 'н':'n', 'О':'O', 'о':'o',
                    'П':'P', 'п':'p', 'Р':'R', 'р':'r', 'С':'S', 'с':'s',
                    'Т':'T', 'т':'t', 'У':'U', 'у':'u', 'Ф':'F', 'ф':'f',
                    'Х':'Ch', 'х':'ch', 'Ц':'C', 'ц':'c', 'Ч':'Cz', 'ч':'cz',
                    'Ш':'Sz', 'ш':'sz', 'Щ':'Szcz', 'щ':'szcz', 'Ы':'Y', 'ы':'y',
                    'Э':'E', 'э':'e', 'Ъ':'', 'ъ':''}
    
    trscp_list=[]

    def ru2pl_complex(word):
        new_word = ''
        # First letter
        if word[0] in ru2pl_first_je_jo.keys():
            new_word = ru2pl_first_je_jo[str(word[0])]
        elif word[0] in ru2pl_first_ju_ja.keys():
            new_word = ru2pl_first_ju_ja[str(word[0])]
        elif word[0] in ru2pl_other_ji.keys():
            new_word = ru2pl_other_ji[str(word[0])]
        elif word[0] in ru2pl_first_l.keys():
            if (len(word) > 1 and word[1] in ru_first_l):
                new_word = ru2pl_first_l[str(word[0])]
            else:
                new_word = ru2pl_second_l[str(word[0])]
        elif word[0] in ru2pl_first_soft.keys():
            pass
        else: new_word = word[0]
        # Following letters
        for i in range(1, len(word)):
            if word[i] in ru2pl_first_je_jo.keys(): # Ru je jo
                if (word[i-1] in ru_vowels or word[i-1] in ru_silent):
                    new_word += ru2pl_first_je_jo[str(word[i])]
                elif word[i-1] in ru_second_je_jo:
                    new_word += ru2pl_second_je_jo[str(word[i])]
                elif (word[i-1] in ru_second_je_only and word[i].lower()=='ё'):
                    new_word += ru2pl_second_je_jo[str(word[i])]
                else:
                    new_word += ru2pl_other_je_jo[str(word[i])]
                
            elif word[i] in ru2pl_first_ju_ja.keys(): # Ru ju ja
                if (word[i-1] in ru_vowels or word[i-1] in ru_silent):
                    new_word += ru2pl_first_ju_ja[str(word[i])]
                elif word[i-1] in ru_second_ju_ja:
                    new_word += ru2pl_second_ju_ja[str(word[i])]
                else:
                    new_word += ru2pl_other_ju_ja[str(word[i])]

            elif word[i] in ru2pl_second_ji.keys(): # Ru ji
                if word[i-1] in ru_second_ji:
                    new_word += ru2pl_second_ji[str(word[i])]
                elif word[i-1] in ru_third_ji:
                    new_word += ru2pl_third_ji[str(word[i])]
                else:
                    new_word += ru2pl_other_ji[str(word[i])]

            elif word[i] in ru2pl_first_l.keys(): # Ru l
                if i == len(word)-1:
                    new_word += ru2pl_second_l[str(word[-1])]
                elif word[i+1] in ru_first_l:
                    new_word += ru2pl_first_l[str(word[i])]
                else:
                    new_word += ru2pl_second_l[str(word[i])]
            
            elif word[i] in ru2pl_first_soft.keys(): # Soft
                if word[i-1] in ru_second_soft:
                    pass
                else:
                    new_word += ru2pl_first_soft[str(word[i])] 

            else:
                new_word += word[i]
        return new_word

    for word in text2t:
        if re.search(r'\w', word):
            # Complex transcription
            word = ru2pl_complex(word)
            # Simple transliteration
            new_word = ''
            for i in range(len(word)):
                new_word += ru2pl_lexicon[str(word[i])] if word[i] in ru2pl_lexicon.keys() else word[i]
            trscp_list.append(new_word)

        else:
            trscp_list.append(word)
    return trscp_list