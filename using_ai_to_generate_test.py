from google import genai

client = genai.Client(api_key="AIzaSyCC50YnW_xy0SfDJkUjRY2aNVisniZmguE")

#response = client.models.generate_content(
 #   model="gemini-2.0-flash", contents="Explain how AI works in a few words"
#)
#print(response.text)

#PNOTE: takes a while to generate, maybe make loading screen ?
response = client.models.generate_content(                                                     #eventually should be for {user_food} or smthn
    model="gemini-2.0-flash", contents="Give me JUST the estimated cost of ingredients for italian sandwich, pb&j, mac and cheese, combine ingredients and list them all out in a numbered list with cost"
)

print(response.text)

