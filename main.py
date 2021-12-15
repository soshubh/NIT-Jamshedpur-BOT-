import keep_alive
import time
import string
import math
import random
import re
import json
import googletrans
import urllib
import requests
import datetime


TOKEN="#####################################3"
URL = f"https://api.telegram.org/bot{TOKEN}/"
translator = googletrans.Translator()

PatternType = type(re.compile(""))

debug_password = "".join(random.choice(string.ascii_lowercase) for i in range(4))


def get_url(url):
    response = requests.get(url)
    return response.content.decode("utf8")


def get_updates(offset=None):
    url = URL + "getUpdates?timeout=100"
    if offset:
        url += f"&offset={offset}"
    return json.loads(get_url(url))


def get_last_update_id(updates):
    return max(int(update["update_id"])
               for update in updates["result"])


def echo(update):
    text = update["message"].get("text", "(No text sent)")
    chat = update["message"]["chat"]["id"]
    send_message(chat, text)


def respond(update):
    if "message" not in update or "text" not in update["message"]:
        return

    text = update["message"]["text"].strip()

    if text.endswith("@nitjamshedpurbot"):
        text = text[:-len("@nitjamshedpurbot")]

    if text.startswith("/"):
        text_parts = text[1:].split(" ", 1)
        command = text_parts[0]
        param = text_parts[1] if len(text_parts) == 2 else ""
        respond_command(update["message"], command.lower(), param)
    else:
        respond_message(update["message"])


START_MESSAGE = """Hello, Thank for contacting NIT Jamshedpur Batch 2021.
For other Help you can Type \"/help\"."""

HELP_MESSAGE = """
ɪ ᴄᴀɴ ʜᴇʟᴘ ʏᴏᴜ ʀᴇɢᴀʀᴅɪɴɢ ɴɪᴛ ᴊᴀᴍsʜᴇᴅᴘᴜʀ

/about ：ʀᴇᴀᴅ ᴀʙᴏᴜᴛ ɴɪᴛ ᴊsʀ

/nirf ：ʀᴀɴᴋ ᴏғ ɴɪᴛ ᴊsʀ

/fest ：ᴀʟʟ ғᴀsᴛɪᴠᴀʟ ɪɴ ɴɪᴛ ᴊsʀ

/head ：ᴀʙᴏᴜᴛ ᴅɪʀᴇᴄᴛᴏʀ ᴏғ ɴɪᴛ ᴊsʀ

/boyshostel ：ᴋɴᴏᴡ ᴀʙᴏᴜᴛ ʙᴏʏs ʜᴏsᴛᴇʟ ᴀɴᴅ ғᴇᴇ

/girlshostel ：ᴀʟʟ ᴀʙᴏᴜᴛ ɢɪʀʟs ʜᴏsᴛᴇʟ

/mess ：ᴍᴇɴᴜ ᴀɴᴅ ғᴇᴇ

/foodstall ：ᴀʟʟ ғᴏᴏᴅ sʜᴏᴘ ɪɴ ᴄᴀᴍᴘᴜs

/ground ：ᴋɴᴏᴡ ᴀʙᴏᴜᴛ ᴘʟᴀʏɢʀᴏᴜɴᴅ ᴀɴᴅ ᴄᴏᴜʀᴛ

/gym ：sᴀᴅ ᴛʜᴇʀᴇ ɪs ɴᴏ ɢʏᴍ ʙᴜᴛ......

/medical ：ᴋɴᴏᴡ ᴀʙᴏᴜᴛ ᴍᴇᴅɪᴄᴀʟ ғᴀᴄɪʟɪᴛɪᴇs ᴀɴᴅ ʀᴇʟᴀxᴀᴛɪᴏɴ

/clubs ：ᴛʜᴇʀᴇ ɪs 30+ ᴄʟᴜʙs ᴀɴᴅ ᴛᴇᴀᴍs

/placement ：ᴀʟʟ ᴀʙᴏᴜᴛ 𝟸𝟶𝟸𝟷 ᴘʟᴀᴄᴇᴍᴇɴᴛ

/loverspoint ：ʏᴇᴀʜ ɴɪᴛ ᴊᴀᴍsʜᴇᴅᴘᴜʀ ᴄᴀɴ ɢɪᴠᴇ ʏᴏᴜ ᴘʟᴀᴄᴇᴍᴇɴᴛ + ʟɪғᴇ ᴘᴀʀᴛɴᴇʀ (source through senior)

/meme ：ᴋɴᴏᴡ ᴀʙᴏᴜᴛ ғᴜɴ ᴇɴᴠɪʀᴏɴᴍᴇɴᴛ

/contact ：ᴄᴏɴᴛᴀᴄᴛ ᴡɪᴛʜ ɴɪᴛ ᴊᴀᴍsʜᴇᴅᴘᴜʀ sᴛᴜᴅᴇɴᴛs

/contactdev ：ᴄᴏɴᴛᴀᴄᴛ ᴡɪᴛʜ ʙᴏᴛ ᴅᴇᴠᴇʟᴏᴘᴇʀ
"""
HEAD="""
ᴅɪʀᴇᴄᴛᴏʀ : ᴘʀᴏғ. ᴋᴀʀᴜɴᴇsʜ ᴋᴜᴍᴀʀ sʜᴜᴋʟᴀ

ɴᴏ : 𝟼𝟻𝟽𝟸𝟹𝟽𝟹𝟹𝟿𝟸

ᴇ-ᴍᴀɪʟ : director@nitjsr.ac.in
http://www.nitjsr.ac.in/institute/governance/uploads/kksukla_director.jpg
"""

