import datetime
import os
import webbrowser

def open_website(website_name):
    supported_websites = {
        'google': 'https://www.google.com',
        'youtube': 'https://www.youtube.com'
    }
    try:
        if website_name in supported_websites:
            webbrowser.open(supported_websites[website_name])
            return f"Opening {website_name}..."
        else:
            return f"Sorry, I don't support opening {website_name} at the moment."
    except Exception as e:
        return f"Error opening {website_name}: {e}"
    
def open_software(software_name):
    supported_software = {
        'calculator': 'calc',
        'notepad': 'notepad.exe'
    }

    try:
        if software_name in supported_software:
            os.system(supported_software[software_name])
            return f"Opening {software_name}..."
        else:
            return f"Sorry, I don't support opening {software_name} as software at the moment."
    except Exception as e:
        return f"Error opening {software_name}: {e}"  
    
def open_google_search(query):
    google_search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    webbrowser.open(google_search_url)
    return f"Searching for '{query}' on Google..."
def open_youtube_search(query):
    youtube_search_url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
    webbrowser.open(youtube_search_url)
    return f"Searching for '{query}' on YouTube..." 
   
def get_current_date_time():
    current_datetime = datetime.datetime.now()
    return current_datetime.strftime("%Y-%m-%d %H:%M:%S")

def rule_based_chatbot(user_input):

    if "hello jimmy" in user_input.lower():
        return "hey..! How can I help you today ?"
    elif "how are you ?" in user_input.lower():
        return "I'm doing well. Thank you! What's about you ?"
    elif "i am fine" in user_input.lower():
        return "ohh Thats sounds nice..!"
    elif "what is your name ?" in user_input.lower():
        return "I am your Personal Chatbot. You can call me Jimmy."
    elif "ok nice name" in user_input.lower():
        return "Thank you sir, Its my pleasure."
    elif "who created you ?" in user_input.lower():
        return "I was created by you sir..Are you forgetting me ?"
    elif "ok can you help me jimmy" in user_input.lower():
        return "of course I'm here to assist you. Feel free to ask me anything!"
    elif "what is todays date jimmy" in user_input.lower():
        return f"Today's date is {get_current_date_time().split()[0]}."
    elif "what the time now" in user_input.lower():
        return f"The current time is {get_current_date_time().split()[1]}."
    
    elif "open" in user_input.lower() and "website" in user_input.lower():
        # Extract website name from the user input
        website_name = user_input.lower().replace("open", "").replace("website", "").strip()
        return open_website(website_name)
    elif "open" in user_input.lower() and "software" in user_input.lower():
        # Extract software name from the user input
        software_name = user_input.lower().replace("open", "").replace("software", "").strip()
        return open_software(software_name)
    
    elif "search on google" in user_input.lower():
        query = user_input.lower().replace("search on google", "").strip()
        return open_google_search(query)
    elif "search on youtube" in user_input.lower():
        query = user_input.lower().replace("search on youtube", "").strip()
        return open_youtube_search(query)
    else:
        return "I'm sorry, I didn't understand that."

while True:
    user_input=input("You: ")
        
    if user_input.lower() == "exit":
        print("Good bye ! See you later.")
        break

    response= rule_based_chatbot(user_input)
    print("Chatbot:",response)

#This Chatbot is created by Dhrubojyoti Chakraborty (Codsoft Internship Task 1).

    
    