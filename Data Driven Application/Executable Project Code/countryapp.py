from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import requests
from io import BytesIO

root = Tk()
root.title("Country Citizen App")
root.geometry("600x450")
root.resizable(0, 0)

# Function to switch between frames
def Show_Frame(frame):
    frame.tkraise()

# Function to show instructions
def show_instructions():
    instructions = """
    Welcome to the Country Citizen App!
    
    1. On the first screen, click 'Next' to start searching for country details.
    2. Enter the name of a country in the input box on the second screen.
    3. Click 'Search' to fetch and display details about the country, including:
       - Country Name
       - Capital City
       - Population
       - Region and Subregion
       - Languages
       - National Flag
       - Currency Details
       - Weather Temperature
    4. Use the 'Currency' button to view the country's currency details.
    5. Use the 'Languages' button to view the languages spoken in the country.
    6. Use the 'Weather Temp' button to view the current weather temperature of the country.
    7. Use the 'Go Back' button to return to the home screen.
    
    Enjoy exploring the world!
    """
    messagebox.showinfo("Instructions", instructions,)

# Function to fetch country details and display results
def fetch_country_data():
    country_name = country_entry.get().strip()  # Get user input
    if not country_name:
        messagebox.showerror("Error", "Please enter a country name.")
        return

    url = f"https://restcountries.com/v3.1/name/{country_name}"
    try:
        # Fetch data from API
        response = requests.get(url)
        response.raise_for_status()
        country_data = response.json()[0]

        # Extract relevant information
        country_info = {
            "Country": country_data.get("name", {}).get("common", "N/A"),
            "Capital": ", ".join(country_data.get("capital", ["N/A"])),
            "Population": f"{country_data.get('population', 'N/A'):,}",
            "Region": country_data.get("region", "N/A"),
            "Subregion": country_data.get("subregion", "N/A"),
            "Languages": ", ".join(country_data.get("languages", {}).values()),
        }

        # Update the text box with country details
        result_text.set("\n".join([f"{key}: {value}" for key, value in country_info.items()]))

        # Fetch and display flag
        flag_url = country_data.get("flags", {}).get("png")
        if flag_url:
            flag_response = requests.get(flag_url)
            flag_response.raise_for_status()
            flag_image_data = BytesIO(flag_response.content)
            flag_image = Image.open(flag_image_data)
            flag_image.thumbnail((150, 100))  # Resize flag to fit the UI
            flag_photo = ImageTk.PhotoImage(flag_image)

            flag_label.configure(image=flag_photo)  # Display the flag
            flag_label.image = flag_photo
        else:
            flag_label.configure(image=None)
            flag_label.image = None

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Failed to fetch data: {e}")
    except (IndexError, KeyError):
        messagebox.showerror("Error", "Country not found or invalid response.")

# Function to fetch currency details
def fetch_currency_data():
    country_name = country_entry.get().strip()
    if not country_name:
        messagebox.showerror("Error", "Please enter a country name.")
        return

    url = f"https://restcountries.com/v3.1/name/{country_name}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        country_data = response.json()[0]

        currencies = country_data.get("currencies", {})
        currency_info = [f"{code}: {details.get('name', 'N/A')} ({details.get('symbol', 'N/A')})" for code, details in currencies.items()]

        result_text.set("Currency Details:\n" + "\n".join(currency_info))

    except requests.RequestException as e:
        messagebox.showerror("Error", f"Failed to fetch currency data: {e}")
    except (IndexError, KeyError):
        messagebox.showerror("Error", "Country not found or invalid response.")

# Function to fetch language details
def fetch_language_data():
    country_name = country_entry.get().strip()
    if not country_name:
        messagebox.showerror("Error", "Please enter a country name.")
        return

    url = f"https://restcountries.com/v3.1/name/{country_name}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        country_data = response.json()[0]

        languages = country_data.get("languages", {})
        language_info = ", ".join(languages.values())

        result_text.set(f"Languages:\n{language_info}")

    except requests.RequestException as e:
        messagebox.showerror("Error", f"Failed to fetch language data: {e}")
    except (IndexError, KeyError):
        messagebox.showerror("Error", "Country not found or invalid response.")

