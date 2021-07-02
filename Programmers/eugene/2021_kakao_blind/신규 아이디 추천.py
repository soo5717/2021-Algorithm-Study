import re
def solution(new_id):
    answer = ''
    
    #step1.
    new_id=new_id.lower()
    #step2.
    new_id=''.join(re.findall('[a-z0-9-_.]+', new_id))
    #step3.
    new_id = re.sub('[..]+', '.', new_id)
    #step4.
    new_id = new_id.strip('.')
    #step5.
    if len(new_id) == 0:
        new_id = 'a'
    
    lenNewId = len(new_id)
    #step6.
    if lenNewId >= 16:
        new_id=new_id[:15]
        new_id = new_id.strip('.')
    #step7.
    elif lenNewId <=2:
        new_id=new_id+new_id[-1]*(3-lenNewId)
    
    return new_id
