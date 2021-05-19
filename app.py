from flask import Flask, render_template,request
import backend_1

app = Flask(__name__, static_folder='static')
@app.route('/', methods=['GET','POST'])


def index():
    countries_list_for_output=[]
    countries_list=backend_1.countries_list()
 
    for i in countries_list:
        tmp_row={'country_name':i}
        countries_list_for_output.append(tmp_row)
        countries=countries_list_for_output

    selected_country=request.form.get('country')
    selected_country_data=backend_1.country_data(selected_country)
    selected_country_data_vaccine=backend_1.vaccine_data(selected_country)
    
    return render_template('index.html',countries=countries,html_data=selected_country_data,html_data_vaccine=selected_country_data_vaccine)
    
    
    
if __name__ == "__main__":    

    app.run(host="192.168.1.3",port=7081,debug=True,threaded=True)
   
