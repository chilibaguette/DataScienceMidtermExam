import csv

with open('allowance.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    row_list = [
        ["name", "weekly allowance"],
        ["Erika Em Sonja Sagario", "500.00"],
        ["Nicole C. Sandoval", "600"],
        ["Allain Rico Muaña", "500"],
        ["Rian Dave Brignas", "500"],
        ["Erika Gabrielle Samson", "500"],
        ["Jan David S. Capuyan", "420"],
        ["Kyle R. Peralta", "500"],
        ["Christian Paulo A. Dagupan", "500"],
        ["Shin Aro", "500"],
        ["Kiana Rae M. Cirilo", "500"],
        ["Imee G. Camba", "600"],
        ["Jamaica Jumuad", "500"],
        ["Kriss Ann S. Dungog", "500"],
        ["Ingrid Maria Sofia Gacayan", "500"],
        ["Gabriel Limbaga", "600"],
        ["Jomary P. Jalang", "4500"],
        ["Dante T. Lucion", "250"],
        ["Jake Bradley Roxas", "150"],
        ["Ayn Lorebelle Cavan", "600"],
        ["Eduard Philippe Tojong", "500"],
        ["Argie Matondo", "500"],
        ["Emilio", "500"],
        ["Princess Abegeal Alegre", "500"],
        ["Joy M. Tag-at", "250"],
        ["Brad Anthony Vann F. Sarra", "500"],
        ["Ralph Laurence Ambrad", "500"],
        ["Evongelio Raden", "500"],
        ["Eric Angelo Devera", "200"],
        ["Renante L. Taac-taac", "500"],
        ["Uriel Joseph L. Garza", "500"],
        ["Roan Jumawan", "900"],
        ["Jhermaine Rob Landeza", "250"],
        ["RJ Alenton", "500"],
        ["Aberoja Kiert Michael", "500"],
        ["Kristoffer Layos", "500"],
        ["Jerome Ayong", "800"],
        ["Jhon Axell Señagan", "1000"],
        ["Lance S. Monsanto", "800"],
        ["Mhey Ryan B. Fernandez", "100"],
        ["Stephen Jon De los Santos", "1000"],
        ["Angelica Eve. A. Angel", "500"],
        ["Sheilmae Jean B. Furog", "800"],
        ["Via M. Gelig", "500"],
        ["Miranda Lois Arriola", "500"],
        ["Joemar M. Ygot", "500"],
        ["John Colleen C. Saberon", "100"],
        ["John Henry T. Tero", "800"],
        ["Lloyd Christopher P. Singcol", "1000"],
        ["Jil-Sharney Camandona", "7500"],
        ["Stephen Hans Amistoso", "2000"],
    ]

    writer.writerow(row_list)
