from flask import Flask, render_template, request
import time
app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def home():
    
    curr = time.time()
    curr=time.ctime(curr)
    
    if request.method=='POST':
        if 'timer' in request.form:
           return render_template('timer.html')
        if 'alarm' in request.form:
           return render_template('alarm.html')
        
        if 'backtoclock' in request.form:
         return render_template('main.html',time=curr)
        if 'timerstart' in request.form:
         a=functime()
         
         a1='Start'
         return render_template('timer.html',content1=a1)
        if 'setingtime' in request.form:
           d=request.form.get('inputtime')
           d=str(d)

           return render_template('alarm.html',myv=d)
        if 'timerstop' in request.form:
         s=curr1
         b=funcstop()
         c=int(b-s)
         c=str(c)
         return render_template('timer.html', time=curr,content1='End', content2=c)
   
    else:
         return render_template('main.html',time=curr)
@app.route('/processform',methods=['GET','POST'])
def processform():
   
   
   if request.method=='POST':
      if 'setingtime' in request.form:
         global username
         
         username = request.form.get('inputtime')
         #return render_template('alarm.html',myv=username)
         if username:
            me=message(username)
            return render_template('alarm.html',myv=me)
         #return render_template('alarm.html',myv=username)
   else:
      return render_template('alarm.html',myv=username)

def message(use_rname):
    p=''
    while p!='Time Is Over':
        curr = time.time()
        curr=time.ctime(curr)
        h=username[0:2]
        min=username[3:5]
        hh=curr[-13:-11]
        mm=curr[-10:-8]
        if (h==hh) and (mm==min):
            p='Time Is Over'
    return p

def current():
   global curr
   curr = time.time()
   curr=time.ctime(curr)
   return curr



def functime():
   global curr1
   curr1 = time.time()
   return curr1


def funcstop():
   curr2 = time.time()
   return curr2
