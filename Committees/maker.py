import pandas as pd

df = pd.read_excel('Committee.xlsx')
short = df["Short"]
full = df["Full"]
head = df["Head"]
members = df["Members"]
color = df["Colours"]
style = df["Additional_styles"]


x = len(short)

for i in range(0, x):

    #COMMITEE LOGOS
    logo = "../C_Logos/"+str(short[i])+".svg"

    #TEXT COLOUR
    if color[i] == "#FFBC42":
        col = "black"
    elif color[i] == "#FF718F":
        col = "black"
    elif color[i] == "#06D6A0":
        col = "black"
    else:
        col = "white"


    #MEMBERS
    member1 = members[i].replace("(", "<li>")
    member = member1.replace(")", "</li>")

    #COMMITTEE ARTICLES
    f = open('C_Articles\\'+str(short[i])+".txt", "r")
    article2 = f.read()
    article1 = article2.replace("(", "<p>")
    article = article1.replace(")", "</p><br>")


    #ARTICLE TITLE
    if article == "&nbsp;":
        a_title = " "
    else:
        a_title = "Commmittee Article"

    #STUDENT HEAD(S)
    
    if len(head[i]) < 15:
        head_desc = 'Student head: '
    else:
        head_desc = 'Student heads: '

    #WRITING THE HTML
    html = open(str(short[i])+".html", "w")
    code = """
    <!DOCTYPE html>
        <html lang="en">

        <head>
        <link rel="shortcut icon" type="image/svg" href='"""+logo+"""'/>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="author" content='"""+full[i]+"""'>
        <title>"""+full[i]+"""</title>
        <link rel="preconnect" href="https://fonts.gstatic.com">
        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap" rel="stylesheet">
        </head>

        <body>
        <div class="header">
            <div class="banner">
                <img src='"""+logo+"""' alt='"""+full[i]+""" Logo' class="logo">
                <h1>"""+full[i]+"""</h1>
                <h4>"""+head_desc+head[i]+"""</h4>
            </div>
            <div class="members">
                <h3>Committee Members</h3>
                <ol class='C_Members'>
                    """+member+"""
                </ol>
            </div>
        </div>
        <div class="article">
            <h3 class='a_title'>"""+a_title+"""</h3>
            <div class="text">
                <div class="actual_text">
                    """+article+"""
                </div>
            </div>
        </div>


        <style>
            * {
                padding: 0;
                margin: 0;
                box-sizing: border-box;
                font-family: 'Poppins', sans-serif;
            }

            .header {
                background: #0D1321;
            }

            .logo {
                width: 2in;
                margin: 30px 0;
                margin-left: calc(50% - 1in);
                transition: 0.3s;
            }
            .logo::-moz-selection {
                color: inherit;
                background: none;
            }

            .logo::selection {
                color: inherit;
                background: none;
            }
            h1 {
                text-align: center;
                width: 90%;
                margin-left: 5%;
                margin-bottom: 20px;
                color: white;
            }

            h3 {
                text-align: center;
                margin-bottom: 10px;
                color: """+col+""";
            }


            h4 {
                font-weight: lighter;
                text-align: center;
                width: 90%;
                margin-left: 5%;
                color: white;
                padding-bottom: 30px;
            }

            .a_title{
                color: black;
            }

            .members {
                background-color: """+color[i]+""";
                color:"""+col+""";
                padding: 20px;
            }

            .C_Members{
                padding-left: 30px;
                color:"""+col+""";
            }
            

            ::-moz-selection {
                color: """+col+""";
                background: """+color[i]+""";
            }

            ::selection {
                color: """+col+""";
                background: """+color[i]+""";
            }

            .article {
                width: 80%;
                text-align: justify;
                margin: 10%;
            }


            @media (min-width: 400px) and (max-width: 700px) {
                ol {
                    width: 70%;
                    margin-left: 15%;
                }
            }


            @media (min-width: 700px) {
                .header {
                    display: grid;
                    grid-template-columns: 1.5fr 1fr;
                }
                .article{
                    margin-top: 4%;
                }
            }

            @media (min-width: 900px) {
                .header {
                    grid-template-columns: 3fr 1fr;
                }

                h1 {
                    margin-bottom: 5px;
                }
            }

            @media (min-width: 1200px) {
                .header {
                    grid-template-columns: 4fr 1fr;

                }
            }
        </style>

        <!-- CUSTOM SCROLLBAR -->
        <style>
            /* width */
            ::-webkit-scrollbar {
                width: 14px;
            }

            /* Track */
            ::-webkit-scrollbar-track {
                background: #fff;
            }

            /* Handle */
            ::-webkit-scrollbar-thumb {
                background: #ccc;
                border: 3px #fff solid;
                border-radius: 10px;
            }

            /* Handle on hover */
            ::-webkit-scrollbar-thumb:hover {
                background: #999999;
            }
        </style>

        <!--Navigation Menu-->
        <div class="menu-container" onclick="myFunction(this)">
            <div class="nav-container">
                <div class="headings">
                    <div class="nav home" draggable="true" ondrag="window.location.href='Navigation.html';">Home</div>
                    <div class="nav articles">Articles</div>
                    <div class="nav gallery">Gallery</div>
                    <div class="nav staff">Staff</div>
                    <div class="nav more">More...</div>
                </div>
                <abbr title="Navigation Menu (Click)">
                    <div class="container">
                        <div class="bar1"></div>
                        <div class="invis"></div>
                        <div class="bar3"></div>
                    </div>
                </abbr>

                <script>function myFunction(x) {
                        x.classList.toggle("change");
                    }</script>
                <style>
                    html {
                        margin: 0;
                        padding: 0;
                        box-sizing: border-box;
                    }


                    .nav-container {
                        width: 350px;
                        height: 100vh;
                        background: #0a0a14;
                        margin: 0px;
                        position: fixed;
                        left: -350px;
                        top: 0;
                        transition: 0.5s;
                    }

                    .change .nav-container {
                        left: 0px;
                    }

                    .headings {
                        color: #06D6A0;
                        width: 350px;
                        position: absolute;
                        top: 52%;
                        left: -300px;
                        transform: translate(0%, -50%);
                        font-family: 'Poppins', sans-serif;
                        font-weight: bold;
                        text-align: left;
                        font-size: 3em;
                        line-height: 1.75em;
                        cursor: pointer;
                        transition: 0.5s;

                    }

                    .change .headings {
                        left: 50px;
                    }

                    .headings:hover>div {
                        opacity: 0;
                        transition: 0.5s ease-in-out;
                        transform: translate(-5px);
                    }

                    .headings:hover>div:hover {
                        color: rgb(255, 78, 152);
                        opacity: 1;
                        transform: translate(5px);
                        transition: 0.2s ease-in-out;
                    }

                    .nb {
                        position: absolute;
                        top: 50%;
                        left: 50%;
                        transform: translate(-50%, -50%);
                        font-size: 25em;
                        font-family: 'Poppins', sans-serif;
                        font-weight: bold;
                        text-align: center;
                        z-index: -1;
                        opacity: 0.03;
                        color: white;
                    }

                    .nav-container::-moz-selection {
                        color: inherit;
                        background: none;
                    }

                    .nav-container::selection {
                        color: inherit;
                        background: none;
                    }

                    .container {
                        display: inline-block;
                        cursor: pointer;
                        margin: 40px;
                        position: fixed;
                        left: -10px;
                        top: -10px;
                        background-color: #0D1321;
                        padding: 10px;
                    }

                    .change .container {
                        background: none;
                    }

                    .bar1,
                    .bar3 {
                        width: 35px;
                        height: 3px;
                        border-radius: 1.5px;
                        background-color: #fff;
                        margin: 2px 0;
                        transition: 0.3s;
                    }

                    .invis {
                        width: 20px;
                        height: 3px;
                        margin: 3px 0;
                    }

                    .change .bar1 {

                        transform: rotate(-45deg) translate(-2px, 6px);
                        background-color: #fff;
                    }

                    .change .bar3 {
                        background-color: #fff;
                        transform: rotate(45deg) translate(-2px, -6px);
                    }



                    @media only screen and (max-width: 750px) {
                        .nav-container {
                            width: 100%;
                            opacity: 1;
                            left: -100%;
                        }

                        .nb {
                            display: none;
                        }

                        html {
                            overflow: scroll;
                        }
                    }
                </style>
            </div>
        </div>
        
        """+style[i]+"""

        </body>
        </html>

""" # ADDITIONAL STYLES TO BE ADDED (style[i])

    code1 = code.replace("""
        <!--Navigation Menu-->
        <div class="menu-container" onclick="myFunction(this)">
            <div class="nav-container">
                <div class="headings">
                    <div class="nav home" draggable="true" ondrag="window.location.href='Navigation.html';">Home</div>
                    <div class="nav articles">Articles</div>
                    <div class="nav gallery">Gallery</div>
                    <div class="nav staff">Staff</div>
                    <div class="nav more">More...</div>
                </div>
                <abbr title="Navigation Menu (Click)">
                    <div class="container">
                        <div class="bar1"></div>
                        <div class="invis"></div>
                        <div class="bar3"></div>
                    </div>
                </abbr>

                <script>function myFunction(x) {
                        x.classList.toggle("change");
                    }</script>
                <style>
                    html {
                        margin: 0;
                        padding: 0;
                        box-sizing: border-box;
                    }


                    .nav-container {
                        width: 350px;
                        height: 100vh;
                        background: #0a0a14;
                        margin: 0px;
                        position: fixed;
                        left: -350px;
                        top: 0;
                        transition: 0.5s;
                    }

                    .change .nav-container {
                        left: 0px;
                    }

                    .headings {
                        color: #06D6A0;
                        width: 350px;
                        position: absolute;
                        top: 52%;
                        left: -300px;
                        transform: translate(0%, -50%);
                        font-family: 'Poppins', sans-serif;
                        font-weight: bold;
                        text-align: left;
                        font-size: 3em;
                        line-height: 1.75em;
                        cursor: pointer;
                        transition: 0.5s;

                    }

                    .change .headings {
                        left: 50px;
                    }

                    .headings:hover>div {
                        opacity: 0;
                        transition: 0.5s ease-in-out;
                        transform: translate(-5px);
                    }

                    .headings:hover>div:hover {
                        color: rgb(255, 78, 152);
                        opacity: 1;
                        transform: translate(5px);
                        transition: 0.2s ease-in-out;
                    }

                    .nb {
                        position: absolute;
                        top: 50%;
                        left: 50%;
                        transform: translate(-50%, -50%);
                        font-size: 25em;
                        font-family: 'Poppins', sans-serif;
                        font-weight: bold;
                        text-align: center;
                        z-index: -1;
                        opacity: 0.03;
                        color: white;
                    }

                    .nav-container::-moz-selection {
                        color: inherit;
                        background: none;
                    }

                    .nav-container::selection {
                        color: inherit;
                        background: none;
                    }

                    .container {
                        display: inline-block;
                        cursor: pointer;
                        margin: 40px;
                        position: fixed;
                        left: -10px;
                        top: -10px;
                        background-color: #0D1321;
                        padding: 10px;
                    }

                    .change .container {
                        background: none;
                    }

                    .bar1,
                    .bar3 {
                        width: 35px;
                        height: 3px;
                        border-radius: 1.5px;
                        background-color: #fff;
                        margin: 2px 0;
                        transition: 0.3s;
                    }

                    .invis {
                        width: 20px;
                        height: 3px;
                        margin: 3px 0;
                    }

                    .change .bar1 {

                        transform: rotate(-45deg) translate(-2px, 6px);
                        background-color: #fff;
                    }

                    .change .bar3 {
                        background-color: #fff;
                        transform: rotate(45deg) translate(-2px, -6px);
                    }



                    @media only screen and (max-width: 750px) {
                        .nav-container {
                            width: 100%;
                            opacity: 1;
                            left: -100%;
                        }

                        .nb {
                            display: none;
                        }

                        html {
                            overflow: scroll;
                        }
                    }
                </style>
            </div>
        </div>""", "<!--INSERT NAVBAR USING PYTHON-->")

    html.write(code1)
    html.close()
    print(short[i])


