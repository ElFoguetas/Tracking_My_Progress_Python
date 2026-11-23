# Challenge: Dark Mode Toggle
# Update the settings dictionary, then write a function that switches
# between light and dark mode.

settings = {
    "theme": "light",
    "font_size": 14,
    "autosave": True,
} 

# 1. Programmatically add a "background" key to the dictionary, and set its value to "white".
# 2. Programmatically delete the "autosave" key from the dictionary.

# Expected output:
# {"theme": "light", "font_size": 14, "background": "white"}

# 3. Write a function called toggle_theme(settings) that switches the theme between "light"
#    and "dark". It should change the background color to match: white for light mode, black for dark mode. Print the theme and background each time the function runs.
# 4. Call toggle_theme(settings) four times to make sure it switches back and forth from dark to light.

# Expected output:
# Theme: dark
# Background: black
# Theme: light
# Background: white
# Theme: dark
# Background: black
# Theme: light
# Background: white

settings["background"] = "white"
del settings["autosave"]
print(settings)

def toggle_theme(settings):
    if settings["background"] == "white":
        settings["background"] = "black"
    else:
        settings["background"] = "white"

toggle_theme(settings)
print(settings)
toggle_theme(settings)
print(settings)
toggle_theme(settings)
print(settings)
toggle_theme(settings)
print(settings)