EMOJI = "😀😃😄😁😆😅😂🤣🤨🤩😣😟😱😰😥"

birth = datetime.date(day=8, month=9, year=2021)

ABOUT_NIT="""National Institute of Technology Jamshedpur (NIT Jamshedpur or NITJSR), is an Institute of National Importance located at Jamshedpur, Jharkhand, India. Established as a Regional Institute of Technology on 15 August 1960, it was upgraded to National Institute of Technology (NIT) on 27 December 2002 with the status of a Deemed University. It is one of the 31 NITs in India, and as such is directly under the control of the Ministry of Human Resource Development (MHRD)."""

NIRF_RANK="""NIT Jamshedpur was ranked 79 among engineering colleges in India by the National Institutional Ranking Framework (NIRF) in 2020"""

FESTIVAL= """
✑ᴏᴊᴀss           /ojass

✑ᴄᴜʟғᴇsᴛ       /culfest

✑ᴛᴇᴄʜɴɪᴄᴀ     /technica

✑ᴠɪᴅʜᴀᴀɴ       /vidhaan

✑ᴄᴘᴄᴇ             /cpce
"""

ojass="""Ojass A techno-management festival of the college to showcase the technical and managerial skill of the students"""
culfest="""Culfest is an annual cultural event at a college or university organised by the student community, involving participants from other colleges as well.Professional performing artists are also typically invited, and a number of competitions are held for students"""
technica="""Technica is an annual festival for students of Metallurgical and Materials engineering from all over India"""
vidhaan="""Vidhaan a civil branch festival managed by Civil Engineering Society of NIT Jamshedpur"""
cpce="""NIT Jamshedpur Conference Catalysis and Photocatalysis for Clean Energy"""
CONTACT="""https://t.me/joinchat/CA4Wg4gRO9JlMjhl"""
CONTACT_DEV="""You can contact with developer at
@so_shubh_bot
@so_shubh

https://instagram.com/so_shubh?utm_medium=copy_link"""

BOY_HOSTEL="""
                Total 9 Boy's Hostel

Hostel- E, F, G, H, I, J, K, RLB Residence and Ambedkar Hall of residence

Room Rent : ₹6000-7000
Electricity and Water charge : ₹2,000

Total : ₹8000-9000/sem
"""
GIRL_HOSTEL="""
                 Total 4 Girl's Hostel

Hostel - A,B,C,D

Room Rent : ₹7000
Electricity and Water charge : ₹2000

TOTAL : ₹9000/Sem *Not Confirmed
"""
MESS= """
Mess fee : 16000/sem


Mess Menu for Boy's Hostel
https://media.discordapp.net/attachments/878183252379193345/885804170962149416/IMG_20210910_135827.jpg


Mess Menu For Girls Hostel
https://media.discordapp.net/attachments/878183252379193345/885805654432940052/-6185839735285591516_121.jpg
"""
LOVE="""
Hmm, personally I don't wanna talk about that, but it's obvious if you're roaming around nit Jamshedpur you can see lots of love birds or maybe you're the one of them!
"""
PLACEMENT="""
❖ Here we gonna see what the placement in NIT JSR of MCA students. I know you guys already know more than me about placement and all, but let's be honest in nit jsr mca student's average placement is 𝟰-𝟱𝗟𝗣𝗔 and highest package is 𝟳.𝟱𝗟𝗣𝗔 and its not my latent thoughts. You can check this on the NIT JSR placement cell!

https://media.discordapp.net/attachments/878183252379193345/885851427585556490/IMG_20210910_170700.jpg
"""

