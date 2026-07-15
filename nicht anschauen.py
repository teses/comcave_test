import time
import webbrowser


RICKROLL_URL = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

lyrics = [
    "We're no strangers to love...",
    "You know the rules and so do I (do I)...",
    "A full commitment's what I'm thinking of...",
    "You wouldn't get this from any other guy...",
    "\nCHORUS:",
    "NEVER GONNA GIVE YOU UP!",
    "NEVER GONNA LET YOU DOWN!",
    "NEVER GONNA RUN AROUND AND DESERT YOU!",
    "NEVER GONNA MAKE YOU CRY!",
    "NEVER GONNA SAY GOODBYE!",
    "NEVER GONNA TELL A LIE AND HURT YOU! 🎶"
]

def rickroll():
    print("Starte wichtiges System-Update...")
    time.sleep(2)
    print("Fortschritt: 33%...")
    time.sleep(1.5)
    print("Fortschritt: 66%...")
    time.sleep(1.5)
    print("Fortschritt: 100%!")
    print("\n[!] FEHLER: Systemüberlastung durch zu viel Groove!\n")
    time.sleep(1)

   
    webbrowser.open(RICKROLL_URL)

    
    for line in lyrics:
        print(line)
        time.sleep(1.5) 

if __name__ == "__main__":
    rickroll()