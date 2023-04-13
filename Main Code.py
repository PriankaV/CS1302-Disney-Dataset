import pandas as pd

DF = pd.read_csv('/Users/avvaichandrasekaran/CollegeCoding/CSC1302/Project/titles.csv')

#----DATA FRAMES-----#

# INITIAL DATA FRAME
columns = ["title", "type", "release_year", "age_certification", "runtime", "seasons", "imdb_score"] 
ogDF : pd.DataFrame = pd.DataFrame(DF, columns=columns)

# AGE RATING DATA FRAME
ageDF : pd.DataFrame = ogDF.dropna(subset = ['age_certification'])

# TV SHOWS ONLY DATA FRAME
tvDF = ageDF.query("type == 'SHOW'")


#----STATISTICS----#

mean = ageDF.groupby("type").mean(numeric_only = True)
median = ageDF.groupby("type").median(numeric_only = True)
variance = ageDF.groupby("type").var(numeric_only = True)
stdDev = ageDF.groupby("type").std(numeric_only = True)


if __name__ == "__main__":
    print (" " * 40 + " ---- INITIAL DATA FRAME ----" )
    print(ogDF)

    print(" " * 8)
    print(" " * 40 + " ---- AGE RATING DATA FRAME ---- ")
    print(ageDF)

    print(" " * 8)
    print(" " * 40 + " ---- TV SHOW RATING DATA FRAME ---- ")
    print(tvDF)

    print(" " * 10)
    print(" " * 40 + "---- ALL STATISTICS ----")

    print (" ")
    print("MEAN")
    print(mean)

    print (" ")
    print("MEDIAN")
    print(median)

    print (" ")
    print("VARIANCE")
    print(variance)

    print (" ")
    print("STANDARD DEV")
    print(stdDev)
