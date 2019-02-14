import numpy as np
# from Database_Module import DataBaseModule

# Input: ID(from main function perhaps), infoDB(from Database function)
# output: Three predicted parameters, three Alert signals(Type:Boolean


class AI_module:
    def __init__(self, ID, dict):
        self._dict = dict
        self.ID = ID

    def Query_Data_From_Database(self):
        ## connect database, query previous one day data from Database
        # Database = database_dict()
        Blood_oxygen = list()
        Systolic = list()
        Diastolic = list()
        heartrate = list()
        # ID = self.ID
        # p = DataBaseModule()
        # get dictionary from database
        for key in self._dict:
            # if key== ID:
            heartate = self._dict.get("heartrate")
            oxygen = self._dict.get("blood_oxygen")
            Diastolic_BP = self._dict.get("Diastolic_BP")
            Systolic_BP = self._dict.get("Systolic_BP")
            heartrate.append(heartate)
            Blood_oxygen.append(oxygen)
            Systolic.append(Systolic_BP)
            Diastolic.append(Diastolic_BP)

        return Blood_oxygen, heartate, Systolic, Diastolic

    def AI_Module(self, Blood_oxygen, heartrate, Systolic, Diastolic):

        ## AI module do the prediction, The AI module uses previous data
        oxygen = np.array(Blood_oxygen)
        heartrate = np.array(heartrate)
        diastolic = np.array(Diastolic)
        systolic = np.array(Systolic)
        heartrate_predict_result = np.mean(heartrate)
        oxygen_predict_result = np.mean(oxygen)
        Diastolic_predict_result = np.mean(diastolic)
        Systolic_predict_result = np.mean(systolic)

        return (
            heartrate_predict_result,
            oxygen_predict_result,
            Diastolic_predict_result,
            Systolic_predict_result,
        )

    def Feedback(
        self,
        heartrate_predict_result,
        oxygen_predict_result,
        Diastolic_predict_result,
        Systolic_predict_result,
    ):

        lower_BO = 70
        lower_HR = 60
        lower_Sy = 90
        upper_Sy = 140
        lower_Di = 60
        upper_Di = 90

        Predict_Hypotension_Alert = False
        Predict_Hypertension_Alert = False

        Predict_Shock_Alert = False
        Predict_Oxygen_Alert = False
        if Systolic_predict_result > upper_Sy or Diastolic_predict_result > upper_Di:
            Predict_Hypertension_Alert = True
        if Systolic_predict_result < lower_Sy and Diastolic_predict_result < lower_Di:
            Predict_Hypotension_Alert = True
        if heartrate_predict_result < lower_HR:
            Predict_Shock_Alert = True
        if oxygen_predict_result < lower_BO:
            Predict_Oxygen_Alert = True
        ## feedback the AI prediction result to the interface
        ## It will turn on the Alert when the statues get worse.
        return (
            Predict_Hypertension_Alert,
            Predict_Hypotension_Alert,
            Predict_Shock_Alert,
            Predict_Oxygen_Alert,
        )

