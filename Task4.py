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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

def get_telemarketers_from_calls():
    global telemarketers

    calls_to = set()
    for record in calls:
        calls_to.add(record[1])

    for record in calls:
        call_from = record[0]
        if call_from not in calls_to:
            telemarketers.add(call_from)


def remove_texts_from_telemarketers():
    global telemarketers
    for record in texts:
        for i in range(2):
            # Remove the phone number if it exists in the telemarketers set.
            phone_number = record[i]
            if phone_number in telemarketers:
                telemarketers.remove(phone_number)


def main():
    
    global telemarketers

    get_telemarketers_from_calls()
    remove_texts_from_telemarketers()

    # Sort the distinct phone numbers 
    telemarketers = list(telemarketers)
    telemarketers.sort()  

    print("These numbers could be telemarketers: ")
    for phone_number in telemarketers:
        print(phone_number)


def test_case_run():
    global telemarketers, calls, texts
    original_calls = calls
    original_texts = texts

    calls = [
        ['(080)67362492', '1408371942', '01-09-2016 06:19:28', '2751'],
        ['78290 31269', '77956 90632', '01-09-2016 06:39:03', '3043'],
        ['98453 46196', '(080)46304537', '01-09-2016 06:40:20', '2457'],
        ['(080)67362492', '(080)43901222', '01-09-2016 06:46:56', '9'],
        ['(04344)228249', '(080)62164823', '01-09-2016 06:50:04', '2329'],
        ['(080)62164823', '74066 93594', '01-09-2016 06:52:07', '300'],
        ['(080)45291968', '90365 06212', '01-09-2016 06:30:36', '9'],
        ['(0821)6141380', '90366 69257', '01-09-2016 06:54:44', '2147'],
        ['(080)46304537', '(04344)322628', '01-09-2016 06:30:36', '9'],
    ]
    expected = {
        '(080)67362492',
        '78290 31269',
        '98453 46196',
        '(04344)228249',
        '(080)45291968',
        '(0821)6141380'
    }
    get_telemarketers_from_calls()
    assert(telemarketers == expected)

    # '78290 31269' and '98453 46196' should be removed.
    texts = [
        ['90367 90080', '74066 93594', '03-09-2016 16:21:57'],
        ['78290 31269', '97386 37259', '03-09-2016 16:26:30'],
        ['93436 09781', '98448 72117', '03-09-2016 16:28:26'],
        ['99007 06998', '84314 00609', '03-09-2016 16:30:26'],
        ['81524 55552', '98453 46196', '03-09-2016 16:30:55'],
        ['81520 43406', '92421 64236', '03-09-2016 16:35:36'],
        ['94495 34273', '94491 05266', '03-09-2016 16:36:25'],
        ['90083 59148', '97421 07528', '03-09-2016 16:37:30'],
    ]
    expected = {
        '(080)67362492',
        '(04344)228249',
        '(080)45291968',
        '(0821)6141380'
    }
    remove_texts_from_telemarketers()
    assert(telemarketers == expected)

    print('All tests  are passed!')
    telemarketers.clear()
    calls = original_calls
    texts = original_texts

telemarketers = set()

main()