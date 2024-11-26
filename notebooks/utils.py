breed_mapping = {
    # OTHER
    'refused to provide' : 'other', 
    'uknown' : 'other', 
    'un' : 'other', 
    'unc' : 'other', 
    'uncertain' : 'other', 
    'unkown' : 'other', 
    'unnkown' : 'other', 
    'unsure' : 'other', 
    'unknown' : 'other',
    'mix' : 'other', 
    'mix breed' : 'other', 
    'mix ' : 'other', 
    'mixed breed' : 'other',
    '' : 'other',
    'breed' : 'other',
    'large breed' : 'other',
    'small breed' : 'other',
    
    # PIT BULL
    'american pit bull' : 'pit bull', 
    'american pit bull ' : 'pit bull', 
    'american pit bull terrier' : 'pit bull', 
    'pitbull' : 'pit bull',
    
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