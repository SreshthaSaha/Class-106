import plotly_express as px
import csv

with open('Ice-Cream_VS_Temperature.csv') as file:
    df = csv.DictReader(file)
    fig  = px.scatter(df,x = "Temperature",y = "Ice-cream Sales")
    fig.show()

