# -*- coding: utf-8 -*-

import json
import ast

p = (r''' {
  "@attributes": { "id": "tableID" },
  "#text": "\
",
  "TBODY": {
    "TR": [
      {
        "@attributes": { "class": "adminToolsLine" },
        "#text": ["\
  ", "\
  ", "\
  ", "\
  ", "\
  ", "\
  ", "\
  ", "\
"],
        "TH": [
          {
            "@attributes": {
              "class": "adminToolsBox1",
              "type": "text",
              "name": "Artist",
              "id": "Artist"
            },
            "#text": "\
    Artist\
  "
          },
          {
            "@attributes": {
              "class": "adminToolsBox1",
              "type": "text",
              "name": "Album",
              "id": "Album"
            },
            "#text": "Album"
          },
          {
            "@attributes": {
              "class": "adminToolsBox2",
              "type": "text",
              "name": "Track",
              "id": "Track"
            },
            "#text": "Track"
          },
          {
            "@attributes": {
              "class": "adminToolsBox3",
              "type": "text",
              "name": "Genre",
              "id": "Genre"
            },
            "#text": "Genre"
          },
          {
            "@attributes": {
              "class": "adminToolsBox4",
              "type": "text",
              "name": "Length",
              "id": "Length"
            },
            "#text": "\
    Length\
  "
          },
          {
            "@attributes": {
              "class": "adminToolsBox1",
              "type": "text",
              "name": "Infos",
              "id": "Infos"
            },
            "#text": "\
    Infos\
  "
          },
          {
            "@attributes": { "class": "adminToolsBox0Header" },
            "#text": "Decline"
          }
        ]
      },
      {
        "@attributes": { "class": "adminToolsLine" },
        "#text": [],
        "TD": [
          {
            "@attributes": {
              "class": "adminToolsBox1",
              "type": "text",
              "name": "Artist",
              "id": "Artist"
            },
            "#text": "Artist02"
          },
          {
            "@attributes": {
              "class": "adminToolsBox1",
              "type": "text",
              "name": "Album",
              "id": "Album"
            },
            "#text": "ALbum from Artist02"
          },
          {
            "@attributes": {
              "class": "adminToolsBox2",
              "type": "text",
              "name": "Track",
              "id": "Track"
            },
            "#text": "\
        ihnj\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox3",
              "type": "text",
              "name": "Genre",
              "id": "Genre"
            },
            "#text": "\
        Indie\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox4",
              "type": "text",
              "name": "Length",
              "id": "Length"
            },
            "#text": "\
        9:32\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox1",
              "type": "text",
              "name": "Infos",
              "id": "Infos"
            },
            "#text": "\
        injojn k\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox0Line",
              "onclick": "removeParent(this)"
            },
            "#text": "X"
          }
        ]
      },
      {
        "@attributes": { "class": "adminToolsLine" },
        "#text": [
          "\
      ",
          "\
      ",
          "\
      ",
          "\
      ",
          "\
      ",
          "\
      ",
          "\
      ",
          "\
    "
        ],
        "TD": [
          {
            "@attributes": {
              "class": "adminToolsBox1",
              "type": "text",
              "name": "Artist",
              "id": "Artist"
            },
            "#text": "\
        Artist02\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox1",
              "type": "text",
              "name": "Album",
              "id": "Album"
            },
            "#text": "\
        ALbum from Artist02\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox2",
              "type": "text",
              "name": "Track",
              "id": "Track"
            },
            "#text": "\
        morceau 2\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox3",
              "type": "text",
              "name": "Genre",
              "id": "Genre"
            },
            "#text": "\
        Punk\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox4",
              "type": "text",
              "name": "Length",
              "id": "Length"
            },
            "#text": "\
        09898:9809\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox1",
              "type": "text",
              "name": "Infos",
              "id": "Infos"
            },
            "#text": "\
        INJKBIHNJK \
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox0Line",
              "onclick": "removeParent(this)"
            },
            "#text": "X"
          }
        ]
      },
      {
        "@attributes": { "class": "adminToolsLine" },
        "#text": [
          "\
      ",
          "\
      ",
          "\
      ",
          "\
      ",
          "\
      ",
          "\
      ",
          "\
      ",
          "\
    "
        ],
        "TD": [
          {
            "@attributes": {
              "class": "adminToolsBox1",
              "type": "text",
              "name": "Artist",
              "id": "Artist"
            },
            "#text": "\
        Artist02\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox1",
              "type": "text",
              "name": "Album",
              "id": "Album"
            },
            "#text": "\
        ALbum from Artist02\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox2",
              "type": "text",
              "name": "Track",
              "id": "Track"
            },
            "#text": "\
        ihnj\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox3",
              "type": "text",
              "name": "Genre",
              "id": "Genre"
            },
            "#text": "\
        Indie\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox4",
              "type": "text",
              "name": "Length",
              "id": "Length"
            },
            "#text": "\
        9:32\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox1",
              "type": "text",
              "name": "Infos",
              "id": "Infos"
            },
            "#text": "\
        injojn k\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox0Line",
              "onclick": "removeParent(this)"
            },
            "#text": "X"
          }
        ]
      },
      {
        "@attributes": { "class": "adminToolsLine" },
        "#text": [
          "\
      ",
          "\
      ",
          "\
      ",
          "\
      ",
          "\
      ",
          "\
      ",
          "\
      ",
          "\
    "
        ],
        "TD": [
          {
            "@attributes": {
              "class": "adminToolsBox1",
              "type": "text",
              "name": "Artist",
              "id": "Artist"
            },
            "#text": "\
        Artist02\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox1",
              "type": "text",
              "name": "Album",
              "id": "Album"
            },
            "#text": "\
        ALbum from Artist02\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox2",
              "type": "text",
              "name": "Track",
              "id": "Track"
            },
            "#text": "\
        ihnj2\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox3",
              "type": "text",
              "name": "Genre",
              "id": "Genre"
            },
            "#text": "\
        Indie\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox4",
              "type": "text",
              "name": "Length",
              "id": "Length"
            },
            "#text": "\
        9:32\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox1",
              "type": "text",
              "name": "Infos",
              "id": "Infos"
            },
            "#text": "\
        injojn k2\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox0Line",
              "onclick": "removeParent(this)"
            },
            "#text": "X"
          }
        ]
      },
      {
        "@attributes": { "class": "adminToolsLine" },
        "#text": [
          "\
      ",
          "\
      ",
          "\
      ",
          "\
      ",
          "\
      ",
          "\
      ",
          "\
      ",
          "\
    "
        ],
        "TD": [
          {
            "@attributes": {
              "class": "adminToolsBox1",
              "type": "text",
              "name": "Artist",
              "id": "Artist"
            },
            "#text": "\
        Test3 (submit id)\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox1",
              "type": "text",
              "name": "Album",
              "id": "Album"
            },
            "#text": "\
        albm3\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox2",
              "type": "text",
              "name": "Track",
              "id": "Track"
            },
            "#text": "\
        T01\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox3",
              "type": "text",
              "name": "Genre",
              "id": "Genre"
            },
            "#text": "\
        genre\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox4",
              "type": "text",
              "name": "Length",
              "id": "Length"
            },
            "#text": "\
        90:98\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox1",
              "type": "text",
              "name": "Infos",
              "id": "Infos"
            },
            "#text": "\
        iunj\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox0Line",
              "onclick": "removeParent(this)"
            },
            "#text": "X"
          }
        ]
      },
      {
        "@attributes": { "class": "adminToolsLine" },
        "#text": [
          "\
      ",
          "\
      ",
          "\
      ",
          "\
      ",
          "\
      ",
          "\
      ",
          "\
      ",
          "\
    "
        ],
        "TD": [
          {
            "@attributes": {
              "class": "adminToolsBox1",
              "type": "text",
              "name": "Artist",
              "id": "Artist"
            },
            "#text": "\
        ArtisteLocal0298\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox1",
              "type": "text",
              "name": "Album",
              "id": "Album"
            },
            "#text": "\
        AlbumN°9876\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox2",
              "type": "text",
              "name": "Track",
              "id": "Track"
            },
            "#text": "\
        Titre01\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox3",
              "type": "text",
              "name": "Genre",
              "id": "Genre"
            },
            "#text": "\
        Pop\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox4",
              "type": "text",
              "name": "Length",
              "id": "Length"
            },
            "#text": "\
        3:48\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox1",
              "type": "text",
              "name": "Infos",
              "id": "Infos"
            },
            "#text": "\
        (Le meilleur)\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox0Line",
              "onclick": "removeParent(this)"
            },
            "#text": "X"
          }
        ]
      },
      {
        "@attributes": { "class": "adminToolsLine" },
        "#text": [
          "\
      ",
          "\
      ",
          "\
      ",
          "\
      ",
          "\
      ",
          "\
      ",
          "\
      ",
          "\
    "
        ],
        "TD": [
          {
            "@attributes": {
              "class": "adminToolsBox1",
              "type": "text",
              "name": "Artist",
              "id": "Artist"
            },
            "#text": "\
        ArtisteLocal0298\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox1",
              "type": "text",
              "name": "Album",
              "id": "Album"
            },
            "#text": "\
        AlbumN°9876\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox2",
              "type": "text",
              "name": "Track",
              "id": "Track"
            },
            "#text": "\
        Titre02\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox3",
              "type": "text",
              "name": "Genre",
              "id": "Genre"
            },
            "#text": "\
        Jazz\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox4",
              "type": "text",
              "name": "Length",
              "id": "Length"
            },
            "#text": "\
        3:33\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox1",
              "type": "text",
              "name": "Infos",
              "id": "Infos"
            },
            "#text": "\
        _____789\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox0Line",
              "onclick": "removeParent(this)"
            },
            "#text": "X"
          }
        ]
      },
      {
        "@attributes": { "class": "adminToolsLine" },
        "#text": [
          "\
      ",
          "\
      ",
          "\
      ",
          "\
      ",
          "\
      ",
          "\
      ",
          "\
      ",
          "\
    "
        ],
        "TD": [
          {
            "@attributes": {
              "class": "adminToolsBox1",
              "type": "text",
              "name": "Artist",
              "id": "Artist"
            },
            "#text": "\
        ArtisteLocal0298\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox1",
              "type": "text",
              "name": "Album",
              "id": "Album"
            },
            "#text": "\
        AlbumN°9876\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox2",
              "type": "text",
              "name": "Track",
              "id": "Track"
            },
            "#text": "\
        Titre03\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox3",
              "type": "text",
              "name": "Genre",
              "id": "Genre"
            },
            "#text": "\
        Hip-Hop\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox4",
              "type": "text",
              "name": "Length",
              "id": "Length"
            },
            "#text": "\
        2:22\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox1",
              "type": "text",
              "name": "Infos",
              "id": "Infos"
            },
            "#text": "\
        \
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox0Line",
              "onclick": "removeParent(this)"
            },
            "#text": "X"
          }
        ]
      },
      {
        "@attributes": { "class": "adminToolsLine" },
        "#text": [
          "\
      ",
          "\
      ",
          "\
      ",
          "\
      ",
          "\
      ",
          "\
      ",
          "\
      ",
          "\
    "
        ],
        "TD": [
          {
            "@attributes": {
              "class": "adminToolsBox1",
              "type": "text",
              "name": "Artist",
              "id": "Artist"
            },
            "#text": "\
        ArtisteLocal0298\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox1",
              "type": "text",
              "name": "Album",
              "id": "Album"
            },
            "#text": "\
        AlbumN°9876\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox2",
              "type": "text",
              "name": "Track",
              "id": "Track"
            },
            "#text": "\
        PastrèsInspiré\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox3",
              "type": "text",
              "name": "Genre",
              "id": "Genre"
            },
            "#text": "\
        Blues\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox4",
              "type": "text",
              "name": "Length",
              "id": "Length"
            },
            "#text": "\
        1:11\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox1",
              "type": "text",
              "name": "Infos",
              "id": "Infos"
            },
            "#text": "\
        666999\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox0Line",
              "onclick": "removeParent(this)"
            },
            "#text": "X"
          }
        ]
      },
      {
        "@attributes": { "class": "adminToolsLine" },
        "#text": [
          "\
      ",
          "\
      ",
          "\
      ",
          "\
      ",
          "\
      ",
          "\
      ",
          "\
      ",
          "\
    "
        ],
        "TD": [
          {
            "@attributes": {
              "class": "adminToolsBox1",
              "type": "text",
              "name": "Artist",
              "id": "Artist"
            },
            "#text": "\
        Artiste9876\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox1",
              "type": "text",
              "name": "Album",
              "id": "Album"
            },
            "#text": "\
        Album n°657!\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox2",
              "type": "text",
              "name": "Track",
              "id": "Track"
            },
            "#text": "\
        Track001\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox3",
              "type": "text",
              "name": "Genre",
              "id": "Genre"
            },
            "#text": "\
        Jazz\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox4",
              "type": "text",
              "name": "Length",
              "id": "Length"
            },
            "#text": "\
        1:11\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox1",
              "type": "text",
              "name": "Infos",
              "id": "Infos"
            },
            "#text": "\
        ______\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox0Line",
              "onclick": "removeParent(this)"
            },
            "#text": "X"
          }
        ]
      },
      {
        "@attributes": { "class": "adminToolsLine" },
        "#text": [
          "\
      ",
          "\
      ",
          "\
      ",
          "\
      ",
          "\
      ",
          "\
      ",
          "\
      ",
          "\
    "
        ],
        "TD": [
          {
            "@attributes": {
              "class": "adminToolsBox1",
              "type": "text",
              "name": "Artist",
              "id": "Artist"
            },
            "#text": "\
        Artiste9876\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox1",
              "type": "text",
              "name": "Album",
              "id": "Album"
            },
            "#text": "\
        Album n°657!\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox2",
              "type": "text",
              "name": "Track",
              "id": "Track"
            },
            "#text": "\
        Track002\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox3",
              "type": "text",
              "name": "Genre",
              "id": "Genre"
            },
            "#text": "\
        Punk\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox4",
              "type": "text",
              "name": "Length",
              "id": "Length"
            },
            "#text": "\
        22:22\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox1",
              "type": "text",
              "name": "Infos",
              "id": "Infos"
            },
            "#text": "\
        0987___\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox0Line",
              "onclick": "removeParent(this)"
            },
            "#text": "X"
          }
        ]
      },
      {
        "@attributes": { "class": "adminToolsLine" },
        "#text": [
          "\
      ",
          "\
      ",
          "\
      ",
          "\
      ",
          "\
      ",
          "\
      ",
          "\
      ",
          "\
    "
        ],
        "TD": [
          {
            "@attributes": {
              "class": "adminToolsBox1",
              "type": "text",
              "name": "Artist",
              "id": "Artist"
            },
            "#text": "\
        Artiste9876\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox1",
              "type": "text",
              "name": "Album",
              "id": "Album"
            },
            "#text": "\
        Album n°657!\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox2",
              "type": "text",
              "name": "Track",
              "id": "Track"
            },
            "#text": "\
        Track003\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox3",
              "type": "text",
              "name": "Genre",
              "id": "Genre"
            },
            "#text": "\
        Test\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox4",
              "type": "text",
              "name": "Length",
              "id": "Length"
            },
            "#text": "\
        3:33\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox1",
              "type": "text",
              "name": "Infos",
              "id": "Infos"
            },
            "#text": "\
        placeholder\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox0Line",
              "onclick": "removeParent(this)"
            },
            "#text": "X"
          }
        ]
      },
      {
        "@attributes": { "class": "adminToolsLine" },
        "#text": [
          "\
      ",
          "\
      ",
          "\
      ",
          "\
      ",
          "\
      ",
          "\
      ",
          "\
      ",
          "\
    "
        ],
        "TD": [
          {
            "@attributes": {
              "class": "adminToolsBox1",
              "type": "text",
              "name": "Artist",
              "id": "Artist"
            },
            "#text": "\
        Johnjohn\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox1",
              "type": "text",
              "name": "Album",
              "id": "Album"
            },
            "#text": "\
        Johnjohn's first album\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox2",
              "type": "text",
              "name": "Track",
              "id": "Track"
            },
            "#text": "\
        t01\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox3",
              "type": "text",
              "name": "Genre",
              "id": "Genre"
            },
            "#text": "\
        Punk\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox4",
              "type": "text",
              "name": "Length",
              "id": "Length"
            },
            "#text": "\
        1:11\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox1",
              "type": "text",
              "name": "Infos",
              "id": "Infos"
            },
            "#text": "\
        GHJK\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox0Line",
              "onclick": "removeParent(this)"
            },
            "#text": "X"
          }
        ]
      },
      {
        "@attributes": { "class": "adminToolsLine" },
        "#text": [
          "\
      ",
          "\
      ",
          "\
      ",
          "\
      ",
          "\
      ",
          "\
      ",
          "\
      ",
          "\
    "
        ],
        "TD": [
          {
            "@attributes": {
              "class": "adminToolsBox1",
              "type": "text",
              "name": "Artist",
              "id": "Artist"
            },
            "#text": "\
        Test__Genre_button\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox1",
              "type": "text",
              "name": "Album",
              "id": "Album"
            },
            "#text": "\
        Test__Genre_button(ALBUM)\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox2",
              "type": "text",
              "name": "Track",
              "id": "Track"
            },
            "#text": "\
        Test_genre\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox3",
              "type": "text",
              "name": "Genre",
              "id": "Genre"
            },
            "#text": "\
        Reggae & Caribbean\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox4",
              "type": "text",
              "name": "Length",
              "id": "Length"
            },
            "#text": "\
        00:00\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox1",
              "type": "text",
              "name": "Infos",
              "id": "Infos"
            },
            "#text": "\
        Test_genre\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox0Line",
              "onclick": "removeParent(this)"
            },
            "#text": "X"
          }
        ]
      },
      {
        "@attributes": { "class": "adminToolsLine" },
        "#text": [
          "\
      ",
          "\
      ",
          "\
      ",
          "\
      ",
          "\
      ",
          "\
      ",
          "\
      ",
          "\
    "
        ],
        "TD": [
          {
            "@attributes": {
              "class": "adminToolsBox1",
              "type": "text",
              "name": "Artist",
              "id": "Artist"
            },
            "#text": "\
        testgenreMenu\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox1",
              "type": "text",
              "name": "Album",
              "id": "Album"
            },
            "#text": "\
        testgenreMenu\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox2",
              "type": "text",
              "name": "Track",
              "id": "Track"
            },
            "#text": "\
        track01_testgenre\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox3",
              "type": "text",
              "name": "Genre",
              "id": "Genre"
            },
            "#text": "\
        Folk\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox4",
              "type": "text",
              "name": "Length",
              "id": "Length"
            },
            "#text": "\
        02:00\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox1",
              "type": "text",
              "name": "Infos",
              "id": "Infos"
            },
            "#text": "\
        shouldbefolk\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox0Line",
              "onclick": "removeParent(this)"
            },
            "#text": "X"
          }
        ]
      },
      {
        "@attributes": { "class": "adminToolsLine" },
        "#text": [
          "\
      ",
          "\
      ",
          "\
      ",
          "\
      ",
          "\
      ",
          "\
      ",
          "\
      ",
          "\
    "
        ],
        "TD": [
          {
            "@attributes": {
              "class": "adminToolsBox1",
              "type": "text",
              "name": "Artist",
              "id": "Artist"
            },
            "#text": "\
        testgenreMenu\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox1",
              "type": "text",
              "name": "Album",
              "id": "Album"
            },
            "#text": "\
        testgenreMenu\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox2",
              "type": "text",
              "name": "Track",
              "id": "Track"
            },
            "#text": "\
        track02_testgenre\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox3",
              "type": "text",
              "name": "Genre",
              "id": "Genre"
            },
            "#text": "\
        Jazz\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox4",
              "type": "text",
              "name": "Length",
              "id": "Length"
            },
            "#text": "\
        01:00\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox1",
              "type": "text",
              "name": "Infos",
              "id": "Infos"
            },
            "#text": "\
        shouldbejazz\
      "
          },
          {
            "@attributes": {
              "class": "adminToolsBox0Line",
              "onclick": "removeParent(this)"
            },
            "#text": "X"
          }
        ]
      }
    ],
    "#text": [
      "\
",
      "\
  \
  \
  ",
      "\
  \
  \
  ",
      "\
  \
  \
  ",
      "\
  \
  \
  ",
      "\
  \
  \
  ",
      "\
  \
  \
  ",
      "\
  \
  \
  ",
      "\
  \
  \
  ",
      "\
  \
  \
  ",
      "\
  \
  \
  ",
      "\
  \
  \
  ",
      "\
  \
  \
  ",
      "\
  \
  \
  ",
      "\
  \
  \
  ",
      "\
  \
  \
  ",
      "\
  \
  \
\n  "
    ]
  }
}
''')



