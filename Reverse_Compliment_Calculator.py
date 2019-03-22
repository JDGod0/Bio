def reverse_compliment_calculator():
    
    # Takes an input and checks that it only contains a, t, g and c.
    
    x = False
    while x == False:
        oligo = input('Please enter oligo sequence').lower()
        accept = set('atgc')
        if set(oligo).issubset(accept):
            x = True
        else:
            print('Oligos may only contain a, t, g and c. Please check oligo sequence and try again')
            
    # Reverses the input        
    
    oligo_rev = oligo[::-1]
    
    # Replaces a with t, g with c etc.  Changes to upper case to ensure previously converted characters are not coverted again.
    
    oligo_rev = oligo_rev.replace('a','T').replace('t','A').replace('g','C').replace('c','G') 
    print(oligo_rev)

if __name__ == '__main__':
    reverse_compliment_calculator()