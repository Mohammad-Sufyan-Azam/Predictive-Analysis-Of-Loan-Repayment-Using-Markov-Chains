import random
import csv
import pandas as pd

gd_gd = 470
gd_hr = 100
gd_lr = 160
gd_bl = 10
gd_paid = 260
hr_gd = 200
hr_hr = 320
hr_lr = 200
hr_bl = 220
hr_paid = 60
lr_gd = 300
lr_hr = 200
lr_lr = 380
lr_bl = 50
lr_paid = 70
id = 1
data = {"Customer_ID" : [],"Credit_Score" : [],"Borrow Loan Type" : [],"Loan Type After 1 year" : []}
while True:
    change = False
    if gd_gd > 0:
        change = True
        data["Customer_ID"].append(id)
        id += 1
        data["Credit_Score"].append(random.randint(61,80))
        data["Borrow Loan Type"].append("Good Loan")
        data["Loan Type After 1 year"].append("Good Loan")
        gd_gd -= 1
    if gd_hr > 0:
        change = True
        data["Customer_ID"].append(id)
        id += 1
        data["Credit_Score"].append(random.randint(21, 40))
        data["Borrow Loan Type"].append("Good Loan")
        data["Loan Type After 1 year"].append("High Risk Loan")
        gd_hr -= 1
    if gd_lr > 0:
        change = True
        data["Customer_ID"].append(id)
        id += 1
        data["Credit_Score"].append(random.randint(41, 60))
        data["Borrow Loan Type"].append("Good Loan")
        data["Loan Type After 1 year"].append("Low Risk Loan")
        gd_lr -= 1
    if gd_bl > 0:
        change = True
        data["Customer_ID"].append(id)
        id += 1
        data["Credit_Score"].append(random.randint(5, 20))
        data["Borrow Loan Type"].append("Good Loan")
        data["Loan Type After 1 year"].append("Bad Loan")
        gd_bl -= 1
    if gd_paid > 0:
        change = True
        data["Customer_ID"].append(id)
        id += 1
        data["Credit_Score"].append(random.randint(81, 95))
        data["Borrow Loan Type"].append("Good Loan")
        data["Loan Type After 1 year"].append("Paid")
        gd_paid -= 1
    if hr_gd > 0:
        change = True
        data["Customer_ID"].append(id)
        id += 1
        data["Credit_Score"].append(random.randint(61,80))
        data["Borrow Loan Type"].append("High Risk Loan")
        data["Loan Type After 1 year"].append("Good Loan")
        hr_gd -= 1
    if hr_hr > 0:
        change = True
        data["Customer_ID"].append(id)
        id += 1
        data["Credit_Score"].append(random.randint(21, 40))
        data["Borrow Loan Type"].append("High Risk Loan")
        data["Loan Type After 1 year"].append("High Risk Loan")
        hr_hr -= 1
    if hr_lr > 0:
        change = True
        data["Customer_ID"].append(id)
        id += 1
        data["Credit_Score"].append(random.randint(41, 60))
        data["Borrow Loan Type"].append("High Risk Loan")
        data["Loan Type After 1 year"].append("Low Risk Loan")
        hr_lr -= 1
    if hr_bl > 0:
        change = True
        data["Customer_ID"].append(id)
        id += 1
        data["Credit_Score"].append(random.randint(5, 20))
        data["Borrow Loan Type"].append("High Risk Loan")
        data["Loan Type After 1 year"].append("Bad Loan")
        hr_bl -= 1
    if hr_paid > 0:
        change = True
        data["Customer_ID"].append(id)
        id += 1
        data["Credit_Score"].append(random.randint(81, 95))
        data["Borrow Loan Type"].append("High Risk Loan")
        data["Loan Type After 1 year"].append("Paid")
        hr_paid -= 1
    if lr_gd > 0:
        change = True
        data["Customer_ID"].append(id)
        id += 1
        data["Credit_Score"].append(random.randint(61,80))
        data["Borrow Loan Type"].append("Low Risk Loan")
        data["Loan Type After 1 year"].append("Good Loan")
        lr_gd -= 1
    if lr_hr > 0:
        change = True
        data["Customer_ID"].append(id)
        id += 1
        data["Credit_Score"].append(random.randint(21, 40))
        data["Borrow Loan Type"].append("Low Risk Loan")
        data["Loan Type After 1 year"].append("High Risk Loan")
        lr_hr -= 1
    if lr_lr > 0:
        change = True
        data["Customer_ID"].append(id)
        id += 1
        data["Credit_Score"].append(random.randint(41, 60))
        data["Borrow Loan Type"].append("Low Risk Loan")
        data["Loan Type After 1 year"].append("Low Risk Loan")
        lr_lr -= 1
    if lr_bl > 0:
        change = True
        data["Customer_ID"].append(id)
        id += 1
        data["Credit_Score"].append(random.randint(5, 20))
        data["Borrow Loan Type"].append("Low Risk Loan")
        data["Loan Type After 1 year"].append("Bad Loan")
        lr_bl -= 1
    if lr_paid > 0:
        change = True
        data["Customer_ID"].append(id)
        id += 1
        data["Credit_Score"].append(random.randint(81, 95))
        data["Borrow Loan Type"].append("Low Risk Loan")
        data["Loan Type After 1 year"].append("Paid")
        lr_paid -= 1

    if not change:
        break

dataframe = pd.DataFrame(data)
dataframe.to_csv("Data_SPA.csv",index = False)

