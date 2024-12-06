breed_mapping = {
    # MIXED/ OTHER
    'refused to provide' : 'mixed/other', 
    'uknown' : 'mixed/other', 
    'un' : 'mixed/other', 
    'unc' : 'mixed/other', 
    'uncertain' : 'mixed/other', 
    'unkown' : 'mixed/other', 
    'unnkown' : 'mixed/other', 
    'unsure' : 'mixed/other', 
    'unknown' : 'mixed/other',
    'mix' : 'mixed/other', 
    'mix breed' : 'mixed/other', 
    'mix ' : 'mixed/other', 
    'mixed breed' : 'mixed/other',
    '' : 'mixed/other',
    'breed' : 'mixed/other',
    'large breed' : 'mixed/other',
    'small breed' : 'mixed/other',
    'other' : 'mixed/other',
    
    # PIT BULL
    'american pit bull' : 'pit bull', 
    'american pit bull ' : 'pit bull', 
    'american pit bull terrier' : 'pit bull', 
    'pitbull' : 'pit bull',
    'blue nosed pit bull': 'pit bull',
    
    # HUSKY
    'siberian husky' : 'husky',
    
    # BULL DOG
    'american bull dog' : 'bull dog', 
    'english bull dog' : 'bull dog', 
    'french bull dog' : 'bull dog', 
    'bull dog, french' : 'bull dog', 
    'bull dog, english' : 'bull dog', 
    'bull dog, american' : 'bull dog', 
    'bulldog' : 'bull dog',
    
    # STANDARD POODLE
    'poodle, standard' : 'standard poodle',
    'poodle' : 'standard poodle',
    
    # TOY POODLE
    'poodle, toy' : 'toy poodle',
    
    # MINIATURE POODLE
    'poodle, miniature' : 'miniature poodle',
    
    # SHEPHERD
    'sheperd' : 'shepherd',
    
    # LABRADOR RETRIEVER
    'labrador' : 'labrador retriever'
}

useless_breed_words = [
    'mixed',
    'mix',
    'mix ',
    'x',
    'crossbreed'
]