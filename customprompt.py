import os

# Define the custom symbol instead of @ as a Unicode character )
custom_symbol = @
# Example for Elder Futhark rune "ᛟ"
# custom_symbol = "\u16DF" 

# Define a function to customize the Bash prompt
def customize_bash_prompt():
    # Define the new PS1 prompt string with square brackets around the current directory
    new_prompt = (
        r'\[\e[0;96m\]┌──(\[\e[1;92m\]\u\[\e[0;96m\]'
        f'{custom_symbol}\[\e[1;96m\]\[\e[1;92m\]\h\[\e[0;96m\])-[\\[\e[1;92m\]\w\[\e[0;96m\]]'
        r'\n\[\e[0;96m\]└─\[\e[1;92m\]\$ \[\e[0m\]'
    )

    # Path to the .bashrc file
    bashrc_path = os.path.expanduser("~/.bashrc")

    # Check if .bashrc file exists
    if os.path.exists(bashrc_path):
        # Read the contents of .bashrc
        with open(bashrc_path, "r") as bashrc_file:
            bashrc_content = bashrc_file.read()

        # Check if the new PS1 prompt is already set
        if new_prompt in bashrc_content:
            print("Custom prompt is already set.")
        else:
            # Append the new PS1 prompt to the end of .bashrc
            with open(bashrc_path, "a") as bashrc_file:
                bashrc_file.write(f"\n# Custom Bash prompt\nPS1='{new_prompt}'\n")

            print("Custom prompt has been set. Please open a new terminal to see the changes.")
    else:
        print(f"Error: The .bashrc file does not exist at {bashrc_path}.")

if __name__ == "__main__":
    customize_bash_prompt()
