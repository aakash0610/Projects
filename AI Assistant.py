import wolframalpha
import PySimpleGUI as sg
import wikipedia
import pyttsx3

#App API call ID
client = wolframalpha.Client("EKQJRE-K9PGLG4WWP")

#text to sppech engine
engine = pyttsx3.init()


# Add a touch of color
sg.theme('DarkBlack')

# All the stuff inside your window.
layout = [  [sg.Text('Greetings From Highsenberg! ')],
            [sg.Text('Enter your search'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Highsenberg', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':	# if user closes window or clicks cancel
        break
    try:
        res = client.query(values[0])
        wolfram_res = next(res.results).text
        wiki_res = wikipedia.summary(values[0], sentences=3)
        engine.say(wolfram_res)
        if engine.say(wolfram_res) == null:
            engine.say(wiki_res)
        sg.PopupNonBlocking("Wolframe Results: "+wolfram_res, "Wikipedia Results: "+wiki_res)

    except (wikipedia.exceptions.DisambiguationError,wikipedia.exceptions.PageError):
        wolfram_res = next(res.results).text
        engine.say(wolfram_res)
        sg.PopupNonBlocking(wolfram_res)

    except:
        wiki_res = wikipedia.summary(values[0], sentences=3)
        engine.say(wiki_res)
        sg.PopupNonBlocking(wiki_res)
    engine.runAndWait()




window.close()