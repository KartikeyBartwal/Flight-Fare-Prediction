from flask import Flask,request,render_template
import pandas as pd
import numpy as np
import pickle
import sklearn
from flask_cors import cross_origin
import os


app=Flask(__name__)
model=pickle.load(open('flight_fare_model.pkl',"rb"))




@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")

@app.route("/prediction",methods=["GET","POST"])
@cross_origin()
def predict():
  if request.method=="POST":
    # Airline "Air Asia was removed in model for dummy variable trap"
    Airline=request.form["Airline"]
    if Airline =="Air India":
      Air_India = 1
      GoAir= 0
      IndiGo= 0
      Jet_Airways= 0
      Jet_Airways_Business= 0
      Multiple_carriers= 0
      Multiple_carriers_Premium_economy= 0
      SpiceJet= 0
      Trujet= 0
      Vistara= 0
      Vistara_Premium_economy= 0

    elif Airline== 'GoAir':
      Air_India = 0
      GoAir= 1
      IndiGo= 0
      Jet_Airways= 0
      Jet_Airways_Business= 0
      Multiple_carriers= 0
      Multiple_carriers_Premium_economy= 0
      SpiceJet= 0
      Trujet= 0
      Vistara= 0
      Vistara_Premium_economy= 0
      
    elif Airline== 'IndiGo':
      Air_India = 0
      GoAir= 0
      IndiGo= 1
      Jet_Airways= 0
      Jet_Airways_Business= 0
      Multiple_carriers= 0
      Multiple_carriers_Premium_economy= 0
      SpiceJet= 0
      Trujet= 0
      Vistara= 0
      Vistara_Premium_economy= 0
      
    elif Airline== 'Jet Airways':
      Air_India = 0
      GoAir= 0
      IndiGo= 0
      Jet_Airways= 1
      Jet_Airways_Business= 0
      Multiple_carriers= 0
      Multiple_carriers_Premium_economy= 0
      SpiceJet= 0
      Trujet= 0
      Vistara= 0
      Vistara_Premium_economy= 0
      
    elif Airline== 'Jet Airways Business':
      Air_India = 0
      GoAir= 0
      IndiGo= 0
      Jet_Airways= 0
      Jet_Airways_Business= 1
      Multiple_carriers= 0
      Multiple_carriers_Premium_economy= 0
      SpiceJet= 0
      Trujet= 0
      Vistara= 0
      Vistara_Premium_economy= 0
      
    elif Airline== 'Multiple carriers':
      Air_India = 0
      GoAir= 0
      IndiGo= 0
      Jet_Airways= 0
      Jet_Airways_Business= 0
      Multiple_carriers= 1
      Multiple_carriers_Premium_economy= 0
      SpiceJet= 0
      Trujet= 0
      Vistara= 0
      Vistara_Premium_economy= 0
      
    elif Airline=='Multiple carriers Premium economy':
      Air_India = 0
      GoAir= 0
      IndiGo= 0
      Jet_Airways= 0
      Jet_Airways_Business= 0
      Multiple_carriers= 0
      Multiple_carriers_Premium_economy= 1
      SpiceJet= 0
      Trujet= 0
      Vistara= 0
      Vistara_Premium_economy= 0
      
    elif Airline== 'SpiceJet':
      Air_India = 0
      GoAir= 0
      IndiGo= 0
      Jet_Airways= 0
      Jet_Airways_Business= 0
      Multiple_carriers= 0
      Multiple_carriers_Premium_economy= 0
      SpiceJet= 1
      Trujet= 0
      Vistara= 0
      Vistara_Premium_economy= 0
      
    elif Airline== 'Trujet':
      Air_India = 0
      GoAir= 0
      IndiGo= 0
      Jet_Airways= 0
      Jet_Airways_Business= 0
      Multiple_carriers= 0
      Multiple_carriers_Premium_economy= 0
      SpiceJet= 0
      Trujet= 1
      Vistara= 0
      Vistara_Premium_economy= 0
      
    elif Airline== 'Vistara':
      Air_India = 0
      GoAir= 0
      IndiGo= 0
      Jet_Airways= 0
      Jet_Airways_Business= 0
      Multiple_carriers= 0
      Multiple_carriers_Premium_economy= 0
      SpiceJet= 0
      Trujet= 0
      Vistara= 1
      Vistara_Premium_economy= 0
      
    elif Airline== 'Vistara Premium economy':
      Air_India = 0
      GoAir= 0
      IndiGo= 0
      Jet_Airways= 0
      Jet_Airways_Business= 0
      Multiple_carriers= 0
      Multiple_carriers_Premium_economy= 0
      SpiceJet= 0
      Trujet= 0
      Vistara= 0
      Vistara_Premium_economy= 1
      
    else:
      Air_India = 0
      GoAir= 0
      IndiGo= 0
      Jet_Airways= 0
      Jet_Airways_Business= 0
      Multiple_carriers= 0
      Multiple_carriers_Premium_economy= 0
      SpiceJet= 0
      Trujet= 0
      Vistara= 0
      Vistara_Premium_economy= 0
      
    
    #Date of Journey
    Date_of_Journey=request.form["Date of Journey"]
    Journey_Date=int(pd.to_datetime( Date_of_Journey,format="%Y-%m-%d").day)
    Journey_Mnth=int(pd.to_datetime( Date_of_Journey,format="%Y-%m-%d").month)
    Journey_Day =Journey_Date
    Journey_Month =Journey_Mnth
    
    #Source "S_Banglore was removed in model for dummy variable trap"
    Source=request.form["Source"]
    if Source == 'S_Kolkata': 
        S_Kolkata=1
        S_Delhi=0
        S_Chennai=0
        S_Mumbai=0
      
    elif Source == 'S_Delhi':
        S_Kolkata=0
        S_Delhi=1
        S_Chennai=0
        S_Mumbai=0
      
    elif Source == 'S_Chennai':
        S_Kolkata=0
        S_Delhi=0
        S_Chennai=1
        S_Mumbai=0
      
    elif Source == 'S_Mumbai':
        S_Kolkata=0
        S_Delhi=0
        S_Chennai=0
        S_Mumbai=1
      
    else:
        S_Kolkata=0
        S_Delhi=0
        S_Chennai=0
        S_Mumbai=0
      
    
    #Destination "D_Banglore was removed in model for dummy variable trap"
    Final_Destination=request.form["Final_Destination"]
    if Final_Destination=="D_Cochin":
        D_Cochin =1
        D_Delhi=0
        D_Hyderabad=0
        D_Kolkata=0
        D_New_Delhi=0
       
    elif Final_Destination=='D_Delhi':
        D_Cochin =0
        D_Delhi=1
        D_Hyderabad=0
        D_Kolkata=0
        D_New_Delhi=0
       
    elif Final_Destination=='D_Hyderabad':
        D_Cochin =0
        D_Delhi=0
        D_Hyderabad=1
        D_Kolkata=0
        D_New_Delhi=0
       
    elif Final_Destination=='D_Kolkata':
        D_Cochin =0
        D_Delhi=0
        D_Hyderabad=0
        D_Kolkata=1
        D_New_Delhi=0
       
    elif Final_Destination=='D_New Delhi':
        D_Cochin =0
        D_Delhi=0
        D_Hyderabad=0
        D_Kolkata=0
        D_New_Delhi=1
       
    else:
        D_Cochin =0
        D_Delhi=0
        D_Hyderabad=0
        D_Kolkata=0
        D_New_Delhi=0
       
   

    #Departure Time
    Departure_Time=request.form["Departure Time"]
    Dep_Hr=int(pd.to_datetime(Departure_Time, format="%H:%M").hour)
    Dep_Min=int(pd.to_datetime(Departure_Time, format="%H:%M").minute)
    Dep_Hour = Dep_Hr
    Dep_min = Dep_Min


    #Duration 
    Duration_of_Flight=request.form["Duration of Flight"]
    duration_Hr=pd.to_datetime(Duration_of_Flight,format="%H:%M").hour
    duration_Min=pd.to_datetime(Duration_of_Flight,format="%H:%M").minute
    duration_hours = duration_Hr
    duration_mins = duration_Min

    #Total Stops
    Total_Stop=int(request.form["Total Stops"])
    Total_Stops =Total_Stop




    prediction=model.predict([[Air_India, GoAir, IndiGo, Jet_Airways, Jet_Airways_Business,
       Multiple_carriers, Multiple_carriers_Premium_economy, SpiceJet,
       Trujet, Vistara, Vistara_Premium_economy, D_Cochin, D_Delhi,
       D_Hyderabad, D_Kolkata, D_New_Delhi, S_Chennai, S_Delhi,
       S_Kolkata, S_Mumbai, Total_Stops,Journey_Month,
       Journey_Day, Dep_Hour, Dep_min, duration_hours,
       duration_mins
]])
     
    output=round(prediction[0],2)

    return render_template('home.html',prediction_text="Your Flight price is Rs. {}".format(output))
  return render_template("home.html")
    
if __name__ == "__main__":
    app.run(debug=True)

