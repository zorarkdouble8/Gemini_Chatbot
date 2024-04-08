from timeit import default_timer
import math
import sys


import google.generativeai as genai
from env import GOOGLE_API_KEY
from customization import customizeMarkdown

global start
start = default_timer()

def main():
  print("Welcome to the simple Gemini AI Chatroom!\n")

  if (GOOGLE_API_KEY == "-1"):
    print("ERROR: You need to put your GOOGLE AI API key into the GOOGLE_API_KEY variable in the env.py file!")
    return

  isSuccessful = initialize()
  if (isSuccessful == False):
    return
  
  print("\nUsing models/gemini-pro")

  model = loadGemini("models/gemini-pro")
  chat = model.start_chat(history=[])


  startChat(model, chat)

def startChat(model, chat):
  print("----Now chatting with Gemini!----")
  while(True):
    print("\n----You----")
    command = input("Awaiting input: ")

    if (command == "Exit"):
      break

    print("\n----Gemini----")
    response = chat.send_message(command)
    print(customizeMarkdown(response.text))
    
    print("\nTotal tokens used:", model.count_tokens(chat.history), "Time thus far:", math.floor(((default_timer() - start) / 60) * 100) / 100, "Min")

def initialize():
  print("----Initializing----")
  try:
    genai.configure(api_key=GOOGLE_API_KEY)

    for m in genai.list_models():
      if 'generateContent' in m.supported_generation_methods:
        print(m.name)
  except:
    print("Error during initialization!")
    return
  

def loadGemini(modelName):
  return genai.GenerativeModel(modelName)


if (__name__ == "__main__"):
  main()



