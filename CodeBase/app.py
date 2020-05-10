from flask import Flask, render_template, url_for, request
from flask_bootstrap  import Bootstrap
from sklearn.externals import joblib
import pandas as pd

# create the application object
app = Flask(__name__)
Bootstrap(app) 

# use decorators to link the function to a url
@app.route('/')
def home():
    return render_template('welcome.html')

@app.route('/predict', methods=['POST'])

def predict():

	daily_val={'tot': 78,
			   'sat_fat': 20,
			   'chol': 300,  
			   'sodium': 2300,
			   'carbs': 275,
			   'fiber':28,
			   'sugar':0,
			   'prot':50,
			   'vitd':20,
			   'calc':1300,
			   'iron':18,
			   'potas':4700
			   }

	food_indices = joblib.load(r'finalized_model.sav')
	dataset = pd.read_csv(r"Preprocessed_dataset.csv")

	if request.method == 'POST':
	    food_list = []
	    energy_kcal = []
	    denergy_kcal = []
	    tot = []
	    dtot = []
	    sat_fat = []
	    dsat_fat = []
	    chol = []
	    dchol = []
	    sodium = []
	    dsodium = []
	    carbs = []
	    dcarbs = []
	    fiber = []
	    dfiber = []
	    sugar = []
	    dsugar = []
	    prot  = []
	    dprot  = []
	    vitd  = []
	    dvitd  = []
	    calc  = []
	    dcalc  = []
	    iron  = []
	    diron  = []
	    potas = []
	    dpotas = []

	    foodname = request.form['namequery']
	    print(foodname)

	    index = dataset[dataset['Itemname'].str.upper().str.contains(foodname)].index.tolist()[0]
	    pred_list = []
	    given_list = []

	    g_name=dataset.iloc[index]['Itemname']
	    g_ener_kcal=dataset.iloc[index]['Energ_Kcal']
	    g_tot=dataset.iloc[index]['Lipid_Tot_(g)']
	    g_sfat=dataset.iloc[index]['FA_Sat_(g)']
	    g_chol=dataset.iloc[index]['Cholestrl_(mg)']
	    g_sod=dataset.iloc[index]['Sodium_(mg)']
	    g_carbs=dataset.iloc[index]['Carbohydrt_(g)']
	    g_fiber=dataset.iloc[index]['Fiber_TD_(g)']
	    g_sugar=dataset.iloc[index]['Sugar_Tot_(g)']
	    g_prot=dataset.iloc[index]['Protein_(g)']
	    g_vitd=dataset.iloc[index]['Vit_D_µg']
	    g_calc=dataset.iloc[index]['Calcium_(mg)']
	    g_iron=dataset.iloc[index]['Iron_(mg)']
	    g_potas=dataset.iloc[index]['Potassium_(mg)']

	    gd_tot=''
	    gd_sfat=''
	    gd_chol=''
	    gd_sod=''
	    gd_carbs=''
	    gd_fiber=''
	    gd_sugar=''
	    gd_prot=''
	    gd_vitd=''
	    gd_calc=''
	    gd_iron=''
	    gd_potas=''

	    for key,val in daily_val.items():
	    	if(val!=0):
	    		if(key=='tot'):
	    			gd_tot=round((g_tot/val)*100)
	    		elif(key=='sat_fat'):
	    			gd_sfat=round((g_sfat/val)*100)
	    		elif(key=='chol'):
	    			gd_chol=round((g_chol/val)*100)
	    		elif(key=='sodium'):
	    			gd_sod=round((g_sod/val)*100)
	    		elif(key=='carbs'):
	    			gd_carbs=round((g_carbs/val)*100)
	    		elif(key=='fiber'):
	    			gd_fiber=round((g_fiber/val)*100)
	    		elif(key=='sugar'):
	    			gd_sugar=round((g_sugar/val)*100)
	    		elif(key=='prot'):
	    			gd_prot=round((g_prot/val)*100)
	    		elif(key=='vitd'):
	    			gd_vitd=round((g_vitd/val)*100)
	    		elif(key=='calc'):
	    			gd_calc=round((g_calc/val)*100)
	    		elif(key=='iron'):
	    			gd_iron=round((g_iron/val)*100)
	    		elif(key=='potas'):
	    			gd_potas=round((g_potas/val)*100)

	    given_list.append((g_name,g_ener_kcal ,g_tot, g_sfat,g_chol,g_sod,g_carbs,g_fiber,g_sugar,g_prot,g_vitd,g_calc,g_iron,g_potas,
	    	gd_tot,gd_sfat,gd_chol,gd_sod,gd_carbs,gd_fiber,gd_sugar,gd_prot,gd_vitd,gd_calc,gd_iron,gd_potas))

	    for i in food_indices[index][1:]:
	    	food_list.append(dataset.iloc[i]['Itemname'])
	    	energy_kcal.append(dataset.iloc[i]['Energ_Kcal'])
	    	tot.append(dataset.iloc[i]['Lipid_Tot_(g)'])
	    	sat_fat.append(dataset.iloc[i]['FA_Sat_(g)'])
	    	chol.append(dataset.iloc[i]['Cholestrl_(mg)'])
	    	sodium.append(dataset.iloc[i]['Sodium_(mg)'])
	    	carbs.append(dataset.iloc[i]['Carbohydrt_(g)'])
	    	fiber.append(dataset.iloc[i]['Fiber_TD_(g)'])
	    	sugar.append(dataset.iloc[i]['Sugar_Tot_(g)'])
	    	prot.append(dataset.iloc[i]['Protein_(g)'])
	    	vitd.append(dataset.iloc[i]['Vit_D_µg'])
	    	calc.append(dataset.iloc[i]['Calcium_(mg)'])
	    	iron.append(dataset.iloc[i]['Iron_(mg)'])
	    	potas.append(dataset.iloc[i]['Potassium_(mg)'])

	    

	    for ele in tot:
	    	val=daily_val['tot']
	    	if(val!=0):
	    		dtot.append(round((ele/val)*100))
	    	else:
	    		dtot.append('')


	    for ele in sat_fat:
	    	val=daily_val['sat_fat']
	    	if(val!=0):
	    		dsat_fat.append(round((ele/val)*100))
	    	else:
	    		dsat_fat.append('')
	    
	    for ele in chol:
	    	val=daily_val['chol']
	    	if(val!=0):
	    		dchol.append(round((ele/val)*100))
	    	else:
	    		dchol.append('')
	    
	    for ele in sodium:
	    	val=daily_val['sodium']
	    	if(val!=0):
	    		dsodium.append(round((ele/val)*100))
	    	else:
	    		dsodium.append('')
	    
	    for ele in carbs:
	    	val=daily_val['carbs']
	    	if(val!=0):
	    		dcarbs.append(round((ele/val)*100))
	    	else:
	    		dcarbs.append('')
	    
	    for ele in fiber:
	    	val=daily_val['fiber']
	    	if(val!=0):
	    		dfiber.append(round((ele/val)*100))
	    	else:
	    		dfiber.append('')
	    
	    for ele in sugar:
	    	val=daily_val['sugar']
	    	if(val!=0):
	    		dsugar.append(round((ele/val)*100))
	    	else:
	    		dsugar.append('')
	    
	    for ele in prot:
	    	val=daily_val['prot']
	    	if(val!=0):
	    		dprot.append(round((ele/val)*100))
	    	else:
	    		dprot.append('')
	    
	    for ele in vitd:
	    	val=daily_val['vitd']
	    	if(val!=0):
	    		dvitd.append(round((ele/val)*100))
	    	else:
	    		dvitd.append('')
	    
	    for ele in calc:
	    	val=daily_val['calc']
	    	if(val!=0):
	    		dcalc.append(round((ele/val)*100))
	    	else:
	    		dcalc.append('')
	    
	    for ele in iron:
	    	val=daily_val['iron']
	    	if(val!=0):
	    		diron.append(round((ele/val)*100))
	    	else:
	    		diron.append('')
	    
	    for ele in potas:
	    	val=daily_val['potas']
	    	if(val!=0):
	    		dpotas.append(round((ele/val)*100))
	    	else:
	    		dpotas.append('')
	    
	    
	    pred_list = zip(food_list,energy_kcal,tot,sat_fat,chol,sodium,carbs,fiber,sugar,prot,vitd,calc,iron,potas,dtot,dsat_fat,dchol,dsodium,dcarbs,dfiber,dsugar,dprot,dvitd,dcalc,diron,dpotas)
	    print(given_list)
	 	   
	    return render_template('results_temp.html', name = foodname.upper(), given = given_list, pred_val = pred_list)

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)