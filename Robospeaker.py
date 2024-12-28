# FIRST PYTHON PROJECT 001

import pyttsx3

if __name__ == '__main__':
    print("Welcome to Robospeaker 1.1. Created by Anish")

    # Initialize the pyttsx3 engine
    engine = pyttsx3.init()

    voices = engine.getProperty('voices')
    for i , voice in  enumerate(voices):
        print(f" voice{i}: {voice.name}-{voice.id}")    
    while True:    
        voice_choice= int(input(f"enter a number from 0 to {len(voices)-1}: "))
        if  voice_choice in range(0,len(voices)):

            while True:
                # voice_choice= int(input(f"enter a number from 0 to {len(voices)-1}: "))
                engine.setProperty('voice',voices[voice_choice].id)
            
                engine.say("this is selected voice test ")
                engine.runAndWait()
                change_voice=input('you want to change voice yes/no: ').strip().lower()
                if change_voice == "yes" :
                    while True:
                        voice_choice= int(input(f"enter a number from 0 to {len(voices)-1}: "))
                        if voice_choice not in range(0,len(voices)):
                            print("please enter valid change_voice input ")
                        else:
                            break


                else:
                    break

            break
        else :
            print("please choose the correct voice_choice input")
 
    
    engine.setProperty('rate', 150)  #rate(speed) set  of sound 
    engine.setProperty('volume', 1)  #volume set of sound


    while True:
        x = input("Enter what you want me to speak: ").lower()
        if x == "quit":
            break

        # Speak the input text
        engine.say(x)
        engine.runAndWait()




