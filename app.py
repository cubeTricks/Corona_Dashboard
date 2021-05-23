from flask import Flask, render_template,request
import backend_1
from datetime import datetime,timedelta

app = Flask(__name__, static_folder='static')
@app.route('/', methods=['GET','POST'])


def index():
    countries_list_for_output=[]
    countries_list=backend_1.countries_list()
    current_date=datetime.now()+timedelta(days=-1)
    current_date=current_date.strftime('%Y-%m-%d')
    selected_date=current_date
    selected_country_data={}
    selected_country_data_vaccine={}
    
    current_date_for_html={'c_date':current_date}
    for i in countries_list:
        tmp_row={'country_name':i}
        countries_list_for_output.append(tmp_row)
        countries=countries_list_for_output

    selected_country=request.form.get('country')
    selected_date=request.form.get('process_date')

    
    
    if selected_date==current_date:
        selected_country_data=backend_1.country_data(selected_country,selected_date)
        selected_country_data_vaccine=backend_1.vaccine_data(selected_country)
        
    elif selected_date is not None:
        selected_country_data=backend_1.country_data(selected_country,selected_date)
        selected_country_data_vaccine=backend_1.vaccine_data(selected_country)
    
    return render_template('index.html',countries=countries,html_data=selected_country_data,html_data_vaccine=selected_country_data_vaccine,current_date_for_html=current_date_for_html)
    
    
    
if __name__ == "__main__":    

    app.run(host="192.168.1.2",port=7081,debug=True,threaded=True)
   
