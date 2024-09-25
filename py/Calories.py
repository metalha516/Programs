weight = float(input("Enter Your Weight"))
height_foot = int(input("Enter your height in foot"))
height_inch_1 = float(input("Enter your height in inch"))
age = int(input("Enter your age"))
gender = str(input("Enter your gender"))
height_inch = (height_foot*12)+height_inch_1
height_cm = height_inch * 2.54
height_meter = height_cm/100
print("Are you a \n lazy \n light \n medium \n heavy \n extra active?")
activity = str(input("Which one you are ?"))
activity = activity.lower()
def BMI(weight, height_meter):
    BMI = weight/(height_meter*height_meter)
    BMI = round(BMI,2) #to take two float value
    return BMI
def comment():
    BMI_data = BMI(weight, height_meter)
    if(BMI_data<18.5 and BMI_data>0):
       return "Underweight"
    if(18.5<BMI_data and BMI_data<24.9):
        return "normal"
    if(25<BMI_data and BMI_data<29.9):
        return "overweight"
    if(30<BMI_data and BMI_data<34.9):
       return "obese"
    if(35<BMI_data):
       return "extremely obese"
    
def BMR(gender, weight, height_cm, age):
    if(gender == "male"):
        BMR = 66.5 + (13.75*weight) + (5.003*height_cm) - (6.75*age)
        return round(BMR, 2)
    if(gender == "female"):
        BMR = 655.1 + (9.563*weight) + (1.850*height_cm) - (4.676*age)
        return round(BMR, 2)

def mc(activity):
    BMR_data = BMR(gender, weight, height_cm, age)
    if(activity == "lazy"):
        mc = BMR_data*1.2
        return round(mc, 2)
    if(activity == "light"):
        mc = BMR_data*1.375
        return round(mc, 2)
    if(activity == "medium"):
        mc = BMR_data*1.55
        return round(mc, 2)
    if(activity == "heavy"):
        mc = BMR_data*1.725
        return round(mc, 2)
    if(activity == "extra"):
        mc = BMR_data*1.9
        return round(mc, 2)
def cal_def():
    mc_data = mc(activity)
    Result = comment()
    if(Result=="normal" or Result=="Underweight"):
        return "You don't need to eat less callories"
    if(Result=="overweight"):
        rc = mc_data*0.88
        return round(rc, 2)
    if(Result=="obese"):
        rc = mc_data*0.78
        return round(rc, 2)
    if(Result=="extremely obese"):
        rc = mc_data*0.68
        return round(rc, 2)
def fat():
    mc_data = mc(activity)
    fat = mc_data*0.3
    cal = fat/9
    return round(cal, 2)
def carb():
    mc_data = mc(activity)
    fat_data = fat()
    pro_data = weight*0.8
    carb = mc_data - (fat_data + pro_data)
    return round(carb, 2)
print("BMI : ", BMI(weight, height_meter))
print("BMR : ", BMR(gender, weight, height_cm, age))
print("Maintainance Callories: ", mc(activity))
print("Defficiant Callories : ", cal_def())
print("Protein : ", weight*0.8,"g")
print("Fat :", fat(),"g")
print("Carb :", carb(),"g")
