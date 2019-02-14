from AI_module import AI_module


def receive_basic_iuput_data(
    Singal_Loss,
    Shock_Alert,
    Oxygen_Supply,
    Fever,
    Hypotension,
    Hypertension,
    Predict_Hypertension_Alert,
    Predict_Hypotension_Alert,
    Predict_Shock_Alert,
    Predict_Oxygen_Alert,
):
    ##Recevie data from input module, then analyze it using some judge functions to generate boolean result
    ##Boolean Parameters
    ##If paramter returns True, means it should be alerted, then add it to the array
    BasicResult = {
        "Signal_Loss": False,
        "Shock_Alert": False,
        "Oxygen_Supply": False,
        "Fever": False,
        "Hypotension": False,
        "Hypertension": False,
    }
    PredictResult = {
        "Predict_Hypertension_Aler": False,
        "Predict_Hypotension_Alert": False,
        "Predict_Shock_Alert": False,
        "Predict_Oxygen_Alert": False,
    }
    if Singal_Loss is True:
        BasicResult["Signal Loss"] = True
    if Shock_Alert is True:
        BasicResult["Shock_Alert"] = True
    if Oxygen_Supply is True:
        BasicResult["Oxygen_Supply"] = True
    if Fever is True:
        BasicResult["Fever"] = True
    if Hypotension is True:
        BasicResult["Hypotension"] = True
    if Hypertension is True:
        BasicResult["Hypertension"] = True
    if Predict_Shock_Alert is True:
        PredictResult["Predict_Shock_Alert"] = True
    if Predict_Oxygen_Alert is True:
        PredictResult["Predict_Oxygen_Alert"] = True
    if Predict_Hypotension_Alert is True:
        PredictResult["Predict_Hypotension_Alert"] = True
    if Predict_Hypertension_Alert is True:
        PredictResult["Predict_Hypertension_Alert"] = True
    print("Test and Predict Result:")
    print(BasicResult)
    print(PredictResult, "\n\n")

    return BasicResult, PredictResult


def display_AI_iuput_data(ID, dict, Blood_oxygen, heartrate, Systolic, Diastolic):
    ## Recevie AI data from input module, then analyze it using some judge functions to generate boolean result
    ## Paramter is boolean
    ## If paramter is True, means it should be alerted, then add it to the array
    p = AI_module(ID, dict)
    heartrate_predict_result, oxygen_predict_result, Diastolic_predict_result, Systolic_predict_result = p.AI_Module(
        Blood_oxygen, heartrate, Systolic, Diastolic
    )
    print("Heartrate Predict Result:", heartrate_predict_result)
    # print(heartrate_predict_result)
    print("Blood Oxygen Predict Result:", oxygen_predict_result)
    # print(oxygen_predict_result)
    print("Diastolic Predict Result:", Diastolic_predict_result)
    # print(Diastolic_predict_result)
    print("Systolic_predict_result:", Systolic_predict_result)
    # print(Systolic_predict_result)


