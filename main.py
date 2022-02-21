import requests
from tkinter import *
import tkinter as tk
from tkinter import ttk

class currency_converter():
    def __init__(self,url):
        self.data= requests.get(url).json()
        self.currencies = self.data['rates']

    def converter(self, from_currency, to_convert, amount):
        # Convert the currency to dollar
        if from_currency != 'USD':
            amount = amount / self.currencies[from_currency]
        # Convert dollars to the final currency
        amount = round((amount * self.currencies[to_convert]), 2)
        return amount


if __name__ == '__main__':
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    instance = currency_converter(url)
    print(instance.converter('USD', 'EUR', 1))