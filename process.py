"""
 From the given dataset, extract the input data(feature) that is most suitable for training
 and the corresponding result(label) column
 
 These two columns are simply written in new file with little processing
 Initial data is still untouched
 
 The features that are used at application level and that convey less meaning are neglected
"""

import pandas as pd
import ast, csv, json, re

# variables to store the feature and label
data_list =[]
label_list = []

dataset = pd.read_csv("NLP.csv")
for data,label in zip(dataset["data"],dataset["label"]):
    # encode the data in ascii to avoid confusing character(like smileys/camera etc..) introduced in Unicode
    # decode that back to restore the string representation
    # if the data or label is empty, it is of no use. Hence, remove them too
    # Further, strip the data. Whitespaces does not mean much
    formatted_data = ast.literal_eval(data)["data"].encode('ascii', 'ignore').decode('utf-8')
    if(formatted_data.strip() != "" and label.strip() != ""):
        data_list.append(formatted_data)
        label_list.append(label)

# Write those varibales(that undergone little formatting) into a CSV file
with open('reqColsFile.csv', 'w', newline='') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL,delimiter=',')
    wr.writerow(["text","label"])
    wr.writerows(zip(data_list, label_list))


"""
 As most of the common data are classified imperfect, use regex operations to actually (clean)convey proper 
 meaning for training purposes.
 
 The CSV file extracted from the previous stage is used for cleaning purposes.
 The cleaned data is written in another CSV file for further processing
"""

reqColsFile = pd.read_csv("reqColsFile.csv")

#hi, hello, good morning, whereWhich, thank you, okayOK, sorRy

for index, colRow in reqColsFile.iterrows():
    # The string representation is stored in a variable to avoid processing colRow frequently
    # especially in OR conditions that are involved
    colRowText = str(colRow["text"])
    
    if re.match("[\s]*ha*[i]+", colRowText, re.I) or re.match("^[\s]*h.e*[l]+o+", colRowText, re.I):
        colRow["label"] = "greeting"
        
    elif re.match("[\s]*g[oud\s]*m[orning]*", colRowText, re.I):# [\s]*go*u*d\s*m[orning]*
        colRow["label"] = "greeting"
        
    elif(re.match("[\s]*t[qhanks\syou]+", colRowText, re.I)):
        colRow["label"] = "greeting"
        
    elif(re.match("[\s]*wh[ere]+", colRowText, re.I) or re.match("[\s]*wr\\b", colRowText, re.I)):
        colRow["label"] = "location"
        
    elif(re.match("[\s]*s[or]*ry", colRowText, re.I)):
        colRow["label"] = "dontMeetRequirements"

    elif(re.match("[\s]*o[kieay]+", colRowText, re.I) or re.match("[\s]*k\\b", colRowText, re.I)):
        colRow["label"] = "greeting"

# The result is written into a CSV, though handling differs from the previous stage
reqColsFile.to_csv("intentClassifiedFile.csv", sep=',', encoding='utf-8', index=False)


"""
 The rasa_nlu classifier accepts training data in either json format or in the markdown format
 With the available data, json is easy to be constructed
 
 Hence, with the pre-processed data, json file is generated as required
"""

csvfile = open('intentClassifiedFile.csv', 'r')

common_examples = []

fieldnames = ("text","intent")
reader = csv.DictReader(csvfile, fieldnames)

for row in reader:
    common_examples.append(row)
    
del common_examples[0] # remove header row

# construct the required json structure
rasa_nlu_data = {"common_examples" : common_examples}
json_data = {"rasa_nlu_data" : rasa_nlu_data}

# The result file that will be fed into rasa for training
with open('intentClassifiedFile.json', 'w') as fp:
    json.dump(json_data, fp)