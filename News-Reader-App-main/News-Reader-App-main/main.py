import requests
import json
import pyttsx3

def speak(str):
    engine = pyttsx3.init()
    engine.setProperty('rate', 180)
    print(str)
    engine.say(str)
    engine.runAndWait()

if __name__ == '__main__':
    speak('Oh Hello! I am the News Reader Programmed By Bhaskar. I will read out the latest news for you!')
    speak("How Many News Do You Want to Hear?")
    a = int(input("How Many Latest News do you want to hear?: "))

    url1 = 'https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=fffbb9566eb047a0909f95ad7bc763e3'

    news1 = requests.get(url1).text
    news_json = json.loads(news1)
    articles = news_json['articles']  # Change 'article' to 'articles'

    for index, article in enumerate(articles):
        if index == a:
            break
        speak(f'''News Number - {index + 1}.. 
        Title - {article['title']}
        Description - {article['description']}
        Content - {article['content']}
        ''')

    speak("Thanks For Listening. Come Back Tomorrow For More News...")
