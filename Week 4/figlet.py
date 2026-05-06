from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

def main():
    text = input("Enter text to convert: ")
    if len(sys.argv) == 1:
        random_font = random.choice(figlet.getFonts())
        figlet.setFont(font=random_font)
        print(figlet.renderText(text))
    elif len(sys.argv) == 3:
        font = sys.argv[1]
        rendered_text = sys.argv[2]
        if font == "-f" or font == "--font":
            if rendered_text not in figlet.getFonts():
                sys.exit("Invalid Usage")
            figlet.setFont(font = rendered_text)
            print(figlet.renderText(text))
        else:
            print("Invalid Usage")
            sys.exit(1)
    else:
        print("Invalid Usage")
        sys.exit(1)

    


    
    
if __name__ == "__main__":
    main()