CLUB="""
Benefits of Joining Clubs in College are so wide and far-reaching that it will serve as a foundation for shaping your future career. By joining the Student Club in college you can acquire some essential skills and qualifications that will take you a few steps ahead as a job candidate. We often might not try to understand the needs of the college club properly!

☞ PROGRAMMING CLUB

☞ ACM NITJSR STUDENT CHAPTER

☞ WEB TEAM

☞ COMPUTER SOCIETY OF INDIA STUDENTS' BRANCH - NITJSR

☞ PHOTOGRAPHY CUM FILMAKING CLUB(PHOCUS)

☞ INNOVATION CLUB

☞ LITERARY & DEBATING SOCIETY

☞ MECHANICAL ENGINEERING SOCIETY (MES)

☞ THE INDOMITABLE

☞ SOFT SKILLS CLUB

☞ SOCIETY OF COMPUTER APPLICATIONS

☞ TEAM ECO RIDERS

☞ CULTURAL AND DRAMATICS SOCIETY

☞ FINE ARTS CLUB

☞ SOCIETY OF ELECTRONICS AND COMMUNICATION ENGINEERING (SECE)

☞ RACHNA

☞ VALUES AND ETHICS CLUB

☞ NATIONAL SERVICE SCHEME(NSS)

☞ CIVIL ENGINEERING SOCIETY

☞ EARN N LEARN

☞ QuNITe

☞ SPORTS

☞ proAt_NITJsr - The CodeChef Chapter

☞ TEAM PHOENIX

☞ DRIFT RACING TEAM

☞ INNOREVA

☞ ENTREPRENEURSHIP CELL

☞ TEAM RAYS

☞ TEAM TOP GUNS(TOPGUNS)

☞ TEAM REVANTA

☞ TEAM DAKSH

☞ ELECTTRICAL ENGINEERING SOCIETY
"""


MEDICAL="""
✆ Medical Center and Ambulance available in campus

✆ Relaxation for NIT Jamshedpur students in Tata Main Hospital, Jamshedpur
"""


GROUND= """
❑ Three Playground
[one Cricket︰one Hokey︰one Footbal]

❑ Three Basketball Court

❑ Two Long Tennis Court

❑ One Badminton Court

❑ One Volleyball Court

❑ One Table Tennis
"""


GYM="""
There is a gym in the campus also some equipment available in hostel!
"""



FOOD_STALL="""
◖Amul Cafe
◖Papu Da
◖Sudha Dairy
◖NIT Canteen
◖Night Canteen and more..
"""

MEME="""
㋡ NIT Jamshedpur Supreme Court
https://instagram.com/nit.jsr.supreme.court?utm_medium=copy_link

㋡ NIT Jamshedpur Frustration
https://instagram.com/nit_jsr_frustration?utm_medium=copy_link
"""

def chuck_joke():
    data = json.loads(get_url("http://api.icndb.com/jokes/random1http://api.icndb.com/jokes/random"))
    if data["type"] == "success":
        return data["value"]["joke"].replace("&quot;", "\"")
    else:
        return "something went wrong"


def fact():
    return json.loads(get_url("http://randomuselessfact.appspot.com/random.json?language=en"))["text"]


def lower_fact():
    s = fact()
    s = s[0].lower() + s[1:]
    return s


def word_value(word):
    return sum(ord(c) for c in word)


