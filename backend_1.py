import pandas as pd
import numpy as np
from datetime import timedelta
import os

file_path=r'C:\Users\chait\Downloads\WHO-COVID-19-global-data_May5_db.csv'



#selected_country=input('Enter the required country Name : ')
#selected_country='India'
df1=pd.read_csv(file_path)
column_names=df1.columns.values
#print(column_names)



metric1=column_names[0] # date_reported
metric2=column_names[2] # Country
metric3=column_names[4] # New cases
metric4=column_names[5] # cumutaltive cases
metric5=column_names[6] # new deaths
metric6=column_names[7] # cumulative deaths

def countries_list():

    countires_list=df1[metric2].tolist()
    countires_list = list(dict.fromkeys(countires_list))
#print(countires_list)
    #print(len(countires_list))
    return countires_list
    
    
def country_data(selected_country):
    df11=pd.DataFrame()
    country_name=[]
    #print('shape of dataframe:',df11.shape)
    
    country_name.append(selected_country)
    ctry_wise_df=df1[df1[metric2].isin(country_name)]
    #print(ctry_wise_df)
    tmp_x_axis_dates=df1[metric1].tolist()
    tmp_x_axis_dates1=set(tmp_x_axis_dates)
    x_axis_dates_today=sorted(tmp_x_axis_dates1)
    x_axis_dates=x_axis_dates_today[0:len(x_axis_dates_today)-1]
    c_day1=[]
    c_day1.append(x_axis_dates[-1])
    c_day1.append(x_axis_dates[-2])
    c_day1.append(x_axis_dates[-3])

    #print(c_day1)
    #df1=self.ctry_wise_df[self.ctry_wise_df[self.metric1].isin(self.c_day1)]

    df11=ctry_wise_df[ctry_wise_df[metric1].isin(c_day1)]

    #print(df11)
    
    
    selected_country_data_for_html=[]
#print(df11.iloc[0].tolist())
#print(type(df11.iloc[0]))
    #print(df11.shape)
    #print(df11)
    if df11.shape[0]>1:
        tmp_rows=[]
        tmp_rows.append(df11.iloc[2].tolist())
        tmp_rows.append(df11.iloc[1].tolist())
        tmp_rows.append(df11.iloc[0].tolist())
        #print(tmp_rows)
        
        for i in tmp_rows:
            tmp_selected_country_data_for_html_row={'Date':i[0],'Country_Name':i[2],'New_Cases':i[4],'Cummulative_Cases':i[5],'New_Deaths':i[6],'Cummulative_Deaths':i[7]}
            selected_country_data_for_html.append(tmp_selected_country_data_for_html_row)
    #print(selected_country_data_for_html)
    return selected_country_data_for_html
    
#country_data('India')