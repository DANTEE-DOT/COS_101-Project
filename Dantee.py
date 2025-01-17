
from tkinter import Tk, Entry, Button, Label, StringVar
from tkinter import Toplevel


window = Tk()
window.geometry("800x600")
window.title("My work")

label = Label( text="Please select a language", font=('Times New Roman', 18))
label.pack(padx=20, pady=20)


def open_new_window():
    new_window = Toplevel(window)
    new_window.title("Japanese Window")
    new_window.geometry("300x200")

    entry_text = Entry(new_window)
    entry_text.pack()

    result = StringVar()
    result_label = Label(new_window, textvariable=result)
    result_label.pack()

    japanese_dictionary = {
    "hello": "konnichiwa",
    "thank you": "arigatou",
    "goodbye": "sayounara",
    "good morning": "ohayou",
    "good evening": "konbanwa",
    "excuse me": "sumimasen",
    "yes": "hai",
    "no": "iie",
    "love": "ai",
    "friend": "tomodachi",
    "family": "kazoku",
    "food": "tabemono",
    "drink": "nomimono",
    "school": "gakkou",
    "teacher": "sensei",
    "student": "gakusei",
    "time": "jikan",
    "japan": "nihon",
    "cat": "neko",
    "dog": "inu",
}

    def search(word):
        if word in japanese_dictionary.keys():
            result.set(japanese_dictionary[word])
            print(japanese_dictionary[word])
        else:
            result.set("Not Found")

    search_btn = Button(new_window, text="Search", font=("Times New Roman", 14), command=lambda: search(entry_text.get()))
    search_btn.pack()


button = Button(window, text="Japanese", width=50, height=2,font=('Times New Roman', 14), command=open_new_window)
button.pack(pady=20)



def open_new_window():
    new_window = Toplevel(window)
    new_window.title("hausa dictionary")
    new_window.geometry("300x300")


    entry_text = Entry(new_window)
    entry_text.pack()


    result = StringVar()
    result_label = Label(new_window, textvariable=result)
    result_label.pack()

    hausa_dictionary = {
        "house": "gida",
        "car": "mota",
        "hospital": "asibiti",
        "boy": "yaro",
        "girl": "yarinya",
        "tomorrow": "gobe",
        "school": "makaranta",
        "chicken": "kaza",
        "hand": "ido",
        "wash": "wanke",
        "elephant": "giwa",
        "yam": "doya",
        "potato": "dankali",
        "chair": "kujera",
        "donkey": "jaki",
        "horse": "doki",
        "money": "kudi",
        "mosque": "masallaci",
        "shoe": "takalmi",
        "twenty": "ashirin"
    }


    def search(word):
        if word in hausa_dictionary.keys():
            result.set(hausa_dictionary[word])
            print(hausa_dictionary[word])
        else:
            result.set("Not Found")


    search_btn = Button(new_window, text="Search", font=("Times New Roman", 14), command=lambda: search(entry_text.get()))
    search_btn.pack()


button2= Button(window, text="Hausa", width=50, height=2,font=('Times New Roman', 14), command=open_new_window)
button2.pack(pady=20)

def open_new_window():
    new_window = Toplevel(window)
    new_window.title("Zulu dictionary")
    new_window.geometry("400x300")


    entry_text = Entry(new_window)
    entry_text.pack()

    result = StringVar()
    result_label = Label(new_window, textvariable=result)
    result_label.pack()

    Zulu_dictionary = {
        'sawubona': "Hello",
        'ngiyabonga': "Thank you",
        'hamba kahle': "Goodbye",
        'kusasa': "Tomorrow",
        'umndeni': "Family",
        'umngane': "Friend",
        'uthando': "Love",
        'amanzi': "Water",
        'ukudla': "Food",
        'isikhathi': "Time",
        'isikhumbuzo': "Memory",
        'umsebenzi': "Work",
        'umfundi': "Student",
        'uthisha': "Teacher",
        'ikhaya': "Home",
        'umhlaba': "World",
        'isibhedlela': "Hospital",
        'imoto': "Car",
        'isikhwama': "Bag",
        'izicathulo': "Shoes"
    }

    def search(word):
        word = entry_text.get().lower()
        if word in Zulu_dictionary.keys():
            print(Zulu_dictionary[word])
        else:
            result.set("Not Found")

    search_btn = Button(new_window, text="search", font=("Times New Roman", 14), command=lambda : search(entry_text.get()))
    search_btn.pack()


button3= Button(window, text="Zulu", width=50, height=2,font=('Times New Roman', 14),command=open_new_window)
button3.pack(pady=20)

def open_new_window():
    new_window = Toplevel(window)
    new_window.title("German Window")
    new_window.geometry("300x200")

    entry_text = Entry(new_window)
    entry_text.pack()

    result = StringVar()
    result_label = Label(new_window, textvariable=result)
    result_label.pack()

    german_dictionary = {
        "apfel": "apple",
        "baum": "tree",
        "haus": "house",
        "katze": "cat",
        "hund": "dog",
        "auto": "car",
        "stuhl": "chair",
        "tisch": "table",
        "buch": "book",
        "blume": "flower",
        "schule": "school",
        "lehrer": "teacher",
        "freund": "friend",
        "wasser": "water",
        "essen": "food",
        "hemd": "shirt",
        "hose": "pants",
        "tage": "days",
        "monat": "month",
        "jahre": "years",
    }

    def search():
        word = entry_text.get().lower()
        if word in german_dictionary:
            result.set(german_dictionary[word])
        else:
            result.set("Not Found")

    search_btn = Button(new_window, text="Search", font=("Times New Roman", 14), command=search)
    search_btn.pack()

button4 = Button(window, text="german", width=50, height=2, font=('Times New Roman', 14), command=open_new_window)
button4.pack(pady=20)

def open_new_window():
    new_window = Toplevel(window)
    new_window.title("Igbo windows")
    new_window.geometry("300x300")

    entry_text = Entry(new_window)
    entry_text.pack()

    result = StringVar()
    result_label = Label(new_window, textvariable=result)
    result_label.pack()

    english_to_igbo_dict = {
        "hello": "Ndewo",
        "goodbye": "Ka ọ dị",
        "thank you": "Daalụ",
        "please": "Biko",
        "yes": "Ee",
        "no": "Mba",
        "how are you?": "Kedu?",
        "I love you": "A hụrụ m gị n’anya",
        "friend": "Enyi",
        "family": "Ezinụlọ",
        "water": "Mmiri",
        "food": "Nri",
        "house": "Ụlọ",
        "book": "Akwụkwọ",
        "school": "Ụlọ akwụkwọ",
        "sun": "Anwụ",
        "moon": "Onwa",
        "star": "Kpakpando",
        "child": "Nwa",
        "man": "Nwoke",
    }

    def search(word):
        word = word.lower()
        if word in english_to_igbo_dict:
            print (english_to_igbo_dict[word])
        else:
            print ("Translation not found")

    search_btn = Button(new_window, text="search", font=("Times New Roman", 14), command=lambda: search (entry_text.get()))
    search_btn.pack()

button5 = Button(window, text="Igbo", width=50, height=2, font=('Times New Roman', 14), command=open_new_window)
button5.pack(pady=20)

window.mainloop()