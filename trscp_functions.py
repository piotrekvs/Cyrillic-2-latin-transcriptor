import re

class SimpleTransliterationToLatin:
    def __init__(self, trslit_table: dict, reverse: bool= False):
        self.cyrillic_to_latin = trslit_table
        
        # Create data structures for reverse transliteration
        self.latin_to_cyrillic: dict={}
        self.latin_multigraphs: dict={}
        if reverse == True:
            for key, val in self.cyrillic_to_latin.items():
                # Reverse transliteration table
                self.latin_to_cyrillic[ val ] = key
                
                # Create dictionary for multigraph processing
                # { 'first_letter' : len(multigraph) }
                if len(val) > 1:
                    if  val[0] not in self.latin_multigraphs:
                        self.latin_multigraphs[ val[0] ] = len(val)
                    elif self.latin_multigraphs[ val[0] ] < len(val):
                        self.latin_multigraphs[ val[0] ] = len(val)


    def Cyrillic2Latin(self, source_text: str):
        print("awdawd")
        end_text: str=''
        for i in range(len(source_text)):
            if source_text[i] in self.cyrillic_to_latin.keys():
                end_text += self.cyrillic_to_latin[str(source_text[i])] 
            else:
                end_text += source_text[i]
        return end_text
    
    def Latin2Cyrillic(self, source_text: str):
        end_text: str=''
        temp_multigraph: str=''
        last_length: int=0
        i = 0
        while i < len(source_text):
            if last_length == 0:
                if source_text[i] in self.latin_multigraphs:
                    temp_multigraph = source_text[i]
                    last_length = 1
                else:
                    # Basic transliteration
                    end_text += self.latin_to_cyrillic[ source_text[i] ] if source_text[i] in self.latin_to_cyrillic else source_text[i]

            else:
                ###if len(temp_multigraph) < self.latin_multigraphs[ temp_multigraph[0] ]:
                temp_multigraph = temp_multigraph + source_text[i]
                
                if temp_multigraph in self.latin_to_cyrillic:
                    last_length = len(temp_multigraph)
                
                if len(temp_multigraph) == self.latin_multigraphs[ temp_multigraph[0] ] or i+1 == len(source_text):
                    end_text += self.latin_to_cyrillic[ temp_multigraph[:last_length] ]
                    i = i - (len(temp_multigraph) - last_length)
                    temp_multigraph = ''
                    last_length = 0
            # Increase iterator
            i = i+1
        
        return end_text




def seperate_words(in_s):
    return re.split(r'(\W+)', in_s)

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