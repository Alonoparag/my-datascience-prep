def build_shift_dict(shift):
        try:
            assert shift>= 0 and shift < 26
            assert type(shift) == int
        except AssertionError:
            print('Error, Shift key must be an integer from 0 to 26 excluding 26')
        except:
            print('An error has occured with the shift type')
        else:
            base_dict = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J',10:'K',11:'L',12:'M',13:'N',14:'O',15:'P',16:'Q',17:'R',18:'S',19:'T',20:'U',21:'V',22:'W',23:'X',24:'Y',25:'Z',26:'a',27:'b',28:'c',29:'d',30:'e',31:'f',32:'g',33:'h',34:'i',35:'j',36:'k',37:'l',38:'m',39:'n',40:'o',41:'p',42:'q',43:'r',44:'s',45:'t',46:'u',47:'v',48:'w',49:'x',50:'y',51:'z', }
            shifted_dict = {}
            for key in base_dict.keys():
                if key < 26:
                    if key - shift < 0:
                        print('base:', key, base_dict[key])
                        print('shift', 26-abs(key - shift), base_dict[26 - (abs(key - shift))])
                        shifted_dict[key] = base_dict[26 - (abs(key - shift))]
                    else:
                        print('base:', key, base_dict[key])
                        print('shift', 26-abs(key - shift), base_dict[26 - (abs(key - shift))])
                        shifted_dict[key] = base_dict[key-shift]
                else:
                    if key - shift < 26:
                        print('base:', key, base_dict[key])
                        print('shift', 52-abs(key - shift-26), base_dict[26 - abs(key - shift-26)])
                        shifted_dict[key] = base_dict[52-abs(key - shift-26)]
                    else:
                        shifted_dict[key] = base_dict[key - shift]
            return shifted_dict.copy()

build_shift_dict(3)


