text = '''({
  "@attributes": { "class": "adminToolsLine" },
  "#text": [
    "\n            ",
    "\n            ",
    "\n            ",
    "\n            ",
    "\n            ",
    "\n            ",
    "\n            ",
    "\n          "
  ],
  "TD": [
    {
      "@attributes": {
        "class": "adminToolsBox1",
        "type": "text",
        "name": "Artist",
        "id": "Artist"
      },
      "#text": "\n              Artist02\n            "
    },
    {
      "@attributes": {
        "class": "adminToolsBox1",
        "type": "text",
        "name": "Album",
        "id": "Album"
      },
      "#text": "\n              ALbum from Artist02\n            "
    },
    {
      "@attributes": {
        "class": "adminToolsBox2",
        "type": "text",
        "name": "Track",
        "id": "Track"
      },
      "#text": "\n              ihnj\n            "
    },
    {
      "@attributes": {
        "class": "adminToolsBox3",
        "type": "text",
        "name": "Genre",
        "id": "Genre"
      },
      "#text": "\n   Indie\n            "
    },
    {
      "@attributes": {
        "class": "adminToolsBox3",
        "type": "text",
        "name": "Length",
        "id": "Length"
      },
      "#text": "\n              9:32\n            "
    },
    {
      "@attributes": {
        "class": "adminToolsBox1",
        "type": "text",
        "name": "Infos",
        "id": "Infos"
      },
      "#text": "\n              injojn k\n            "
    },
    {
      "@attributes": {
        "class": "adminPlaylistCheckbox",
        "name": "checkboxS",
        "id": "checkboxS"
      },
      "#text": ["\n              ", "\n            "],
      "INPUT": { "@attributes": { "type": "checkbox", "name": "checkboxLine" } }
    }
  ]
},
{
  "@attributes": { "class": "adminToolsLine" },
  "#text": [
    "\n            ",
    "\n            ",
    "\n            ",
    "\n            ",
    "\n            ",
    "\n            ",
    "\n            ",
    "\n          "
  ],
  "TD": [
    {
      "@attributes": {
        "class": "adminToolsBox1",
        "type": "text",
        "name": "Artist",
        "id": "Artist"
      },
      "#text": "\n              Artist02\n            "
    },
    {
      "@attributes": {
        "class": "adminToolsBox1",
        "type": "text",
        "name": "Album",
        "id": "Album"
      },
      "#text": "\n              ALbum from Artist02\n            "
    },
    {
      "@attributes": {
        "class": "adminToolsBox2",
        "type": "text",
        "name": "Track",
        "id": "Track"
      },
      "#text": "\n              morceau 2\n            "
    },
    {
      "@attributes": {
        "class": "adminToolsBox3",
        "type": "text",
        "name": "Genre",
        "id": "Genre"
      },
      "#text": "\n   Punk\n            "
    },
    {
      "@attributes": {
        "class": "adminToolsBox3",
        "type": "text",
        "name": "Length",
        "id": "Length"
      },
      "#text": "\n              09898:9809\n            "
    },
    {
      "@attributes": {
        "class": "adminToolsBox1",
        "type": "text",
        "name": "Infos",
        "id": "Infos"
      },
      "#text": "\n              INJKBIHNJK \n            "
    },
    {
      "@attributes": {
        "class": "adminPlaylistCheckbox",
        "name": "checkboxS",
        "id": "checkboxS"
      },
      "#text": ["\n              ", "\n            "],
      "INPUT": { "@attributes": { "type": "checkbox", "name": "checkboxLine" } }
    }
  ]
},
{
  "@attributes": { "class": "adminToolsLine" },
  "#text": [
    "\n            ",
    "\n            ",
    "\n            ",
    "\n            ",
    "\n            ",
    "\n            ",
    "\n            ",
    "\n          "
  ],
  "TD": [
    {
      "@attributes": {
        "class": "adminToolsBox1",
        "type": "text",
        "name": "Artist",
        "id": "Artist"
      },
      "#text": "\n              Artist02\n            "
    },
    {
      "@attributes": {
        "class": "adminToolsBox1",
        "type": "text",
        "name": "Album",
        "id": "Album"
      },
      "#text": "\n              ALbum from Artist02\n            "
    },
    {
      "@attributes": {
        "class": "adminToolsBox2",
        "type": "text",
        "name": "Track",
        "id": "Track"
      },
      "#text": "\n              ihnj\n            "
    },
    {
      "@attributes": {
        "class": "adminToolsBox3",
        "type": "text",
        "name": "Genre",
        "id": "Genre"
      },
      "#text": "\n     Indie\n            "
    },
    {
      "@attributes": {
        "class": "adminToolsBox3",
        "type": "text",
        "name": "Length",
        "id": "Length"
      },
      "#text": "\n              9:32\n            "
    },
    {
      "@attributes": {
        "class": "adminToolsBox1",
        "type": "text",
        "name": "Infos",
        "id": "Infos"
      },
      "#text": "\n              injojn k\n            "
    },
    {
      "@attributes": {
        "class": "adminPlaylistCheckbox",
        "name": "checkboxS",
        "id": "checkboxS"
      },
      "#text": ["\n              ", "\n            "],
      "INPUT": { "@attributes": { "type": "checkbox", "name": "checkboxLine" } }
    }
  ]
})

'''

def get_section_i(text):
        text = text.replace('''"TD":  "TD"''', '''"TD":''')
        beginning = text.find("TD")
        text = text.replace("TD", "", 1)
        end = text[beginning:].find("TD")
        #print("text["+str(beginning)+" : "+str(end)+"]")
        #print(len(text[beginning:end]))
        #print(text[beginning:end])
        return text[beginning:end]

def remove_section_i(text):
        text = text.replace('''"TD":  "TD"''', '''"TD":''')
        beginning = text.find("TD")
        text = text.replace("TD", "", 1)
        end = text[beginning:].find("TD")
        return text[end:]

def parse_request(text):
    result = ""
    lines = []
    main = text[text.find('''"TD"'''):text.find('''})''')]+"TD_THE_END"
    tracks = main.count("TD")
    for i in range(0, 3):
        print("------------------------------------------------------------")
        section_i = get_section_i(main)
        ##################
        item = section_i_to_array(section_i)
        item[3] = item[3].replace(" ", "")
        print(item)
        ##################
        main = remove_section_i(main)
        print("------------------------------------------------------------")
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
    beginning = text.find('''"@attributes": {''')
    text = text.replace('''"@attributes": {''', "", 1)
    end = text[beginning:].find('''"@attributes": {''')
    return text[beginning:end]

def remove_sub_section_i(text):
    beginning = text.find('''"@attributes": {''')
    text = text.replace('''"@attributes": {''', "", 1)
    end = text[beginning:].find('''"@attributes": {''')
    return text[end:]


def clean_sub_section(item):
    #print("\n\n item:\n"+item+"\n")
    beginning = item.find('''"#text": "''')
    item = item.replace('''"#text": "''', "", 1)
    final_item = item[beginning:].replace(''' "''', "").replace('''\n''', "").replace("  ", "")
    #print("======> "+final_item)
    return final_item





parse_request(text)
