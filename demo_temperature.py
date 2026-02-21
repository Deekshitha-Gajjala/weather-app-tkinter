from tkinter import *
from tkinter import ttk
import requests

api_key = "YOUR_API_KEY"

url = "https://api.openweathermap.org/data/2.5/weather"

params = {
    "q": "Kadiri,IN",
    "units": "metric",
    "appid": api_key
}

response = requests.get(url, params=params)

print(response.status_code)
print(response.json())

win= Tk()
win.title("Weather app")
win.config(bg="lightblue")
win.geometry("500x570")
name_label=Label(win,text="Weather app",
                 font=("Times New Roman",30,"bold"))
name_label.place(x=25,y=50,height=50,width=450)
list_name=[
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
    "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand",
    "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur",
    "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab",
    "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura",
    "Uttar Pradesh", "Uttarakhand", "West Bengal"
]
com=ttk.Combobox(win,text="Weather app",values=list_name,
                 font=("Times New Roman",20,"bold"))
com.place(x=25,y=120,height=50,width=450)
def get_weather():
    city = com.get()

    if city == "":
        W_label1.config(text="Select City")
        return

    params = {
        "q": city + ",IN",
        "units": "metric",
        "appid": api_key
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()

        if response.status_code == 200:

            weather_main = data["weather"][0]["main"]
            weather_desc = data["weather"][0]["description"]
            temperature = data["main"]["temp"]
            pressure = data["main"]["pressure"]

            W_label1.config(text=weather_main)
            Wb_label1.config(text=weather_desc)
            temp_label1.config(text=str(temperature) + " °C")
            pre_label1.config(text=str(pressure) + " hPa")

        else:
            W_label1.config(text="City not found")

    except:
        W_label1.config(text="Network Error")
done_button=Button(win,text="Done",
                 font=("Times New Roman",20,"bold"),command=get_weather)
done_button.place(y=190,height=50,width=100,x=200)
W_label=Label(win,text="Weather climate",
                 font=("Times New Roman",17))
W_label.place(x=25,y=260,height=50,width=210)
W_label1=Label(win,text=" ",
                 font=("Times New Roman",17))
W_label1.place(x=250,y=260,height=50,width=210)
Wb_label=Label(win,text="Weather Description",
                 font=("Times New Roman",17))
Wb_label.place(x=25,y=330,height=50,width=210)
Wb_label1=Label(win,text="",
                 font=("Times New Roman",17))
Wb_label1.place(x=250,y=330,height=50,width=210)
temp_label=Label(win,text="Temperature",
                 font=("Times New Roman",17))
temp_label.place(x=25,y=400,height=50,width=210)
temp_label1=Label(win,text="",
                 font=("Times New Roman",17))
temp_label1.place(x=250,y=400,height=50,width=210)
pre_label=Label(win,text="Pressure",
                 font=("Times New Roman",17))
pre_label.place(x=25,y=470,height=50,width=210)
pre_label1=Label(win,text="",
                 font=("Times New Roman",17))
pre_label1.place(x=250,y=470,height=50,width=210)
state_capitals = {
    "Andhra Pradesh": "Amaravati",
    "Arunachal Pradesh": "Itanagar",
    "Assam": "Dispur",
    "Bihar": "Patna",
    "Chhattisgarh": "Raipur",
    "Goa": "Panaji",
    "Gujarat": "Gandhinagar",
    "Haryana": "Chandigarh",
    "Himachal Pradesh": "Shimla",
    "Jharkhand": "Ranchi",
    "Karnataka": "Bengaluru",
    "Kerala": "Thiruvananthapuram",
    "Madhya Pradesh": "Bhopal",
    "Maharashtra": "Mumbai",
    "Manipur": "Imphal",
    "Meghalaya": "Shillong",
    "Mizoram": "Aizawl",
    "Nagaland": "Kohima",
    "Odisha": "Bhubaneswar",
    "Punjab": "Chandigarh",
    "Rajasthan": "Jaipur",
    "Sikkim": "Gangtok",
    "Tamil Nadu": "Chennai",
    "Telangana": "Hyderabad",
    "Tripura": "Agartala",
    "Uttar Pradesh": "Lucknow",
    "Uttarakhand": "Dehradun",
    "West Bengal": "Kolkata"
}
win.mainloop()