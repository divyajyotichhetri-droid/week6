import emoji

name = input("Enter your name: ")
print(emoji.emojize(f"Hello {name}! :smile:"))

activity = input("Enter your favorite activity: ")

print(emoji.emojize(f"Enjoy {activity}! :thumbs_up:"))
print(emoji.emojize("Keep learning Python! :red_heart:"))
