import telebot
import requests
import json

from geotext import GeoText

bot = telebot.TeleBot("821473745:AAHBZmoM0qc05Udtkd-rDoww8nW8LJSFWQQ")

api_call = "http://api.openweathermap.org/data/2.5/weather?appid=e8634d1d07ae42cd0d64f21bee74922a&q=Delhi"
api_key = "e8634d1d07ae42cd0d64f21bee74922a"


@bot.message_handler(func=lambda message: "weather" in message.text)
def weather_related_queries(message):
    places = GeoText(message.text.title())
    api_call = f"https://api.openweathermap.org/data/2.5/weather?appid=e8634d1d07ae42cd0d64f21bee74922a&q={places.cities[0]}&units=metric"
    response = requests.get(api_call)
    json_output = json.loads(response.text)
    temp = json_output["main"]["temp"]
    bot.reply_to(message, f"Current Temperature at {places.cities[0]} is {temp}°C")


bot.polling()
