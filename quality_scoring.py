import pandas as pd


df = pd.read_csv("titanic.csv")
print(df.head())

# วิธีการเรียกดูค่าใน Column
# df["Survived"]
# df.Survived

df.info()

age_not_null = df.Age.notnull()
dq_age = age_not_null.sum() / len(age_not_null)
print(f"Data Quality of Age: {dq_age}")

cabin_not_null = df.Cabin.notnull()
dq_cabin = cabin_not_null.sum() / len(cabin_not_null)
print(f"Data Quality of Cabin: {dq_cabin}")

embarked_not_null = df.Embarked.notnull()
dq_embarked = embarked_not_null.sum() / len(embarked_not_null)
print(f"Data Quality of Embarked: {dq_embarked}")
#--------------------------------------------------------------------------------
passenger_id_not_null = df.PassengerId.notnull()
dq_passenger = passenger_id_not_null.sum() / len(passenger_id_not_null)
print(f"Data Quality of passenger: {dq_passenger}")

survived_not_null = df.Survived.notnull()
dq_survived = survived_not_null.sum() / len(survived_not_null)
print(f"Data Quality of survied: {dq_survived}")

pclass_not_null = df.Pclass.notnull()
dq_pclass = pclass_not_null.sum() / len(pclass_not_null)
print(f"Data Quality of pclass: {dq_pclass}")

name_not_null = df.Name.notnull()
dq_name = name_not_null.sum() / len(name_not_null)
print(f"Data Quality of name: {dq_name}")

sex_not_null = df.Sex.notnull()
dq_sex = sex_not_null.sum() / len(sex_not_null)
print(f"Data Quality of sex: {dq_sex}")

sibsp_not_null = df.SibSp.notnull()
dq_sibsp = sibsp_not_null.sum() / len(sibsp_not_null)
print(f"Data Quality of SibSp: {dq_sibsp}")

parch_not_null = df.Parch.notnull()
dq_parch = parch_not_null.sum() / len(parch_not_null)
print(f"Data Quality of Parch: {dq_parch}")

ticket_not_null = df.Ticket.notnull()
dq_ticket = ticket_not_null.sum() / len(ticket_not_null)
print(f"Data Quality of Ticket: {dq_ticket}")

fare_not_null = df.Fare.notnull()
dq_fare = fare_not_null.sum() / len(fare_not_null)
print(f"Data Quality of Ticket: {dq_fare}")

print(f"Completeness: {(dq_age + dq_cabin + dq_embarked + dq_passenger + dq_survived + dq_pclass + dq_name + dq_sex + dq_parch + dq_ticket + dq_fare) / 11}")