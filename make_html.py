
def make_html():
    return "<!DOCTYPE html>" + "\n" + \
        "<html lang=\"en\">"  + "\n" + \
        "  <head>"  + "\n" + \
        "    <meta charset=\"UTF-8\">" + "\n" + \
        "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">"  + "\n" +\
        "    <title>Basic HTML Page</title>"  + "\n" + \
        "    <link rel=\"stylesheet\" href=\"Mission3_Formatting.css\">"  + "\n" +\
        "  </head>" + "\n" +\
        "  <body>" + "\n" +\
        "    <h1>Markov Face</h1>" + "\n" +\
        "    <h2>Lydia Pitts: Mission 3</h2>" + "\n" +\
        "    <div class=\"Face\"> " + "\n" +\
        "        <div class=\"Eyes_Nose\">" + "\n" + \
        "            <img class=\"leftEye\" src=\"" + eye1 + "\"></img>" + "\n" + \
        "            <img class=\"rightEye\" src=\"" + eye2 + "\"></img>" + "\n" + \
        "        </div>" + "\n" + \
        "        <img class=\"nose\" src=\"" + nose + "\"></img>" + "\n" + \
        "        <img class=\"mouth\" src=\"" + mouth + "\"></img>" + "\n" + \
        "    </div>" + "\n" + \
        "  </body>" + "\n" + \
        "</html>"