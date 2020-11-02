
def make_html_doc(poem_name, file_name, line1, line2, line3, line4, line5):
     with open("poems/" + file_name + ".html", 'w') as new_poem:
        text = html_text(poem_name, line1, line2, line3, line4, line5)
        new_poem.write(text)
        new_poem.close()

def html_text(poem_name, line1, line2, line3, line4, line5):
    return "<!DOCTYPE html>" + "\n" + \
        "<html lang=\"en\">"  + "\n" + \
        "  <head>"  + "\n" + \
        "    <meta charset=\"UTF-8\">" + "\n" + \
        "    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">"  + "\n" +\
        "    <title>Basic HTML Page</title>"  + "\n" + \
        "    <link rel=\"stylesheet\" href=\"style.css\">"  + "\n" +\
        "  </head>" + "\n" +\
        "  <body>" + "\n" +\
        "    <h1>" + poem_name + "</h1>" + "\n" +\
        "    <p>" + "\n" +\
        "      " + line1 + "\n" +\
        "      <br>" + "\n" +\
        "      " + line2 + "\n"+\
        "      <br>" + "\n" +\
        "      " + line3 + "\n"+\
        "      <br>" + "\n" +\
        "      " + line4 + "\n"+\
        "      <br>" + "\n" +\
        "      " + line5 + "\n"+\
        "    <p>" + "\n" +\
        "    <button id=\"speakbtn\">Hear Poem</button>" + "\n\n" +\
        "    <br><br>" + "\n" +\
        "    Select Voice: <select name=\"\" id=\"voiceList\"></select>" + "\n\n" +\
        "    <script>" + "\n" +\
        "      var voiceList = document.querySelector(\'#voiceList\')" + "\n" +\
        "      var speakbtn = document.querySelector(\'#speakbtn\')" + "\n\n" +\
        "      var tts = window.speechSynthesis;" + "\n" +\
		"      var voices = [];" + "\n\n" +\
        "      var poem = \"" + line1 + ". " + line2 + ". " + line3 + ". " + line4 + ". " + line5 + ". \"" + "\n" +\
		"      GetVoices();" + "\n\n" +\
        "      if(speechSynthesis !== undefined){" + "\n" +\
		"	     speechSynthesis.onvoiceschanged = GetVoices;" + "\n" +\
		"      }" + "\n\n" +\
        "      speakbtn.addEventListener('click', ()=>{" + "\n" +\
        "        var toSpeak = new SpeechSynthesisUtterance(poem)" + "\n" +\
        "        var selectedVoiceName = voiceList.selectedOptions[0].getAttribute('data-name');" + "\n" +\
        "        voices.forEach((voice)=>{" + "\n" +\
        "          if(voice.name === selectedVoiceName){" + "\n" +\
        "            toSpeak.voice = voice;" + "\n" +\
        "          }" + "\n" +\
        "        });" + "\n" +\
        "        tts.speak(toSpeak);" + "\n" +\
        "      });" + "\n\n" +\
        "      function GetVoices(){" + "\n" +\
		"	     voices = tts.getVoices();" + "\n" +\
		"	     voiceList.innterHTML = '';" + "\n" +\
		"	     voices.forEach((voice)=>{" + "\n" +\
		"		    var listItem = document.createElement('option');" + "\n" +\
		"		    listItem.textContent = voice.name;" + "\n" +\
		"		    listItem.setAttribute('data-lang', voice.lang);" + "\n" +\
		"		    listItem.setAttribute('data-name', voice.name);" + "\n" +\
		"		    voiceList.appendChild(listItem);" + "\n" +\
		"	     });" + "\n" +\
		"	     voiceList.selectedIndex = 0;" + "\n" +\
		"      }" + "\n" +\
        "    </script>" + "\n" +\
        "  </body>" + "\n" + \
        "</html>"