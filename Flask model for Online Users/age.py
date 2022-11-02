import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from dtreeviz.trees import *

class LarvaeAge:

    def fetching_data(self):
        df = pd.read_excel('/Users/mohitjain/Desktop/Msc Project on Machine Learning/Flask model for Online Users/Dataset.xlsx')

        #allocating the temprature according to the number in dataset
        df['Temperature'] = df['Temperature'].replace(1,25) 
        df['Temperature'] = df['Temperature'].replace(2,20)
        df['Temperature'] = df['Temperature'].replace(3,15)

        return df

    def decideTemp(self, temperature):
        full_df = self.fetching_data()
        full_df = full_df.loc[full_df['Temperature']==temperature]
        return full_df

    def splitTrainingdata(self, temperature):
        df = self.decideTemp(temperature)
        x = df.drop(["Hours","ID","Series","Run","Cup","Batch","Temperature"], axis=1).values
        y = df["Hours"]

        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=100)

        
        return [x_train,x_test,y_train,y_test]

    def age_prediction(self, length, weight, larvelStage, temperature):
        training_list = self.splitTrainingdata(temperature)
        regressor = DecisionTreeRegressor(criterion="squared_error")
        regressor.fit(training_list[0], training_list[2])
        value = [[length, weight, larvelStage]]
        return regressor.predict(value)[0]
    
    def path_view(self, length, weight, larvelStage, temperature):
        training_list = self.splitTrainingdata(temperature)
        regressor = DecisionTreeRegressor(criterion="squared_error")
        regressor.fit(training_list[0], training_list[2])
        viz = dtreeviz(regressor,
                training_list[0],
                training_list[2],
                target_name="Hours",
                orientation='LR',
                feature_names= ["Length", "Weight", "Larvalstage"],
                X=[length, weight, larvelStage],
                show_just_path=True,
                colors={'highlight': 'RED'})

        viz.save(f"/Users/mohitjain/Desktop/Msc Project on Machine Learning/Flask model for Online Users/static/uploaded_viz/path_view{length}-{weight}-{larvelStage}-{temperature}.svg")

    def tree_view(self, length, weight, larvelStage, temperature):
        training_list = self.splitTrainingdata(temperature)
        regressor = DecisionTreeRegressor(criterion="squared_error")
        regressor.fit(training_list[0], training_list[2])
        viz = dtreeviz(regressor,
                training_list[0],
                training_list[2],
                target_name="Hours",
                orientation='TD',
                feature_names= ["Length", "Weight", "Larvalstage"],
                X=[length, weight, larvelStage],
                colors={'highlight': 'RED'})

        viz.save(f"/Users/mohitjain/Desktop/Msc Project on Machine Learning/Flask model for Online Users/static/uploaded_viz/tree_view{length}-{weight}-{larvelStage}-{temperature}.svg")