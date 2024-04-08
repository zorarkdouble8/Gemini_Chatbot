# Gemini_Chatbot
A easy to use command line chatbot to answer any questions that come up!
<img width="473" alt="WindowsTerminal_Py2r0pZoG9" src="https://github.com/zorarkdouble8/Gemini_Chatbot/assets/65358496/7ac37d07-52f3-4c62-ab5d-3dd2aa7417ea">

# How to use:
1. Get an AI API key from google: https://makersuite.google.com/app/apikey
2. Put the Api key into the variable name GOOGLE_API_KEY in the env.py file
3. Run the program and talk to Gemini!

# Customization:
The gemini model outputs markdown but the command prompt can't output markdown. Therefore, the markdown is converted to HTML and then each tag is replaced with a color key or symbol that displays in the command prompt.
To Customize, edit the htmlToColor dictionary in the customization.py file
