import speech_recognition as sr
from ccyacc import parser
from difflib import get_close_matches


def main_loop(commands):
    source = sr.Microphone()
    recog = sr.Recognizer()
    recog.pause_threshold = 0.5

    while True:
        try:
            with source as s:
                audio = recog.listen(s)
                text = recog.recognize_google(audio)
                if text == 'exit'
                    break;
                matches = get_close_matches(text, commands, cutoff=0.7)
                if matches:
                    for command in commands[matches[0]]:
                        command.execute()
        except:
            pass


if __name__ == "__main__":
    fname = input("Command File: ")
    with open(fname, 'r') as fin:
        commands = parser.parse(''.join(line for line in fin))
    main_loop(commands)
    pass
