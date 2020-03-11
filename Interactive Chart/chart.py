import plotly
import plotly.graph_objects as go
import pandas as pd


excel_file = 'sales.xlsx'
df = pd.read_excel(excel_file)
print(df)

# Designate x axis and y axis using plotly scatter graph
data = [go.Scatter(x=df['Date'], y=df['Profit'])]

# Plot & Show in a graph
fig = go.Figure(data)
fig.show()

# Save the chart in a html format
plotly.offline.plot(fig, filename="Report.html")