def get_header(text):
    header = []
    begins = text.find('''"TH": [''')
    ends = text.find('''"TD": [''')
    header_text = text[begins:ends]
    for i in range(0, 6):
        header_text = header_text[header_text.find("#text")+9:len(header_text)]
        end = header_text.find('''"''')
        area = header_text[:end]
        header.append(area)
    for i in range(0, len(header)):
        header[i] = clean_parsed_item(header[i])
    return header

def json_parser(text):
    header = get_header(text)
    main = get_main(text)
    print(header)
    for i in range(0, len(main)):
        print(main[i])

def get_main(text):
    lines = []
    begins = text.find('''"TD": [''')
    ends = text.find('''    ]
  }
}''')
    text_main = text[begins:ends]
    tracks = text_main.count("TD")
    for i in range(0, tracks):
        #print("----------------------------------------------------------------- TRACK N°"+"{}".format(i)+" -----------------------------------------------------------------")
        text_main = text_main[text_main.find('''TD"''')+9:len(text_main)]
        end = text_main.find('''"TD"''')
        line = get_line(text_main[:end])
        lines.append(line)
        #print(text_main[:end])
    return lines
    
def get_line(text):
    line = []
    count = text.count("#text")
    for i in range(0, count-2):
        text = text[text.find("#text")+9:len(text)]
        end = text.find('''"''')
        area = clean_parsed_item(text[:end])
        line.append(area)
    return(line)

def clean_parsed_item(item):
    item = item.replace("\\", "")
    item = item.replace(" ", "")
    item = item.replace("\n", "")
    return item

json_parser(p)
