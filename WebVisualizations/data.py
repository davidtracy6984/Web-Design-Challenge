import pandas as pd
data_df = pd.read_csv('Resources/cities.csv')
#print(data_df)
htmlData = data_df.to_html()
#print(htmlData)
##data_df.to_html('table.html')
#This will populate the existing data.html file with the table after removing hashtags below
text_file = open("data.html", "w")
text_file.write(htmlData)
text_file.close()