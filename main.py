from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
  if request.method == "POST":
    name = request.form['name']
    best_sub = request.form['best_sub']
    worst_sub = request.form['worst_sub']
    return redirect(url_for('results', name=name, best_sub=best_sub, worst_sub=worst_sub))
  return render_template('index.html')
  
best_GP = []
best_M = []
best_P = []
best_C = []
best_E = []
best_CL = []

@app.route('/results', methods=['GET','POST'])
def results():
  help_list = None
  name = request.args.get('name')
  best_sub = request.args.get('best_sub')
  worst_sub = request.args.get('worst_sub')
  with open('data.txt', 'a') as file:
    file.write(name + ','+ best_sub + ',' + worst_sub + '\n') 
  lines = []  
  with open('data.txt', 'r') as file:
    lines = file.readlines()

  for line in lines: 
    record = line.split(',')
    name = record[0]
    best_sub = record[1]      
    if best_sub == "GP":
      best_GP.append(name)
    if best_sub == "Math":
      best_M.append(name)
    if best_sub == "Computing":
      best_C.append(name)
    if best_sub == "Physics":
      best_P.append(name)
    if best_sub == "Economics":
      best_E.append(name)
    if best_sub == "Chinese":
      best_CL.append(name)
    
    worst_sub = record[2]
    if worst_sub == "GP":
      help_list = best_GP
    if worst_sub == "Math":
      help_list = best_M
    if worst_sub == "Computing":
      help_list = best_C
    if worst_sub == "Physics":
      help_list = best_P
    if worst_sub == "Economics":
      help_list = best_E
    if worst_sub == "Chinese":
      help_list = best_CL
 
  return render_template('results.html', best_sub=best_sub, worst_sub=worst_sub, help_list=help_list) 
  

app.run(host='0.0.0.0', port=81)