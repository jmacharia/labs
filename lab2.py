
def data_type(data):
    '''
    This function takes one argument, compares and returns results based
    on the argument supplied to the function
    '''
    #return length if argument is a string
    if type(data) == str:
        return len(data)

    #return no value if argument is a Nonetype
    elif data == None:
        return "no value"

    #return bolean if argument is a boolean
    elif type(data) == bool:
    	return boolean

    #return string showing if argument is a less or more that 100
    elif type(data) == int:
        if data > 100:
            return "more than 100"
        else:
            return "less than 100"

    #return the third item if argument is a list
    elif type(data) == list:
    	return data[2]

data_value = data_type(['joe', 24, {1: 'done'}, [1, 'list']])
print data_value
