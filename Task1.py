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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

def get_different_phone_numbers(records):
    
    global diff_phone_numbers

    for record in records:
        for i in range(2):
            diff_phone_numbers.add(record[i])


def main():
    get_different_phone_numbers(texts)
    get_different_phone_numbers(calls)

    print("There are {} different telephone numbers in the records.".format(len(diff_phone_numbers)))

def test_case_run():

    phone_numbers = [
        ['97424 22395', '90365 06212', '01-09-2016 06:03:22'],
        ['97424 22395', '92415 91418', '01-09-2016 06:03:22'],
        ['94489 72078', '97424 22395', '01-09-2016 06:05:35'],
    ]
    expected_numbers = {
        '97424 22395', '90365 06212', '92415 91418', '94489 72078'
    }
    expected_count = 4

    get_different_phone_numbers(phone_numbers)
    assert(diff_phone_numbers == expected_numbers)
    assert(len(diff_phone_numbers) == expected_count)

    get_different_phone_numbers(phone_numbers)
    assert(diff_phone_numbers == expected_numbers)
    assert(len(diff_phone_numbers) == expected_count)

    phone_numbers = [
        ['78130 00821', '92415 91418', '01-09-2016 06:01:12,186'],
        ['90365 06212', '(022)28952819', '01-09-2016 06:01:59,2093'],
        ['97424 22395', '94489 72078', '01-09-2016 06:03:51,1975'],
    ]
    expected_numbers = {
        '97424 22395', '90365 06212', '92415 91418', '94489 72078',
        '78130 00821', '(022)28952819',
    }
    expected_count = 6

    get_different_phone_numbers(phone_numbers)
    assert(diff_phone_numbers == expected_numbers)
    assert(len(diff_phone_numbers) == expected_count)
    get_different_phone_numbers(phone_numbers)
    assert(diff_phone_numbers == expected_numbers)
    assert(len(diff_phone_numbers) == expected_count)

    print('All tests are passed!')


# A list of different phone numbers.
diff_phone_numbers = set()
main()