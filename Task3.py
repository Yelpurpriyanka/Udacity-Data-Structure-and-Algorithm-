"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
def is_bangalore(phone_number):
    if not phone_number[:5] == '(080)':
        return False
    return phone_number[5:].isnumeric()


def is_fixed_line(phone_number):
    return phone_number[:2] == '(0'


def is_mobile(phone_number):
    # Checks if the phone number starts with a 7, 8, or 9.
    if not (phone_number[0] == '7' or
            phone_number[0] == '8' or
            phone_number[0] == '9'):
        return False

    middle_index = len(phone_number) // 2
    return phone_number[middle_index] == ' '


def is_telemarketer(phone_number):
    # If the number does not start with 140, return False.
    if not phone_number[:3] == '140':
        return False
    return phone_number[3:].isnumeric()


def get_area_code(phone_number):
    code = '0'
    for i in range(2, len(phone_number)):
        if phone_number[i] == ')':
            break
        code += phone_number[i]

    return code


def get_mobile_prefix(phone_number):
    return phone_number[:4]

def get_calls_made_from_bangalore(records):
    """
    list of all calls made by people in Bangalore.
    """
    global number_of_calls_made

    calls_made = []

    for record in records:
        # Skipping a call if not made from Bangalore.
        if not is_bangalore(record[0]):
            continue

        number_of_calls_made += 1

        calls_made.append(record[1])

    return calls_made


def get_codes(calls_made):
    global calls_to_bangalore

    codes = set()
    has_telemarketer = False

    for phone_number in calls_made:

        
        if is_telemarketer(phone_number) and not has_telemarketer:
            codes.add('140')
            has_telemarketer = True

        
        elif is_mobile(phone_number):
            codes.add(get_mobile_prefix(phone_number))

       
        elif is_fixed_line(phone_number):
            codes.add(get_area_code(phone_number))

            
            if is_bangalore(phone_number):
                calls_to_bangalore += 1

    return list(codes)


def main():
    
    #Runs the main program.
    
    global number_of_calls_made, calls_to_bangalore

    calls_made = get_calls_made_from_bangalore(calls)
    codes = get_codes(calls_made)

    # Part A:
    codes.sort() 
    print("The numbers called by people in Bangalore have codes:")
    for code in codes:
        print(code)

    # Part B:
    percentage_of_calls = round((calls_to_bangalore / number_of_calls_made) * 100, 2)
    print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(str(percentage_of_calls)))


def test_case_run():
    global number_of_calls_made, calls_to_bangalore
    number_of_calls_made = 0
    calls_to_bangalore = 0

    # Testing a telemarketer numbers.
    assert(is_telemarketer('1408371942'))
    assert(not is_telemarketer('140 8371942'))
    assert(not is_telemarketer('(140)8371942'))
    assert(not is_fixed_line('1408371942'))
    assert(not is_mobile('1408371942'))

    # Testing a fixed line numbers.
    assert(is_fixed_line('(04344)316423'))
    assert(not is_mobile('(04344)316423'))
    assert(not is_telemarketer('(04344)316423'))
    assert(get_area_code('(04344)316423') == '04344')

    # Testing a bangalore numbers.
    assert(is_fixed_line('(080)67362492'))
    assert(is_fixed_line('(080)32255824'))
    assert(is_bangalore('(080)67362492'))
    assert(is_bangalore('(080)32255824'))
    assert(not is_bangalore('(080) 32255824'))
    assert(not is_bangalore('( 080 )32255824'))
    assert(not is_bangalore('(04344)322628'))
    assert(not is_bangalore('99003 47921'))
    assert(not is_bangalore('1408371942'))

    # Test all mobile numbers.
    test_data = {
        '92421 09526': '9242',
        '77956 90632': '7795',
        '74066 93594': '7406',
        '98453 46196': '9845',
    }
    for phone_number, prefix in test_data.items():
        assert(is_mobile(phone_number))
        assert(not is_fixed_line(phone_number))
        assert(not is_telemarketer(phone_number))
        assert(get_mobile_prefix(phone_number) == prefix)

    number_of_calls_made = 0
    calls_to_bangalore = 0
    test_data = [
        [
            ['(080)67362492', '1408371942', '01-09-2016 06:19:28', '2751'],
            ['78132 18081', '77956 90632', '01-09-2016 06:39:03', '3043'],
            ['98453 46196', '94005 06213', '01-09-2016 06:40:20', '2457'],
            ['(080)62164823', '(080)43901222', '01-09-2016 06:46:56', '9'],
            ['(04344)228249', '(080)43901284', '01-09-2016 06:50:04', '2329'],
            ['(080)62164823', '74066 93594', '01-09-2016 06:52:07', '300'],
            ['(080)45291968', '90365 06212', '01-09-2016 06:30:36', '9'],
            ['(0821)6141380', '90366 69257', '01-09-2016 06:54:44', '2147'],
            ['(080)46304537', '(04344)322628', '01-09-2016 06:30:36', '9'],
        ],
        [
            ['(080)67362492', '1408371942', '01-09-2016 06:19:28', '2751'],
            ['(080)67362492', '(080)43901222', '01-09-2016 06:19:28', '2751'],
            ['(080)45291968', '90365 06212', '01-09-2016 06:30:36', '9'],
            ['(080)62164823', '(04344)322628', '01-09-2016 06:52:07', '300'],
            ['(080)61413801', '(04344)322628', '01-09-2016 06:54:44', '2147'],
            ['(080)67362492', '1408371942', '01-09-2016 06:19:28', '2751'],
            ['(080)46304537', '90365 06212', '01-09-2016 06:30:36', '9'],
            ['(080)62164823', '(080)43901222', '01-09-2016 06:46:56', '9'],
        ]
    ]

    # Testing of  getting calls from Bangalore.
    expected = [
        '1408371942',
        '(080)43901222',
        '74066 93594',
        '90365 06212',
        '(04344)322628'
    ]
    calls_made = get_calls_made_from_bangalore(test_data[0])
    assert(calls_made == expected)
    codes = get_codes(calls_made)
    expected = ['140', '080', '74066', '90365', '04344']
    assert(codes.sort() == expected.sort())
    assert(number_of_calls_made == 5)
    assert(calls_to_bangalore == 1)
    number_of_calls_made = 0
    calls_to_bangalore = 0
    expected = [
        '1408371942',
        '(080)43901222',
        '90365 06212',
        '(04344)322628',
        '(04344)322628',
        '1408371942',
        '90365 06212',
        '(080)43901222'
    ]
    calls_made = get_calls_made_from_bangalore(test_data[1])
    assert(calls_made == expected)

    codes = get_codes(calls_made)
    assert(len(codes) == 4)
    expected = ['140', '080', '90365', '04344']
    assert(codes.sort() == expected.sort())
    assert(number_of_calls_made == 8)
    assert(calls_to_bangalore == 2)


    print('All tests are passed!')
    number_of_calls_made = 0
    calls_to_bangalore = 0
number_of_calls_made = 0
calls_to_bangalore = 0

main()