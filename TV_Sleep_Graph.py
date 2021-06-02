import plotly_express as px
import csv

with open('TV_VS_Size.csv') as file:
    df = csv.DictReader(file)
    fig  = px.scatter(df,x = "Size of TV",y = "Average time spent watching TV in a week")
    fig.show()
