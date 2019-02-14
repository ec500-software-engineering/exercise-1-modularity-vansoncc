import AI_module
import Analyzer
import Database_Module
import input_api
import OutputAlert_module
import random
import time
import threading


def main(dic):
    dic = {"ID": 1, "age": 22, "gender": 'Male', "heartrate": random.randint(50, 100),
           "Diastolic_BP": random.randint(40, 110), "Systolic_BP": random.randint(70, 160),
           "blood_oxygen": random.randint(50, 100),
           "temperature": random.randint(34, 39), "time": time.ctime()}
    #input module:
    patient = input_api.input_api(dic["ID"],dic["age"],dic["gender"],dic["heartrate"],dic["Diastolic_BP"],dic["Systolic_BP"],
                                  dic["blood_oxygen"],dic["temperature"],dic["time"])

    data1 =patient.return_request(1)
    patient.return_request(2)
    print("Patient Data:")
    print(data1)



    #Analyze module:
    data=Analyzer.Analyzer(dic["Systolic_BP"],dic["Diastolic_BP"],dic["heartrate"],dic["blood_oxygen"],dic["temperature"])
    Signal_Loss=data.Signal_Loss(dic["heartrate"],dic["temperature"])
    Shock_Alert=data.Shock_Alert(dic["heartrate"],dic["temperature"])
    Oxygen_Supply=data.Oxygen_Supply(dic["blood_oxygen"])
    Fever=data.Fever(dic["temperature"])
    Hypotension=data.Hypotension(dic["Systolic_BP"],dic["Diastolic_BP"])
    Hypertension=data.Hypertension(dic["Systolic_BP"],dic["Diastolic_BP"])

    #Database:
    database= Database_Module.DataBaseModule()
    # print(authenDB.get("admin"))
    # database.auth(authenDB(), authenDB.get("admin"))
    database.insert(1,data1)


    ##AI_module
    AI = AI_module.AI_module(dic["ID"],data1)
    Blood_oxygen, heartate, Systolic,Diastolic=AI.Query_Data_From_Database()
    heartrate_predict_result, oxygen_predict_result, Diastolic_predict_result, Systolic_predict_result=AI.AI_Module(Blood_oxygen,                   heartate, Systolic,Diastolic)
    Predict_Hypertension_Alert,Predict_Hypotension_Alert,Predict_Shock_Alert,Predict_Oxygen_Alert=AI.Feedback(                                          heartrate_predict_result, oxygen_predict_result, Diastolic_predict_result, Systolic_predict_result)



    ##Output
    OutputAlert_module.display_AI_iuput_data(dic["ID"], data1, Blood_oxygen, heartate, Systolic, Diastolic)

    OutputAlert_module.receive_basic_iuput_data(Signal_Loss, Shock_Alert, Oxygen_Supply, Fever, Hypotension,
                                                       Hypertension, Predict_Hypertension_Alert, Predict_Hypotension_Alert,Predict_Shock_Alert, Predict_Oxygen_Alert)



for i in range(5):
    dic = {"ID": 1, "age": 22, "gender": 'Male', "heartrate": random.randint(50, 100),
           "Diastolic_BP": random.randint(40, 110), "Systolic_BP": random.randint(70, 160),
           "blood_oxygen": random.randint(50, 100),
           "temperature": random.randint(34, 39), "time": time.ctime()}
    print("This is thread",i+1)
    thread = threading.Thread(target=main(dic))
    thread.start()
