def get_section_i(text):
        beginning = text.find("TD")
        text = text.replace("TD", "", 1)
        end = text[beginning:].find("TD")
        return text[beginning:end]

def remove_section_i(text):
        text = text.replace('''"TD":  "TD"''', '''"TD":''')
        beginning = text.find("TD")
        text = text.replace("TD", "", 1)
        end = text[beginning:].find("TD")
        return text[end:]

def clean_text(text):
    text = text.replace("              ", "")
    text = text.replace('''          ''', '')
    text = text.replace("            ", "")
    text = text.replace('''\n''', "")
    text = text.replace('''\"''', "")
    return text

def parse_request(text):
    result = ""
    lines = []
    text = clean_text(text)
    main = text[text.find('''TD'''):]+"TD_THE_END"
    tracks = main.count("TD")
    for i in range(0, tracks -1):
        section_i = get_section_i(main)
        item = section_i_to_array(section_i)
        print(item)
        item[3] = item[3].replace(" ", "")
        main = remove_section_i(main)
    return result

def section_i_to_array(section_i):
    array = []
    for i in range(0, 6):
        item = get_sub_section(section_i)
        item_clean = clean_sub_section(item)
        array.append(item_clean)
        section_i = remove_sub_section_i(section_i)
    return array

def get_sub_section(text):
    beginning = text.find('''@attributes:{''')
    text = text.replace('''@attributes:{''', "", 1)
    end = text[beginning:].find('''@attributes:{''')
    return text[beginning:end]

def remove_sub_section_i(text):
    beginning = text.find('''@attributes:{''')
    text = text.replace('''@attributes:{''', "", 1)
    end = text[beginning:].find('''@attributes:{''')
    return text[end:]


def clean_sub_section(item):
    #print("\n\n item:\n"+item+"\n")
    beginning = item.find('''#text:''')
    item = item.replace('''#text:''', "", 1)
    final_item = item[beginning:].replace(''' "''', "").replace('''\n''', "").replace("  ", "").replace('''\\n''', "")
    #print("======> "+final_item)
    return final_item
