regions = {
    "midwest": ["ND","SD","NB","KS", "MN","MO","IA","WI","IS","IN","MI", "OH"],
    "rockies": ["MO","ID","WY","NV","UT","CO"],
    "southwest": ["AZ","NM","TX","OK"],
    "pacific": ["WA","OR","CA"],
    "southeast": ["AK","LA","MS","AL","GA","SC","NC","VA","WV","KY","TN","FL","DE","MD"],
    "northeast": ["PA","NY","NJ","CT","RI","MA","VT","NH","ME", "DC","D.C."]
}

import csv
import pandas as pd
import us


students = pd.read_csv("analyzed.csv")
print(students)


cols = list(students.columns.values)
cols.insert(4,'region')

with open("regionsorted.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(cols)
    for elem in students.iterrows():
        # print(elem)
        region = "UNKNOWN"
        for r, states in regions.items():
            if elem[1].state in states:
                print("FOUND", r)
                region = r
                continue
            for state in states:
                if state != "GA":
                    try:
                        fullName = us.states.lookup(state).name.lower()
                    except:
                        fullName = "NOTASTATE"
                    post = elem[1].post
                    if state in post or fullName in post:
                        elem[1].state = state
                        region = r

        newelem = list(elem[1].to_numpy())
        newelem.insert(4,region)
        writer.writerow(newelem)