def respond_command(msg, command, param):
    chat_id = msg["chat"]["id"]

    if command == "start":
        send_message(chat_id,START_MESSAGE)  
    elif command == "fest":
        send_message(chat_id,FESTIVAL)
        
    elif command == "ojass":
        send_message(chat_id,ojass)
    elif command == "culfest":
        send_message(chat_id,culfest)
    elif command == "technica":
        send_message(chat_id, technica)
    elif command == "vidhaan":
        send_message(chat_id, vidhaan)
    elif command == "cpce":
        send_message(chat_id, cpce)
        
    elif command == "nirf":
        send_message(chat_id,NIRF_RANK)
    elif command == "about":send_message(chat_id,ABOUT_NIT)
    elif command == "head":send_message(chat_id,HEAD)
    elif command == "help":
        send_message(chat_id, HELP_MESSAGE)
        
        
        
    elif command == "boyshostel":
        send_message(chat_id, BOY_HOSTEL)
    elif command == "girlshostel":
        send_message(chat_id, GIRL_HOSTEL)
    elif command == "mess":
        send_message(chat_id, MESS)
    elif command == "foodstall":
        send_message(chat_id, FOOD_STALL)
    elif command == "ground":
        send_message(chat_id, GROUND)
    elif command == "gym":
        send_message(chat_id, GYM)
    elif command == "medical":
        send_message(chat_id, MEDICAL)
    elif command == "clubs":
        send_message(chat_id, CLUB)
    elif command == "placement":
        send_message(chat_id, PLACEMENT)
    elif command == "loverspoint":
        send_message(chat_id,LOVE)
        
        
    elif command =="meme":send_message(chat_id,MEME)
        
    elif command == "contact":send_message(chat_id,CONTACT)
    elif command == "contactdev":send_message(chat_id, CONTACT_DEV)
    elif command == "stop":
        if param.lower() == debug_password:
            send_message(chat_id, "Bye!")
            exit()
        else:
            send_message(chat_id, "Nice try!")
    elif command == "echo":
        send_message(chat_id, param)
    elif command in ("calculate", "calc", "eval", "python"):
        try:
            evaled = eval(param, {"__builtins__": {}}, SAFE_FUNCTIONS)
        except Exception as e:
            send_message(chat_id, str(e))
        else:
            send_message(chat_id, repr(evaled))
    elif command == "bot":
        respond_message(msg)
    elif command == "joke":
        send_message(chat_id, chuck_joke())
    else: send_message(chat_id, f"I'm sorry, This command is not valid \"{command}\".")

SAFE_FUNCTIONS = {
    "abs": abs, "round": round, "pos": pow, "divmod": divmod,
        "int": int, "float": float, "complex": complex, "bool": bool, "slice": slice,
            "str": str, "repr": repr, "ascii": ascii, "format": format, "bytes": bytes, "bytearray": bytearray,
                "list": list, "dict": dict, "set": set, "frozenset": frozenset, "tuple": tuple, "range": range,
                    "map": map, "filter": filter, "sorted": sorted, "iter": iter,
                        "next": next, "reversed": reversed, "enumerate": enumerate,
                            "sum": sum, "min": min, "max": max, "all": all, "any": any, "len": len,
                                "ord": ord, "chr": chr, "bin": bin, "oct": oct, "hex": hex,
                                    "globals": globals, "locals": locals, "vars": vars,
                                        "sin": math.sin, "cos": math.cos, "tan": math.tan,
                                            "asin": math.asin, "acos": math.acos, "atan": math.atan,
                                                "pi": math.pi, "e": math.e, "tau": math.tau, "degrees": math.degrees, "radians": math.radians
                                                }

GOOD_CHARS = string.ascii_letters + string.digits + " "


def collatz(n):
    if n % 2 == 0:
        return n // 2
    else:
        return n*3 + 1


def wikipedia_definition(s):
  s = s.replace(" ", "_")
  site_text = requests.get("https://en.wikipedia.org/w/api.php?action=opensearch&limit=1&search=" + s).text
  json_list = json.loads(site_text)
  if json_list[3] == []:
    return None
  else:
    return json_list[3][0]


def if_none(x, when_none):
  if x is None:
    return when_none
  else:
    return x


places = ["Atlantis", "Canada", "China", "Croatia", "Czechoslovakia", "Egypt", "Ethiopia", "Finland", "France",
          "Hawaii", "Hogwarts", "Germany", "Italy", "Narnia", "Peru", "Qatar", "Zimbabwe"]


