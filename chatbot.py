print("Hello I am AI bot. What's your name?: ")
name = input()
print(f"Nice to meet you, {name}")

print("How are you feeling today? (good/bad) : ")
mood = input().lower()

if mood == "good":
    print("Im Glad to hear that!")
elif mood == "bad":
    print("Im sorry to hear that, hope things get better soon")
else:
    print("I see. Sometimes it's hard to put feelings into words.")
print(f"It was nice chatting with you {name}, goodbye!")