import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import joblib
from sklearn.linear_model import LogisticRegression

iris_data = pd.read_csv('data/iris.csv')
le = LabelEncoder()
print(le.fit(iris_data['species']))
iris_data['species'] = le.fit_transform(iris_data['species'])
print(le.classes_) # [setosa ~]

iris_data_columns = iris_data.drop(columns=['species'])
iris_data_species = iris_data['species']

# 데이터 셋 분리
train_input, test_input, train_target, test_target = train_test_split(
    iris_data_columns, iris_data_species, test_size=0.25
)

# 모델 만들기
model = LogisticRegression()
model.fit(train_input, train_target)

# 모델 내보내기(배포)
model_file = open('models/logistic_regression_model_iris_221208.pkl', 'wb')
joblib.dump(model, model_file)
model_file.close()