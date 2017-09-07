#ghanta
def fn(s):
    current_states=set()
    current_states.add(1)
    next_states=set()
    for c in s:
        next_states=states(current_states,c)
        current_states=next_states
    return 4 in current_states




def states(current_states,current_char):
    next_states=set()
    for state in current_states:
        if state==1 and current_char=='a':
            next_states.add(1)
            next_states.add(2)
        elif state==1 and current_char=='b':
            next_states.add(1)
        elif state==2 and current_char=='b':
            next_states.add(3)
        elif state==3 and current_char=='b':
            next_states.add(4)
    return next_states
        
            


s = input()

if fn(s):
	print("accepted")
else:
   print("not accepted")