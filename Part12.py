import pandas as pd

# initial dataframe
DF = pd.read_csv('/Users/avvaichandrasekaran/CollegeCoding/CSC1302/Project/titles.csv', nrows = 100)

#----DATA FRAMES-----#

# INITIAL DATA FRAME
columns = ["title", "type", "release_year", "age_certification", "runtime", "seasons"]
ogDF : pd.DataFrame = pd.DataFrame(DF, columns=columns)
print (" " * 40 + " ---- INITIAL DATA FRAME ----" )
print(ogDF)

# AGE RATING DATA FRAME
print(" " * 8)
print(" " * 40 + " ---- AGE RATING DATA FRAME ---- ")
ageDF : pd.DataFrame = ogDF.dropna(subset = ['age_certification'])
print(ageDF)

# TV SHOWS ONLY DATA FRAME
print(" " * 8)
print(" " * 40 + " ---- TV SHOW RATING DATA FRAME ---- ")
tvDF = ageDF.query("type == 'SHOW'")
print(tvDF)

#----STATISTICS----#

print(" " * 10)
print(" " * 40 + "---- ALL STATISTICS ----")

print (" ")
print("MEAN")
mean = ageDF.groupby("type").mean(numeric_only = True)
print(mean)

print (" ")
print("MEDIAN")
median = ageDF.groupby("type").median(numeric_only = True)
print(median)

print (" ")
print("VARIANCE")
variance = ageDF.groupby("type").var(numeric_only = True)
print(variance)

print (" ")
print("STANDARD DEV")
stdDev = ageDF.groupby("type").std(numeric_only = True)
print(stdDev)

