import pandas as pd 

pd.set_option('display.width', 1000)
pd.set_option('colheader_justify', 'center')

df = pd.read_csv('cities.csv')

df.set_index(["City_ID"])

html_table = df.to_html()

file = open('cities.html', 'w')
file.write(html_table)
file.close()