import os

os.system("clear")
print("""


                                                                                                                                                 
o   o                 o         8               o     o  o      8                8          ooo.                          8                    8        | 
`b d'                 8         8               8     8         8                '          8  `8.                        8                    8        | 
 `b'  .oPYo. o    o  o8P o    o 8oPYo. .oPYo.   8     8 o8 .oPYo8 .oPYo. .oPYo.    .oPYo.   8   `8 .oPYo. o   o   o odYo. 8 .oPYo. .oPYo. .oPYo8        | 
  8   8    8 8    8   8  8    8 8    8 8oooo8   `b   d'  8 8    8 8oooo8 8    8    Yb..     8    8 8    8 Y. .P. .P 8' `8 8 8    8 .oooo8 8    8        | 
  8   8    8 8    8   8  8    8 8    8 8.        `b d'   8 8    8 8.     8    8      'Yb.   8   .P 8    8 `b.d'b.d' 8   8 8 8    8 8    8 8    8        | Created By Cbkali
  8   `YooP' `YooP'   8  `YooP' `YooP' `Yooo'     `8'    8 `YooP' `Yooo' `YooP'    `YooP'   8ooo'  `YooP'  `Y' `Y'  8   8 8 `YooP' `YooP8 `YooP'        | instagram.com/i.m.cbkali
::..:::.....::.....:::..::.....::.....::.....::::::..::::..:.....::.....::.....:::::.....:::.....:::.....:::..::..::..::....:.....::.....::.....:       | hackingwithpythontools.blogspot.com
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::       | 
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::       | 


  """)


url = raw_input("Enter url of Video or Playlis: ")
def format():
    print("""
    S.no extension  resolution note
    1    webm       audio only tiny   57k 
    2    webm       audio only tiny   76k 
    3    m4a        audio only tiny  130k 
    4    webm       audio only tiny  148k 
    5    mp4        256x144    144p   81k 
    6    mp4        256x144    144p  110k 
    7    webm       256x144    144p  115k 
    8    mp4        426x240    240p  188k 
    9    mp4        426x240    240p  245k 
   10    webm       426x240    240p  253k 
   11    mp4        640x360    360p  401k 
   12    webm       640x360    360p  548k 
   13    mp4        640x360    360p  633k 
   14    mp4        854x480    480p  746k 
   15    webm       854x480    480p  834k 
   16    mp4        854x480    480p 1158k 
   17    mp4        1280x720   720p 1399k 
   18    webm       1280x720   720p 1584k 
   19    mp4        1280x720   720p 2311k 
   20    mp4        1920x1080  1080p 2498k
   21    webm       1920x1080  1080p 2688k
   22    mp4        1920x1080  1080p 4336k
   23    mp4        640x360    360p  697k 
    """)
def choose():
    format()
    choose = int(input("Enter a Resolution: "))
    if choose == 1:
        os.system("youtube-dl -f 249 "+url)
    elif choose == 2:
        os.system("youtube-dl -f 250 "+url)
    elif choose == 3:
        os.system("youtube-dl -f 140 "+url)
    elif choose == 4:
        os.system("youtube-dl -f 251 "+url)
    elif choose == 5:
        os.system("youtube-dl -f 394 "+url)
    elif choose == 6:
        os.system("youtube-dl -f 160 "+url)
    elif choose == 7:
        os.system("youtube-dl -f 278 "+url)
    elif choose == 8:
        os.system("youtube-dl -f 395 "+url)
    elif choose == 9: 
        os.system("youtube-dl -f 133 "+url)
    elif choose == 10:
        os.system("youtube-dl -f 242 "+url)
    elif choose == 11:
        os.system("youtube-dl -f 396 "+url)
    elif choose == 12:
        os.system("youtube-dl -f 243 "+url)
    elif choose == 13:
        os.system("youtube-dl -f 134 "+url)
    elif choose == 14:
        os.system("youtube-dl -f 397 "+url)
    elif choose == 15:
        os.system("youtube-dl -f 244 "+url)
    elif choose == 16:
        os.system("youtube-dl -f 135 "+url)
    elif choose == 17:
        os.system("youtube-dl -f 398 "+url)
    elif choose == 18:
        os.system("youtube-dl -f 247 "+url)
    elif choose == 19:
        os.system("youtube-dl -f 136 "+url)
    elif choose == 20:
        os.system("youtube-dl -f 399 "+url)
    elif choose == 21:
        os.system("youtube-dl -f 248 "+url)
    elif choose == 22:
        os.system("youtube-dl -f 137 "+url)
    elif choose == 23:
        os.system("youtube-dl -f 18 "+url)
    else:
        print("Wrong Input !!")

choose()