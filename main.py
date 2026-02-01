import socket
import time

HOST = "0.0.0.0"
PORT = 2323
CLEAR = "\033[H\033[J"

def send(conn, text):
    conn.sendall(text.encode("utf-8", errors="ignore"))

def frame(conn, scene, text="", delay=3.0):
    send(conn, CLEAR)
    send(conn, scene + "\n")
    if text:
        send(conn, "\n" + text + "\n")
    time.sleep(delay)

# ===== CHARACTERS =====

HAYKO_1 = r"""
  o
 /|\
 / \
"""

HAYKO_2 = r"""
  o
 \|/
 / \
"""

FRIEND = r"""
  o
 /|\
  |
"""

MAN = r"""
  O
 /|\
 / \
"""

BUS = r"""
 _______________________
|   BUS BUS BUS BUS     |
|______________________|
   O               O
"""

BAR = r"""
==============================
|            BAR             |
==============================
"""

HOSPITAL = r"""
==============================
|          HOSPITAL          |
|         ROOM 203           |
==============================
"""

BED = r"""
   _____________
  |             |
  |   HAYKO     |
  |_____________|
"""

ROAD = "=============================="

# ===== SERVER =====

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(5)
    print("[+] Listening on 2323")

    while True:
        conn, addr = s.accept()
        print("[+] Connected:", addr)

        try:
            # ---- PART 1 ----

            for i in range(12):
                body = HAYKO_1 if i % 2 == 0 else HAYKO_2
                frame(conn, " " * i + body + BAR,
                      "* Hayko nervously enters the bar *", 0.35)

            frame(conn, BAR + HAYKO_1, "Hayko - Բարև ապեր", 2.5)
            frame(conn, BAR + HAYKO_2, "Barman - Բարև ապեր", 2.5)

            frame(conn, BAR + HAYKO_1,
                  "Hayko - Ախպեր ինձ շուտ տուր խմեմ ելի...", 3)

            frame(conn, BAR + HAYKO_2,
                  "Hayko - ԱՊԵ ԹՈՂԵՑ ԹՌԱՎՎՎ", 3)

            for i in range(14):
                frame(conn,
                      " " * (25 - i) + MAN + BAR,
                      "Man - Գոքոր Գոքոր, կնիկդ քեզ դավաճանումա", 0.25)

            frame(conn, HAYKO_2,
                  "Hayko - ՎԱՅ ՀՈՐՍ ԱՐԵՎ", 3)

            for i in range(16):
                body = HAYKO_1 if i % 2 == 0 else HAYKO_2
                frame(conn,
                      " " * i + body,
                      "* Hayko runs after him *", 0.18)

            frame(conn, BUS + "\n" + ROAD + "\n" + HAYKO_1,
                  "* BUS HITS HAYKO *", 3)

            # ---- PART 2 ----

            frame(conn,
                  "\n\n        PART 2\n   After the bus...\n",
                  "", 4)

            frame(conn,
                  HOSPITAL + "\n" + BED,
                  "* Hospital room *", 3)

            frame(conn,
                  HOSPITAL + "\n" + FRIEND + "   " + BED + "   " + FRIEND,
                  "Friend 1 - Էկար ախպերս", 4)

            frame(conn,
                  HOSPITAL + "\n" + FRIEND + "   " + BED + "   " + FRIEND,
                  "Friend 2 - Քո համար բերել ենք չայ, պիվա, սեմուշկա ու պիվա", 5)

            frame(conn,
                  HOSPITAL + "\n" + FRIEND + "   " + BED + "   " + FRIEND,
                  "Friend 1 - Դե հլը պատմի, ոնց եղավ ավտոբուսի տակ ընգար", 5)

            frame(conn,
                  HOSPITAL + "\n" + BED,
                  "Hayko - ՍԱՂ ՆԵՌՎԵՐԻՑԱ տղեք ջան, սաղ նեռվերիցա", 5)

            frame(conn,
                  HOSPITAL + "\n" + BED,
                  "Մտա բար, ասի մի բաժակ բան խմեմ...", 4)

            frame(conn,
                  HOSPITAL + "\n" + BED,
                  "Մեկը մտավ ասեց՝ Գոքոր, կնիկդ քեզ դավաճանումա", 4)

            frame(conn,
                  HOSPITAL + "\n" + BED,
                  "Ես գժված վազեցի դրա հետևից...", 4)

            frame(conn,
                  HOSPITAL + "\n" + BED,
                  "Ընկա ավտոբուսի տակ...", 4)

            frame(conn,
                  HOSPITAL + "\n" + BED,
                  "Ախր շատ նեռվայն եմ դառել տղեք ջան", 4)

            frame(conn,
                  HOSPITAL + "\n" + BED,
                  "Ոչ ամուսնացած եմ...", 3)

            frame(conn,
                  HOSPITAL + "\n" + BED,
                  "Ոչ անունսա Գոքոր...", 4)

            frame(conn,
                  "\n\n      վսյո պրծավ",
                  "", 6)

        except Exception as e:
            print("[-] Error:", e)

        finally:
            conn.close()
            print("[-] Disconnected:", addr)
