import pandas as pd

 
cricketers = pd.read_csv("people.csv")
print(cricketers)


names = cricketers["Name"]
print(names)

data_dict = {
    'Name': ['John', 'Mary', 'David', 'Emily', 'Michael'],
    'Age': [25, 31, 42, 28, 35],
    'Country': ['USA', 'UK', 'Australia', 'Canada', 'France'],
    'Score': [90, 80, 95, 78, 92]
}

df = pd.DataFrame(data_dict)
print(df)
# data frame from a 9x9 2d array with specific rows and columns from a dictionary

names_2d = [
    ["Robert Wadlow", "Tallest man ever", "272 cm (8 ft 11.1 in)"],
    ["Jyoti Amge", "Shortest woman alive", "62.8 cm (2 ft 0.7 in)"],
    ["Ashrita Furman", "Most records held", "600+"],
    ["Lee Redmond", "Longest fingernails ever (female)", "8.65 m (28 ft 4.5 in)"],
    ["Chandra Bahadur Dangi", "Shortest man ever", "54.6 cm (1 ft 9.5 in)"],
    ["Sultan Kösen", "Tallest living man", "251 cm (8 ft 2.8 in)"],
    ["Pauline Musters", "Shortest woman ever", "30 cm (1 ft 0 in)"],
    ["Bao Xishun", "Tallest man ever (living)", "236 cm (7 ft 8.9 in)"],
    ["He Pingping", "Shortest man ever (living)", "74 cm (2 ft 5 in)"],
    ["Sultan Kösen", "Largest hands ever", "27.5 cm (10.8 in)"]
]
df1 = pd.DataFrame(names_2d, columns=["Name", "Achievement", "Record"])
print(df1)


names = [
    "John Doe",
    "Jane Smith",
    "Ahmed Ali",
    "Maria Rodriguez",
    "David Kim",
    "Emily Chen",
    "Michael Brown",
    "Sofia Garcia",
    "James Johnson",
    "Liam Williams",
    "Olivia Taylor",
    "William Jones",
    "Ella Wilson",
    "Harper Harris",
    "Ava Martinez",
    "Daniel White",
    "Sophia Clark",
    "Ethan Thompson",
    "Madison Walker",
    "Benjamin Wright"
]

countries = [
    "USA",
    "UK",
    "Pakistan",
    "Mexico",
    "South Korea",
    "China",
    "USA",
    "Spain",
    "USA",
    "UK",
    "USA",
    "UK",
    "USA",
    "USA",
    "USA",
    "USA",
    "USA",
    "USA",
    "USA",
    "USA"
]
series = pd.Series(data=countries,index=names)
print(series)
print(type(series))

#AAcessing 

print(series.index)
print(series.ndim)
print(series.shape)
print(series.size)

#using ind3ex to access a series
# series[] and loc uses index
print(series["Benjamin Wright"])  
print(series["Daniel White"])  
print(series["Daniel White":"Benjamin Wright"])

print(series.loc["Benjamin Wright"])  
print(series.loc["Daniel White"])  
print(series.loc["Daniel White":"Benjamin Wright"])

print(series.iloc[1])  
print(series.iloc[3])  
print(series.iloc[3:8])



print(series.iloc[-1])


v = pd.Series(data = 186)
print(v)


v1 = pd.Series(dtype=int)
print(v1)

batsmen = pd.Series([
    "Sachin Tendulkar",
    "Ricky Ponting",
    "Brian Lara",
    "Jacques Kallis",
    "Rahul Dravid",
    "Kumar Sangakkara",
    "Mahela Jayawardene",
    "AB de Villiers",
    "Hashim Amla",
    "Virat Kohli",
    "Steve Smith",
    "Kane Williamson",
    "Joe Root",
    "David Warner",
    "Ross Taylor",
    "Alastair Cook",
    "Michael Clarke",
    "Younis Khan",
    "Inzamam-ul-Haq",
    "Virender Sehwag"
])

bowlers = pd.Series([
    "Muttiah Muralitharan",
    "Shane Warne",
    "Anil Kumble",
    "Glenn McGrath",
    "Wasim Akram",
    "Waqar Younis",
    "Curtly Ambrose",
    "Malcolm Marshall",
    "Richard Hadlee",
    "Kapil Dev",
    "Shaun Pollock",
    "Chaminda Vaas",
    "Courtney Walsh",
    "Allan Donald",
    "Dale Steyn",
    "James Anderson",
    "Stuart Broad",
    "Rangana Herath",
    "Mitchell Johnson",
    "Zaheer Khan"
])

result = batsmen + bowlers
print(result)

# with different index

s1 = pd.Series([11, 22, 3,4,5,9], index=[0,1,2,3,4,5])
s2 = pd.Series([4, 55, 66, 7,88,9], index=[0,3,4,5,6,7])
s3 = s1 + s2

print(s1)
print(s2)
print(s3)

# now using .add for addition
print(s1.add(s2, fill_value=0.0))

print(s1.add(s2, fill_value=10.0))
