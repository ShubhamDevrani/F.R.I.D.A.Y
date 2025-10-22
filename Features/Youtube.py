import webbrowser

def YoutubeSearch(Data):

    Data = Data.replace("friday","")
    Data = Data.replace("open youtube and search", "")
    Data = Data.replace("search on youtube", "")
    Data = Data.replace("search on youtube that", "")

    webbrowser.open(f"www.youtube.com/results?search_query={Data}")