def fetch_weather_temperature():
    country_name = country_entry.get().strip()
    if not country_name:
        messagebox.showerror("Error", "Please enter a country name to check the weather.")
        return

    url = "https://api.openweathermap.org/data/2.5/weather"  # Replace with the correct API URL
    params = {
        "q": country_name,
        "appid": "4bfb31428663a9d547b191450dd85c95",  # Replace with your API key
        "units": "metric"
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        weather_data = response.json()
        
        weather_info = {
            "Location": weather_data.get("name", "N/A"),
            "Temperature": f"{weather_data['main']['temp']}°C",
            "Weather": weather_data["weather"][0]["description"].capitalize(),
        }
        result_text.set("\n".join([f"{key}: {value}" for key, value in weather_info.items()]))
    except requests.RequestException as e:
        messagebox.showerror("Error", f"Failed to fetch weather data: {e}")

# Frame 1
Frame1 = Frame(root, width=600, height=450)
Image1 = Image.open("A2 - DDA/Executable Project Code/CountryCitizenApp.png")
Resize_Image = Image1.resize((600, 450))
Background_Image = ImageTk.PhotoImage(Resize_Image)

Background_Label = Label(Frame1, image=Background_Image)
Background_Label.place(x=0, y=0)

Button1 = Button(Frame1, text="Instructions", bg="#f8cf2c", fg="black", font=("Arial", 10, "bold",), bd=0, command=show_instructions)
Button1.place(x=45, y=365)

Button2 = Button(Frame1, text="Next", bg="#f8cf2c", fg="black", font=("Arial", 16, "bold"), bd=0, command=lambda: Show_Frame(Button_Frame1))
Button2.place(x=232, y=360)
Frame1.place(x=0, y=0)

# Button Frame
Button_Frame1 = Frame(root, width=600, height=450)
Image2 = Image.open("A2 - DDA/Executable Project Code/CCA2.png")
Resize_Image1 = Image2.resize((600, 450))
Background_Image2 = ImageTk.PhotoImage(Resize_Image1)

Background_Label2 = Label(Button_Frame1, image=Background_Image2)
Background_Label2.place(x=0, y=0)

# Input field for country name
country_entry = Entry(Button_Frame1, width=24, font=("Arial", 12))
country_entry.place(x=190, y=90)

# Search button
search_button = Button(Button_Frame1, text="Search", bg="#C62300", fg="white", font=("Arial", 12, "bold"), bd=0, command=fetch_country_data)
search_button.place(x=260, y=136)

# Display for country details
result_text = StringVar()
result_label = Label(Button_Frame1, textvariable=result_text, bg="black", fg="white", font=("Arial", 12, "bold"), bd=0, justify=LEFT, width=42, height=7, anchor="nw")
result_label.place(x=88, y=220)

# Display for the flag
flag_label = Label(Button_Frame1, bg="black")
flag_label.place(x=366, y=220, width=150, height=100)

# "Go Back" button
back_button = Button(Button_Frame1, text="Go Back", bg="#149631", fg="white", font=("Arial", 12, "bold"), bd=0, command=lambda: Show_Frame(Frame1))
back_button.place(x=45, y=396)

# Buttons for new features
currency_button = Button(Button_Frame1, text="Currency", bg="#149631", fg="white", font=("Arial", 12, "bold"), bd=0, command=fetch_currency_data)
currency_button.place(x=188, y=397)

language_button = Button(Button_Frame1, text="Languages", bg="#149631", fg="white", font=("Arial", 10, "bold"), bd=0, command=fetch_language_data)
language_button.place(x=336, y=398)

weather_button = Button(Button_Frame1, text="Weather Temp", bg="#149631", fg="white", font=("Arial", 8, "bold"), bd=0, command=fetch_weather_temperature)
weather_button.place(x=476, y=400)

Button_Frame1.place(x=0, y=0)

# Show the first frame initially
Show_Frame(Frame1)

# Start the app
root.mainloop()