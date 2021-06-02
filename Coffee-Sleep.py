import plotly_express as px
import csv

with open('Coffee_VS_Sleep.csv') as file:
    df = csv.DictReader(file)
    fig  = px.scatter(df,x = "Coffee in ml",y = "sleep in hours",color = "week")
    fig.show()
