__author__ = "Kaushal Rijal"

    
    #Project created to easily create a "maag faaram" and avoid using calculator.
    #Prleiminiary ideas:
    #1) Automatically do all calculations after taking "talab scale"
    #2) Create a GUI(depends upon mood)
    #3) Use pandas and export the data to a CSV file.

#Functions
from distutils.log import error
from tokenize import Double


def grade_amt(talab, grade):
    if type(grade and talab) == float:
        return (talab/30)*grade
    return "Invalid Value Entered!"

def sanchaya_kosh_thap(talab, grade):
    if type(grade and talab) == float:
        return (talab+grade)/10
    return "Invalid Value Entered!"

def jamma_talab(talab, grade, sanchaya_kosh, bima):
    if type(talab and grade and sanchaya_kosh and bima) != str:
        return talab + grade + sanchaya_kosh + bima
    return "Invalid Value Entered!"


def one_month(jamma, bhatta, headmaster):
    if type(jamma and bhatta) != str and type(headmaster) == bool:
        if headmaster == True:
            return jamma + bhatta + 300
        return float(jamma) + bhatta
    return "Invalid Value Entered!"

def kul_jamma(tin_mahina, anya):
    if type(tin_mahina) != str and type(anya) == bool:
        if anya ==  True:
            if is_sthaayi == True:
                return tin_mahina + (sanchaya_kosh_amount*10)
            else:
                return tin_mahina + float(talab_scale)
        return tin_mahina
    return "Invalid Value Entered!"

#Inputs from user
talab_scale = input("Please enter the talab scale: ")
is_sthaayi = input("Are you sthaayi?(yes/no): ")

if is_sthaayi.strip().lower() == "yes":
    grade = input("Please enter your grade: ")
    is_sthaayi = True
else:
    is_sthaayi = False

is_pra_a = input("Are you the headmaster?(yes/no): ")
dashain_kharcha = input("Are you getting dashain kharcha or such things?(yes/no): ")

#Specific Conditions for bhattas
if is_pra_a.lower() == "yes":
    is_pra_a = True
else:
    is_pra_a = False

if dashain_kharcha.lower() == "yes":
    dashain_kharcha = True
else:
    dashain_kharcha = False

#Variables
if is_sthaayi:
    grade_amount = grade_amt(float(talab_scale), float(grade))
    sanchaya_kosh_amount = sanchaya_kosh_thap(float(talab_scale), float(grade_amount))
    jamma_talab_amount = jamma_talab(float(talab_scale), grade_amount, sanchaya_kosh_amount, 400)
    bimaa_thap = 400
else:
    grade_amount = "-"
    sanchaya_kosh_amount = "-"
    jamma_talab_amount = talab_scale
    bimaa_thap = "-"

one_month_amount = one_month(jamma_talab_amount, 2000, is_pra_a)
three_month_amount = one_month_amount * 3
kul_jamma_amount = kul_jamma(three_month_amount, dashain_kharcha)

#Output
print("\nGrade Amt.:", grade_amount,
    "\nSanchaya Kosh Thap:", sanchaya_kosh_amount,
    "\nBimaa Thap:", bimaa_thap,
    "\nJamma Talab:", jamma_talab_amount,
    "\n1 Mahinako Talab:", one_month_amount,
    "\n3 Mahinko Talab:", three_month_amount,
    "\nKul Jamma:", kul_jamma_amount)

input("\n\nPress enter key to exit!")