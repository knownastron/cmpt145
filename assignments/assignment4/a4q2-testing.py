#Name: Jason Tran
#NSID: jat687
#Student Number: 11101081
#Course: CMPT 145-01
#Lab: L03

import a4q2 as Check

#####################################################################
# test Check.check_balance()
# Unit testing


test_create = [
    {'inputs' : ['(adsf)'],
     'outputs':[True],
     'reason' : 'one parenthesis - balanced - true'
     },
    {'inputs' : ['[adsf]'],
     'outputs':[True],
     'reason' : 'one square bracket - balanced - true'
     },
    {'inputs' : ['{adfa}'],
     'outputs':[True],
     'reason' : 'one curly bracket - balanced - true'
     },
    {'inputs' : ['((asf{{adsf[[({ad})adf]]}asdf}))'],
     'outputs':[True],
     'reason' : 'mix of curly bracket, square bracket, and parentheses'
     },
    {'inputs' : ['(a*b) + 4}'],
     'outputs':[False],
     'reason' : 'missing open bracket'
     },
    {'inputs' : ['[(a+b)'],
     'outputs':[False],
     'reason' : 'missing closed bracket'
     },
    {'inputs' : ['} [b+(a)] {'],
     'outputs':[False],
     'reason' : 'closed bracket appears before open bracket'
     },
    {'inputs' : ['{a+b) * (c * d}'],
     'outputs':[False],
     'reason' : 'closing bracket is not to the right of the appropriate open' +
                'bracket'
     },
    {'inputs' : ['[( a+b ] * 5)'],
     'outputs':[False],
     'reason' : 'parenthesis can only close when all parentheses opened' +
                ' after are closed'
     }
]

for t in test_create:
    args_in = t['inputs']
    expected = t['outputs']

    #get result from check_balance
    result = Check.check_balance(args_in[0])

    if result != expected[0]:
        print('Error in check_balance(): expected', expected[0],
            'but returned', result, '--', t['reason'])



print('*** Test script completed ***')
