# hw2_1
* file: ./hw2_1.png
this is the proof of Kaggle competition.
And choosing 5 important_features = ["Neighborhood", "GrLivArea", "OverallQual", "TotalBsmtSF", "GarageArea"] 
The result with all features is actually slightly higher than choose 5 features.

mse: 927635072.0000, with all features.
mse: 899382592.0000, with 5 featuers.

# hw2_2
* file: ./HW2_bike-sharing_test_sol.csv
* code: ./hw2_2.ipynb

# hw2_3
* file: ./HW2_hr-analytics_test_sol.csv
* code: ./hw2_3.ipynb
* confusion matrix: ./hw2_3_confusion_matrix.png
With feature_importance, we can know the top 5 related feature:
1. satisfaction_level: 0.5147
2. time_spend_company: 0.1253
3. last_evaluation: 0.1166
4. average_montly_hours: 0.1131
5. number_project: 0.1048

We can know the satisfaction_level is the most important feature to determine whether a employee stay or left.
And as the format of average_monthly_hours is not regularized, I implemented a data transform turing them to values between -1 and 1.
The Performance do enhance from 0.956 val acc to 0.957 val acc, which is great.

# hw2_4
* file: ./hw2_4_AI_competition.png
組長：陳昱逢
參加項目：永豐AI GO競賽-攻房戰
