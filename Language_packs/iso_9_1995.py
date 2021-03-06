# -*- coding: utf-8 -*-

# Official in most countries in the world.
# 
# Standard ISO 9:1995
# In Russia referred to as GOST 7.79-2000 System A
#
# more details:
# [ISO 9 #ISO 9:1995](https://en.wikipedia.org/wiki/ISO_9#ISO_9:1995)
#
# Attention: Converting back from romanized cyrillic to cyrillic is supported.

ISO_9_1995 = (
    ('А', 'A'), 
    ('а', 'a'), 
    ('Ӓ', '\u00C4'), 
    ('ӓ', '\u00E4'), 
    ('Ӓ̄', '\u00C4' + '\u0323'), 
    ('ӓ̄', '\u00E4' + '\u0323'), 
    ('Ӑ', '\u0102'), 
    ('ӑ', '\u0103'), 
    ('А̄', '\u0100'), 
    ('а̄', '\u0101'), 
    ('Ӕ', '\u00C6'), 
    ('ӕ', '\u00E6'), 
    ('А́', '\u00C1'), 
    ('а́', '\u00E1'), 
    ('А̊', '\u00C5'), 
    ('а̊', '\u00E5'), 
    ('Б', 'B'), 
    ('б', 'b'), 
    ('В', 'V'), 
    ('в', 'v'), 
    ('Г', 'G'), 
    ('г', 'g'), 
    ('Ѓ', '\u01F4'), 
    ('ѓ', '\u01F5'), 
    ('Ғ', '\u0120'), 
    ('ғ', '\u0121'), 
    ('Ҕ', '\u011E'), 
    ('ҕ', '\u011F'), 
    ('Һ', '\u1E24'), 
    ('һ', '\u1E25'), 
    ('Д', 'D'), 
    ('д', 'd'), 
    ('Ђ', '\u0110'), 
    ('ђ', '\u0111'), 
    ('Е', 'E'), 
    ('е', 'e'), 
    ('Ӗ', '\u0114'), 
    ('ӗ', '\u0115'), 
    ('Ё', '\u00CB'), 
    ('ё', '\u00EB'), 
    ('Є', '\u00CA'), 
    ('є', '\u00EA'), 
    ('Ж', '\u017D'), 
    ('ж', '\u017E'), 
    ('Җ', '\u017D' + '\u0326'), # 017D+0327
    ('җ', '\u017E' + '\u0326'), # 017E+0327
    ('Ӝ', 'Z' + '\u0304'), 
    ('ӝ', 'z' + '\u0304'), 
    ('Ӂ', 'Z' + '\u0306'), 
    ('ӂ', 'z' + '\u0306'), 
    ('З', 'Z'), 
    ('з', 'z'), 
    ('Ӟ', 'Z' + '\u0308'), 
    ('ӟ', 'z' + '\u0308'), 
    ('Ӡ', '\u0179'), 
    ('ӡ', '\u017A'), 
    ('Ѕ', '\u1E90'), 
    ('ѕ', '\u1E91'), 
    ('И', 'I'), 
    ('и', 'i'), 
    ('Ӣ', '\u012A'), 
    ('ӣ', '\u012B'), 
    ('И́', '\u00CD'), 
    ('и́', '\u00ED'), 
    ('Ӥ', '\u00CE'), 
    ('ӥ', '\u00EE'), 
    ('Й', 'J'), 
    ('й', 'j'), 
    ('І', '\u00CC'), 
    ('і', '\u00EC'), 
    ('Ї', '\u00CF'), 
    ('ї', '\u00EF'), 
    ('І̄', '\u01CF'), 
    ('і̄', '\u01D0'), 
    ('Ј', 'J' + '\u030C'), 
    ('ј', '\u01F0'), 
    ('Ј̵', 'J' + '\u0301'), 
    ('ј̵', 'j' + '\u0301'), 
    ('К', 'K'), 
    ('к', 'k'), 
    ('Ќ', '\u1E30'), 
    ('ќ', '\u1E31'), 
    ('Ӄ', '\u1E32'), 
    ('ӄ', '\u1E33'), 
    ('Ҝ', 'K' + '\u0302'), 
    ('ҝ', 'k' + '\u0302'), 
    ('Ҡ', '\u01E8'), 
    ('ҡ', '\u01E9'), 
    ('Ҟ', 'K' + '\u0304'), 
    ('ҟ', 'k' + '\u0304'), 
    ('Қ', 'K' + '\u0326'), # '\u0136', 
    ('қ', 'k' + '\u0326'), # '\u0137', 
    ('К̨', 'K' + '\u0300'), 
    ('к̨', 'k' + '\u0300'), 
    ('Ԛ', 'Q'), 
    ('ԛ', 'q'), 
    ('Л', 'L'), 
    ('л', 'l'), 
    ('Љ', 'L' + '\u0302'), 
    ('љ', 'l' + '\u0302'), 
    ('Ԡ', 'L' + '\u0326'), # '\u013B', 
    ('ԡ', 'l' + '\u0326'), # '\u013C
    ('М', 'M'), 
    ('м', 'm'), 
    ('Н', 'N'), 
    ('н', 'n'), 
    ('Њ', 'N' + '\u0302'), 
    ('њ', 'n' + '\u0302'), 
    ('Ң', 'N' + '\u0326'), # '\u0145', 
    ('ң', 'n' + '\u0326'), # '\u0146',  
    ('Ӊ', '\u1E46'), 
    ('ӊ', '\u1E47'), 
    ('Ҥ', '\u1E44'), 
    ('ҥ', '\u1E45'), 
    ('Ԋ', '\u01F8'), 
    ('ԋ', '\u01F9'), 
    ('Ԣ', '\u0143'), 
    ('ԣ', '\u0144'), 
    ('Ӈ', '\u0147'), 
    ('ӈ', '\u0148'), 
    ('Н̄', 'N' + '\u0304'), 
    ('н̄', 'n' + '\u0304'), 
    ('О', 'O'), 
    ('о', 'o'), 
    ('Ӧ', '\u00D6'), 
    ('ӧ', '\u00F6'), 
    ('Ө', '\u00D4'), 
    ('ө', '\u00F4'), 
    ('Ӫ', '\u0150'), 
    ('ӫ', '\u0151'), 
    ('Ӧ̄', '\u00D6' + '\u0323'), 
    ('о̄̈', '\u00F6' + '\u0323'), 
    ('Ҩ', '\u00D2'), 
    ('ҩ', '\u00F2'), 
    ('О́', '\u00D3'), 
    ('о́', '\u00F3'), 
    ('О̄', '\u014C'), 
    ('о̄', '\u014D'), 
    ('Œ', '\u0152'), 
    ('œ', '\u0153'), 
    ('П', 'P'), 
    ('п', 'p'), 
    ('Ҧ', '\u1E54'), 
    ('ҧ', '\u1E55'), 
    ('Ԥ', 'P' + '\u0300'), 
    ('ԥ', 'p' + '\u0300'), 
    ('Р', 'R'), 
    ('р', 'r'), 
    ('С', 'S'), 
    ('с', 's'), 
    ('Ҫ', '\u0218'), # '\u015E'
    ('ҫ', '\u0219'), # '\u015F', 
    ('С̀', 'S' + '\u0300'), 
    ('с̀', 's' + '\u0300'), 
    ('Т', 'T'), 
    ('т', 't'), 
    ('Ћ', '\u0106'), 
    ('ћ', '\u0107'), 
    ('Ԏ', 'T' + '\u0300'), 
    ('ԏ', 't' + '\u0300'), 
    ('Т̌', '\u0164'), 
    ('т̌', '\u0165'), 
    ('Ҭ', '\u021A'), #'\u0162' 
    ('ҭ', '\u021B'), #'\u0163',  
    ('У', 'U'), 
    ('у', 'u'), 
    ('Ӱ', '\u00DC'), 
    ('ӱ', '\u00FC'), 
    ('Ӯ', '\u016A'), 
    ('ӯ', '\u016B'), 
    ('Ў', '\u016C'), 
    ('ў', '\u016D'), 
    ('Ӳ', '\u0170'), 
    ('ӳ', '\u0171'), 
    ('У́', '\u00DA'), 
    ('у́', '\u00FA'), 
    ('Ӱ̄', '\u00DC' + '\u0323'), #'\u016A' + '\u0323', 
    ('ӱ̄', '\u00FC' + '\u0323'), # '\u016B' + '\u0323', 
    ('Ү', '\u00D9'), 
    ('ү', '\u00F9'), 
    ('Ұ', 'U' + '\u0307'), 
    ('ұ', 'u' + '\u0307'), 
    ('Ԝ', 'W'), 
    ('ԝ', 'w'), 
    ('Ф', 'F'), 
    ('ф', 'f'), 
    ('Х', 'H'), 
    ('х', 'h'), 
    ('Ҳ', 'H' + '\u0326'), # '\u1E28'
    ('ҳ', 'h' + '\u0326'), # '\u1E29'
    ('Ц', 'C'), 
    ('ц', 'c'), 
    ('Ҵ', 'C' + '\u0304'), 
    ('ҵ', 'c' + '\u0304'), 
    ('Џ', 'D' + '\u0302'), 
    ('џ', 'd' + '\u0302'), 
    ('Ч', '\u010C'), 
    ('ч', '\u010D'), 
    ('Ҷ', 'C' + '\u0326'), # '\u00C7', 
    ('ҷ', 'c' + '\u0326'), # '\u00E7' 
    ('Ӌ', 'C' + '\u0323'), 
    ('ӌ', 'c' + '\u0323'), 
    ('Ӵ', 'C' + '\u0308'), 
    ('ӵ', 'c' + '\u0308'), 
    ('Ҹ', '\u0108'), 
    ('ҹ', '\u0109'), 
    ('Ч̀', 'C' + '\u0300'), 
    ('ч̀', 'c' + '\u0300'), 
    ('Ҽ', 'C' + '\u0306'), 
    ('ҽ', 'c' + '\u0306'), 
    ('Ҿ', 'C' + '\u0328' + '\u0306'), 
    ('ҿ', 'c' + '\u0328' + '\u0306'), 
    ('Ш', '\u0160'), 
    ('ш', '\u0161'), 
    ('Щ', '\u015C'), 
    ('щ', '\u015D'), 
    ('Ъ', '\u02BA'), 
    ('ъ', '\u02BA'), 
    ('Ы', 'Y'), 
    ('ы', 'y'), 
    ('Ӹ', '\u0178'), 
    ('ӹ', '\u00FF'), 
    ('Ы̄', '\u0232'), 
    ('ы̄', '\u0233'), 
    ('Ь', '\u02B9'), 
    ('ь', '\u02B9'), 
    ('Э', '\u00C8'), 
    ('э', '\u00E8'), 
    ('Ә', 'A' + '\u030B'), 
    ('ә', 'a' + '\u030B'), 
    ('Ӛ', '\u00C0'), 
    ('ӛ', '\u00E0'), 
    ('Ю', '\u00DB'), 
    ('ю', '\u00FB'), 
    ('Ю̄', '\u00DB' + '\u0304'), 
    ('ю̄', '\u00FB' + '\u0304'), 
    ('Я', '\u00C2'), 
    ('я', '\u00E2'), 
    ('Ґ', 'G' + '\u0300'), 
    ('ґ', 'g' + '\u0300'), 
    ('Ѣ', '\u011A'), 
    ('ѣ', '\u011B'), 
    ('Ѫ', '\u01CD'), 
    ('ѫ', '\u01CE'), 
    ('Ѳ', 'F' + '\u0300'), 
    ('ѳ', 'f' + '\u0300'), 
    ('Ѵ', '\u1EF2'), 
    ('ѵ', '\u1EF3'), 
    ('Ӏ', '\u2021'), 
    ('ʼ', '\u0060'), 
    ('ˮ', '\u00A8'), 
    ("№", "#")
)
