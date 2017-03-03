import urllib;

def readText(filePath):
    text = open(filePath);
    fileContent = text.read();
    text.close();

    return checkProfanity(fileContent);


def checkProfanity(text):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + text);
    response = connection.read();
    connection.close();

    return response;


def checkText(filePath):
    hasCurse = readText(filePath);

    if "true" in hasCurse:
        print("Profanity Alert!!!");
    elif "false" in hasCurse:
        print("You are good to go!!!");
    else:
        print("Could not scan the document properly!!!");


checkText("text.txt");