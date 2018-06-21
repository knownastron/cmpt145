#Name: Jason Tran
#NSID: jat687
#Student Number: 11101081
#Course: CMPT 145-01
#Lab: L03

import a4q2 as Check

#####################################################################
# test Check.check_balance()
# Unit testing


test_check_balance = [
    {'inputs' : ['Hello World!'],
     'outputs': [True],
     'reason' : 'No parenthesis, curly bracket, or square bracket - balanced'
     },
    {'inputs' : ['(adsf)'],
     'outputs':[True],
     'reason' : 'one parenthesis - balanced'
     },
    {'inputs' : ['[adsf]'],
     'outputs': [True],
     'reason' : 'one square bracket - balanced'
     },
    {'inputs' : ['{adfa}'],
     'outputs': [True],
     'reason' : 'one curly bracket - balanced'
     },
    {'inputs' : ['((asf{{adsf[[({ad})adf]]}asdf}))'],
     'outputs': [True],
     'reason' : 'mix of curly bracket, square bracket, and parentheses - balanced'
     },
    {'inputs' : ['{{())([{(})()(){}{[]}}]))}()}'],
     'outputs': [False],
     'reason' : 'mix of curly bracket, square bracket, and parentheses - unbalanced'
     },
    {'inputs' : ['(a*b) + 4}'],
     'outputs': [False],
     'reason' : 'missing open curly bracket'
     },
    {'inputs' : ['[(a+b)'],
     'outputs': [False],
     'reason' : 'missing closing square bracket'
     },
    {'inputs' : ['} [b+(a)] {'],
     'outputs': [False],
     'reason' : 'closed curly bracket appears before open bracket'
     },
    {'inputs' : ['{a+b) * (c * d}'],
     'outputs': [False],
     'reason' : 'closing curly bracket is not to the right of the appropriate' +
                'open curly bracket'
     },
    {'inputs' : ['[( a+b ] * 5)'],
     'outputs': [False],
     'reason' : 'parenthesis can only close when all parentheses opened' +
                ' after are closed'
     }
]

for t in test_check_balance:
    args_in = t['inputs']
    expected = t['outputs']

    #get result from check_balance
    result = Check.check_balance(args_in[0])

    if result != expected[0]:
        print('Error in check_balance(): expected', expected[0],
            'but returned', result, '--', t['reason'])



print('*** Test script completed ***')
