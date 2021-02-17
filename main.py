import csv
import json
import requests
# https://weblate.lolc.at/exports/stats/uchuujin/script-0003/?format=json

translated_percent_dict = []
translated_words_dict = []

for i in range(224):
    #for i in range(5): #testing range
    currentScript = str(i).zfill(4)

    dataURL = "https://weblate.lolc.at/exports/stats/uchuujin/script-" + \
        currentScript + "/?format=json"
    print("------")
    print(dataURL)
    print("")

    jsonData = json.loads(requests.get(dataURL).text)
    #print(type(jsonData))
    print("JSON data for " + currentScript + ": ")
    print(jsonData)

    translated_percent = str(jsonData[0]['translated_percent'])
    translated_words = str(jsonData[0]['translated_words'])

    print("")
    print("Script number: " + currentScript)
    print("Translated Percentage: " + translated_percent)
    print("Translated Words: " + translated_words)

    print("------")
    print("")
    print("")

    # add values to new dictionary
    translated_percent_dict.append(translated_percent)
    translated_words_dict.append(translated_words)

# write file
with open('NichiStats.csv', 'w') as writeFile:
    writer = csv.writer(writeFile, delimiter=',',
                        quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for i in range(len(translated_percent_dict)):
        print("Writing: ",
              translated_percent_dict[i], translated_words_dict[i])
        writer.writerow([translated_percent_dict[i], translated_words_dict[i]])
writeFile.close()