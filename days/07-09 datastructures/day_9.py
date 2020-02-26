from data import us_state_abbrev, states_list 

def get_nth_item(data, n):
    '''print out the nth item in a list or dict'''
    if n > 50:
        result = 'There are less than {} states in the US...'.format(n)
    elif type(data) == list:
        result = data[n]
    else:
        result = list(data)[n]
            
    return result

print(get_nth_item(us_state_abbrev, n=127))

print(get_nth_item(us_state_abbrev, n=7))

print(get_nth_item(states_list, n=28))

print(get_nth_item(states_list, n=112))
