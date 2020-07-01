'''
Just looking at some of the easy Leetcode question to prepare for interview preparation
'''

#Max Sub Array 

def max_sub_array(the_array: list) -> int:
    numero = 0
    largest = numero
    for num in range(len(the_array)):
        numero += the_array[num]
        if numero < 0:
            numero = 0
        if numero > largest:
            largest = numero
        
    return largest



    
    def is_valid(self, s: str) -> bool:
            tracker = []
        for idx, c in enumerate(s):
            if s[idx] == '(' or s[idx] == '[' or s[idx] == '{':
                tracker.append(c)
            if c == '}': 
                if not tracker[-1] == '{':
                    return False
                else: 
                    tracker.pop()
                    
            if c == ']': 
                if not tracker[-1] == '[':
                    return False
                else: 
                    tracker.pop()
                    
            if c == ')': 
                if not tracker[-1] == '(':
                    return False
                else: 
                    tracker.pop()
        
        if len(tracker) == 0:
            return True
        
        else:
            return False