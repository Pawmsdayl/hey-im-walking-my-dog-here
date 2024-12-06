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

useless_breed_words = {
    'mixed',
    'mix',
    'mix ',
    'x',
    'crossbreed'
}

# Source: https://www.nycbynatives.com/nyc_info/new_york_city_zip_codes.php
# Source: https://www.bizzarroagency.com/new-york-city-zip-codes/
nyc_zip_codes = {
    10001, 10002, 10003, 10004, 10005, 
    10006, 10007, 10008, 10009, 10010, 
    10011, 10012, 10013, 10014, 10015, 
    10016, 10017, 10018, 10019, 10020, 
    10021, 10022, 10023, 10024, 10025, 
    10026, 10027, 10028, 10029, 10030, 
    10031, 10032, 10033, 10034, 10035, 
    10036, 10037, 10038, 10039, 10040, 
    10041, 10044, 10045, 10048, 10055, 
    10060, 10069, 10090, 10095, 10098, 
    10099, 10103, 10104, 10105, 10106, 
    10107, 10110, 10111, 10112, 10115, 
    10118, 10119, 10120, 10121, 10122, 
    10123, 10128, 10151, 10152, 10153, 
    10154, 10155, 10158, 10161, 10162, 
    10165, 10166, 10167, 10168, 10169, 
    10170, 10171, 10172, 10173, 10174, 
    10175, 10176, 10177, 10178, 10199, 
    10270, 10271, 10278, 10279, 10280, 
    10281, 10282, 10301, 10302, 10303, 
    10304, 10305, 10306, 10307, 10308, 
    10309, 10310, 10311, 10312, 10314, 
    10451, 10452, 10453, 10454, 10455, 
    10456, 10457, 10458, 10459, 10460, 
    10461, 10462, 10463, 10464, 10465, 
    10466, 10467, 10468, 10469, 10470, 
    10471, 10472, 10473, 10474, 10475, 
    11004, 11101, 11102, 11103, 11104, 
    11105, 11106, 11109, 11201, 11203, 
    11204, 11205, 11206, 11207, 11208, 
    11209, 11210, 11211, 11212, 11213, 
    11214, 11215, 11216, 11217, 11218, 
    11219, 11220, 11221, 11222, 11223, 
    11224, 11225, 11226, 11228, 11229, 
    11230, 11231, 11232, 11233, 11234, 
    11235, 11236, 11237, 11238, 11239, 
    11241, 11242, 11243, 11249, 11252, 
    11256, 11351, 11354, 11355, 11356, 
    11357, 11358, 11359, 11360, 11361, 
    11362, 11363, 11364, 11365, 11366, 
    11367, 11368, 11369, 11370, 11371, 
    11372, 11373, 11374, 11375, 11377, 
    11378, 11379, 11385, 11411, 11412, 
    11413, 11414, 11415, 11416, 11417, 
    11418, 11419, 11420, 11421, 11422, 
    11423, 11426, 11427, 11428, 11429, 
    11430, 11432, 11433, 11434, 11435, 
    11436, 11691, 11692, 11693, 11694, 
    11697
}