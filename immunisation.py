age_in_months=14#"At_Birth"

if age_in_months<=5:
    print("Vaccine:Polio \nInjection Site:Orally")

elif age_in_months>=6 and age_in_months<=14:
    print("Vaccine:DPT\nInjection Site:Anterolateral Thigh")

elif age_in_months>=9 and age_in_months<=12:
    print("Vaccine:Typhoid\nInjection Site:Muscle of the Thigh or The Upper Arm")

elif age_in_months>=6 and age_in_months==10 and age_in_months==14:
    print("Vaccine:PCV\nInjection Site:Anterolateral Thigh")

elif age_in_months<=6:
    print("Vaccine:HepB\nInjection Site:Upper Arm or Anterolateral Thigh")

elif age_in_months==12:
    print("Vaccine:HepA\nInjection Site:Anterolateral Thigh or Deltoild Muscle")

elif age_in_months== "At_Birth":
    print("Vaccine: (a) BCG\n(b) HepB\n(c) OPV\n(d) Polio ")

else:
    print("INVALID AGE")