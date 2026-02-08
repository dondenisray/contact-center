import pandas as pd 

from sqlalchemy import create_engine

print ("PYTHON Y PANDAS LISTOS")


###cadena de conexión a SQL Server (local)
connection_string = (
    "mssql+pyodbc://@localhost\\SQLEXPRESS/ContactCenterBI"
    "?driver=ODBC+Driver+17+for+SQL+Server"
)

##creamos la conexión
engine = create_engine(connection_string)


# Leemos la tabla Calls desde SQL
query = "SELECT * FROM Calls"
df = pd.read_sql(query, engine)

print (df)

### ver estrucutura del dataset

print( "\n INFO DEL DATA SET")
 
print (df.info())

## total calls

total_calls = len(df)

print ("\n total calls", total_calls)

## total calls per day

calls_per_day = df.groupby("call_date").size()

print("\ntotal calls per day", total_calls)


# answered calls 
answered_calls = df[df["answered"] == 1]
print("\nanswered calls")
print(len(answered_calls))

###answered rate 

answer_rate = len(answered_calls ) / len(df)

print (" \nanswered rate", answer_rate) 


#invalid durations

invalid_duration = df[df["duration_seconds"]<= 0]

print ("\n invalids durations", invalid_duration)

### avg duration 

valid_duration = df[df["duration_seconds"]> 0]

average_duration = valid_duration["duration_seconds"].mean

print ("\nAVG Duration ", average_duration)

