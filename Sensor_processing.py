import random
import datetime
import ast


def dummydataSet():
    """" This is a function for problem 1

        *The order of the objects must be sequential, ( ie. 1,2,3...32. ) since each number references a different pipeline region
        *Your generated dataset needs to return a single set of data, that has 32 entries, with each entry returning 16 floats.
        *The 16 floats returned will be between 0 and 1

    """

    No_of_clusters = 32  # Number of clusters
    Sensors_in_cluster: int = 16  # Number of sensors in each cluster

    dataset = []  # create and empty list

    for x in range(0, No_of_clusters):
        dataset.append([])  # Create 32 number of cluster lists

    for y in range(0, No_of_clusters):  # For each cluster from 1 to 32
        for z in range(0, Sensors_in_cluster):  # fill 16 random sensor readings
            dataset[y].append(z)
            dataset[y][z] = random.uniform(0, 1)  # generate random sensor readings between 0 and 1
            dataset[y][z] = round((dataset[y][z]), 5)  # round each value to 3 decimal places

    for k in range (0, No_of_clusters): #insert date and time
        dataset[k].insert(0, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    return dataset

def StoreDataInTextFile(myData):
    """" This is a function for problem 2

        *Every time your data set is generated the output should be stored and saved
            - For a challenge you could try to write the data to a file
        *New data should not overwrite historical data
        *For an extra challenge you can try to date and time stamp each interval of data collection
    """

    with open("Collected_Data.txt", "a") as f:
        TempData = str(myData)
        myList = TempData.split("]")        #Split the list using ']'

        for i in range(0,len(myData)):
            print("Cluster {}".format(i+1), end=" ")
            print(myList[i])
            f.write("Cluster {}".format(i+1))
            f.write("%s\n" % myList[i])         #write data with errors to file

    loggedData = myData

    return loggedData

def GenerateErrData(SimulatedData, SensorErrorText="err"):
    """" This is a function for problem 3

        *Create a copy of a "corrupted" data set containing at least one entry where the value is "err"
        *Your function should check for this error
        *Convert the string to a numerical value that can be uniquely identified as the error
        *Create an error log that records that the error happened and which of the sensors the error occurred with
    """
    No_of_clusters = 33
    No_of_sensors = 16

    RandomClusterWithError = random.randint(1, No_of_clusters)  # generate a random interger between 0 and 31 [32 clusters]
    RandomSensorWithError = int(round(len(SimulatedData[0]) * (random.random())))  # convert string to an integer number

    if RandomClusterWithError > 1:  # If there is a cluster with an error
        index1 = 0
        while index1 < RandomClusterWithError:  # For all clusters with errors
            if RandomClusterWithError > 1:  # if there is an error in cluster with unique error value - valid data range is 0-1
                index2 = 0
                while index2 < RandomClusterWithError:
                    ErrorCluster = int(round(len(SimulatedData) * (random.random())))
                    ErrorSensor = int(round(len(SimulatedData[0]) * (random.random())))

                    if ErrorCluster < len(SimulatedData):
                        if ErrorSensor < len(SimulatedData[0]):
                            tempdata = SimulatedData[ErrorCluster]
                            tempdata[ErrorSensor] = str(SensorErrorText)  # introduce an error in  random sensor
                        else:
                            pass
                    else:
                        pass

                    index2 = index2 + 4  # move to next sensor
            else:
                pass
            index1 = index1 + 4  # move to next cluster

    else:
        pass  # if there is no error in cluster do nothing

    return SimulatedData

def ConvErrorToNumber(DataWithErrors, SensorErrorText="err", UniqueErrorValue=2):  # function to convert Errors to numerical values
    index1 = 0
    while index1 < len(DataWithErrors):
        index2 = 0
        while index2 < len(DataWithErrors[index1]):
            if DataWithErrors[index1][index2] == SensorErrorText:  # if data is text with "err"
                DataWithErrors[index1][index2] = UniqueErrorValue  # Replace with a error value
            else:
                pass
            index2 = index2 + 1
        index1 = index1 + 1

    return DataWithErrors

def logfileWithErrors(errorData, UniqueErrValue=2):
    f = open("ErrorFile.txt", "a")  # open a text file to store error clusters
    index1 = 0  # Index of cluster
    while index1 < len(errorData):  # loop through clusters lines in text file
        index2 = 0  # Loop through cluster sensors in text file
        while index2 < len(errorData[index1]):
            ErrorFile = list()
            if errorData[index1][index2] == UniqueErrValue:  # Find error sensor with a unique error value of 2
                ErrorFile.append(errorData[index1][0])
                ErrorFile.append("Cluster {0}".format(index1 + 1))  #Store cluster with defect in ErrorFile
                ErrorFile.append("Sensor {0}".format(index2 + 1))  # Store defective sensor
                f.write(str(ErrorFile))  # Write defects to ErrorFile.txt
                f.write('\n')
            else:
                pass  # pass if no error found
            index2 = index2 + 1  # Check next sensor in cluster
        index1 = index1 + 1  # Move to next cluster
    f.close()

    return

def ExecuteProgram():
    Data = dummydataSet()  # Create a random dummy data set
    ErrorData = GenerateErrData(Data)  # introduce errors to random data in my dummy data set
    DataInFile = StoreDataInTextFile(Data)  # Write data that contains errors to a file
    STN = ConvErrorToNumber(DataInFile)  # Convert errors to numerical values
    ErrorData = logfileWithErrors(STN)  # Create and store data with errors only

    return

ExecuteProgram()
