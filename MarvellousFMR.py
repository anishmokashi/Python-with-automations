# Taks : Name of function
# Elements : List of data elements
def filterX(Task, Elements):
    Result = []
    for no in Elements:
        if(Task(no) == True):
            Result.append(no)
    return Result

# Taks : Name of function
# Elements : List of data elements
def mapX(Task, Elements):
    Result = []
    for no in Elements:
        Ret = Task(no)
        Result.append(Ret)
    return Result

# Taks : Name of function
# Elements : List of data elements
def reduceX(Task, Elements):
    Sum = 0
    for no in Elements:
        Sum = Task(Sum,no)
    return Sum
