import requests
import datetime
import json
import tkinter as tk



# def get_api_data(nb_day_forecast):

#     url = "https://weatherapi-com.p.rapidapi.com/forecast.json"
#     # city = input('Enter a city : ')
#     city = 'Quebec'
#     date = current_date = datetime.date.today().strftime("%Y-%m-%d")
    
#     querystring = {"q":city,"days":nb_day_forecast,"dt":date}

#     headers = {
# 	"X-RapidAPI-Key": "05ee033960msh834d461df4fc349p1303d2jsned42163386bf",
# 	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
#     }

#     response = requests.get(url, headers=headers, params=querystring)
#     prettified_json = json.dumps(response.json(), indent=4)


#     # print(prettified_json)
#     data = response.json()

#     date =              data['location']['localtime'][:-5]
#     time =              data['location']['localtime'][11:]
#     temperature =       data['current']['temp_c']
#     wind =              data['current']['wind_kph']
#     humidity =          data['current']['humidity']
#     precipitation =     data['current']['precip_mm']

#     print(f'Current time : {time}')
#     print(f'Current date : {date}')
#     print(f'Current temperature (celcius): {temperature}')
#     print(f'Wind (kph): {wind}')
#     print(f'Humidity (percent) : {humidity}')
#     print(f'Precipitation (mm) : {precipitation}')

# get_api_data(1)



def submit():
    input_text = entry.get()
    result_label.config(text=f"You entered: {input_text}")

# Create a root window
root = tk.Tk()
root.title("Input Box Example")

# Create an Entry widget for text input
entry = tk.Entry(root)
entry.pack(pady=10)

# Create a button to submit the input
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack()

# Create a label to display the result
result_label = tk.Label(root, text="")
result_label.pack()

# Run the Tkinter event loop
root.mainloop()