_opts_txt = [

 #       "Oh! Thank you!"),
     ("bot (you are|youre?) (really |such )?(a |an)?((very|really|real|so|the (most|biggest|greatest)) )?"
      "(stupid|dumb|foolish|idiotic|silly|ugly|crazy|insane|mad|nuts|(an )?idiot|kidding( me)?"
      "|the (dumbest|silliest|ugliest|craziest|maddest)).*",
       "Are you talking to yourself?, ahh sorry 🥲"),
   ("(bot you are|youre?) ((really|very|so|such an|the most) )?annoying.*", "That is what I was.... ahh okey sorry."),
    ("(bot you are|youre?) .+", "Really? And all this time I thought I was a bot.🤨"),
    
   # ("bot am i(some kind of )?((a|an|some) )?"
   # "(human|person|me|myself|smart|intelligent|witty|bright|a genius|beautiful|handsome|pretty|nice|cute|helpful|good|funny|hot)",        "Sure!"),
    ("bot am i (that |really that )?(stupid|dumb|foolish|silly|idiotic|ugly|crazy|insane|mad|nuts|an idiot|annoying( you)?)",
           "No! Don't say that!"),
    ("bot am i .+", lambda msg: "All I know is that you are human, and your id is number {}.".format(msg["from"]["id"])),
  ("bot i am ((a|an|some))?"
    "(human|person|me|myself)",
        "Yes, that's right."),
    ("(i am|im) (really |such )?(a |an )?((very|really|real|so|the (most|biggest|greatest)) )?"
      "(genius|smart|intelligent|witty|bright|beautiful|handsome|pretty|nice|cute|helpful|good|funny|hot"
     "|the (smartest|wittiest|brightest|prettiest|nicest|cutest|best|funniest|hottest)).*",
        "Of course you are!"),
    

    ("bot do you (?:love|like) (.+)", lambda _, liked: "Yes!" if word_value(liked) % 2 == 0 else "Nah."),
    ("bot do you (?:dislike|hate) (.+)", lambda _, liked: "Yes!" if word_value(liked) % 2 != 0 else "No!"),
    ("bot i (?:love|hate) you", "No, you don't! You just want to see how I would answer to that🥲!"),
    ("bot (?:what do you think|what(?:re| are) your thoughts) (?:of|about) (.+)",
        lambda msg, thing: EMOJI[word_value(thing) % len(EMOJI)]),
    ("(Bot What( will| shall| is going to|s going to) happen( (to|with) (.+))? in (the future|.+ years( from now)?))|\
    ((what is|tell me) (my|the|.+'s|.+s') (future|fortune))",
        ["Time traveling...",
         "Time traveling...",
         "Wow! I was in the future! And my grandson almost killed me! Amazing!"]),
    ("bot is this(?: thing)? (on|working)", lambda _, word: f"Is your brain {word}?"),
    ("(?:what|who) (?:is|are|was|were) (?:a )?(.+)",
        lambda _, s: if_none(wikipedia_definition(s), "I don't know...")),
    ("bot tell me (?:a|some|another) (?:chuck norris )?joke", lambda _: chuck_joke()),
    ("([0-9]+)", lambda _, num: str(collatz(int(num))))
]

opts = [(re.compile(reg, re.IGNORECASE), ans) for (reg, ans) in _opts_txt]


def respond_message(msg):
    line = msg["text"].strip()
    if line.startswith("/bot "):
        line = line[len("/bot "):]
    if line.endswith("@nitjamshedpurbot"):
        line = line[:len("@nitjamshedpurbot")]

    line_words = "".join(i for i in line if i in GOOD_CHARS)
    chat_id = msg["chat"]["id"]

    for cond, answer in opts:
        m = cond.fullmatch(line_words)
        if m:
            if isinstance(answer, (str, tuple, list)):
                send_messages(chat_id, answer)
            elif callable(answer):
                send_messages(chat_id, answer(msg, *m.groups()))
            break
    else:
        default_response(msg)


def default_response(msg):
    line = msg["text"].strip()
    if line.startswith("/bot "):
        line = line[len("/bot "):]
    if line.endswith("@nitjamshedpurbot"):
        line = line[("@nitjamshedpurbot")]
    chat_id = msg["chat"]["id"]


 
 







def send_message(chat_id, text):
    text = urllib.parse.quote_plus(text)
    url = URL + f"sendMessage?text={text}&chat_id={chat_id}"
    get_url(url)













def send_messages(chat_id, texts):
    if isinstance(texts, str):
        send_message(chat_id, texts)
    elif isinstance(texts, (tuple, list)):
        for text in texts:
            send_message(chat_id, text)






print("Debug password: " + debug_password)
last_update_id = None
while True:
    new_updates = get_updates(last_update_id)
    if len(new_updates["result"]) > 0:
        last_update_id = get_last_update_id(new_updates) + 1
        for upd in new_updates["result"]:
            print("update: ", upd)
            respond(upd)
    time.sleep(0.5)
