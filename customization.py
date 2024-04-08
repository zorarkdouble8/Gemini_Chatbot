import markdown

class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

htmlToColor = {
    "<strong>" : color.BOLD,
    "</strong>" : color.END,

    "<em>" : color.UNDERLINE,
    "</em>" : color.END,

    "<p>" : "",
    "</p>" : "\n",

    "<li>" : "- ",
    "</li>" : "",

    "<ul>" : "",
    "</ul>" : "",
    
    "<code>" : color.GREEN,
    "</code>" : color.END
}

def customizeMarkdown(text):
    html = markdown.markdown(text)

    for key in htmlToColor:
        html = html.replace(key, htmlToColor[key])

    #Not really html anymore b/c the purpose is to remove all the tags
    return html
      
   