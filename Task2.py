"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
def get_longest_time_on_phone(records):
    global call_durations

    phone_numbers = set()
    longest_duration = 0

    for record in records:
        for i in range(2):
            phone_number = record[i]
            duration = int(record[-1])

            call_durations[phone_number] = call_durations.get(phone_number, 0) + duration

            if call_durations[phone_number] > longest_duration:
                longest_duration = call_durations[phone_number]
                phone_numbers = {phone_number}
            elif call_durations[phone_number] == longest_duration:
                phone_numbers.add(phone_number)

    return phone_numbers, longest_duration


def main():
    phone_numbers, total_time = get_longest_time_on_phone(calls)
    phone_number = ', '.join(phone_numbers)
    print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(phone_number, total_time))


def test_case_run():
    global call_durations

    calls = [
        ['78130 00821', '98453 94494', '01-09-2016 06:01:12', '186'],
        ['78298 91466', '(022)28952819', '01-09-2016 06:01:59', '2093'],
        ['(022)28952819', '78130 00821', '01-09-2016 06:03:51', '1975'],
        ['98453 94494', '(080)33118033', '01-09-2016 06:11:23', '1156'],
    ]
    expected_dict = {
        '78130 00821': 2161,
        '98453 94494': 1342,
        '78298 91466': 2093,
        '(022)28952819': 4068,
        '(080)33118033': 1156
    }

    call_durations.clear()
    phone_numbers, total_time = get_longest_time_on_phone(calls)
    assert(1 == len(phone_numbers))
    assert({'(022)28952819'} == phone_numbers)
    assert (4068 == total_time)
    assert(expected_dict == call_durations)
    calls = [
        ['(04344)228249', '(080)43901222', '01-09-2016 06:50:04', '2329'],
        ['(080)62164823', '74066 93594', '01-09-2016 06:52:07', '300'],
        ['(0821)6141380', '90366 69257', '01-09-2016 06:54:44', '2147'],
        ['98446 66723', '83019 53227', '01-09-2016 06:56:16', '129'],
        ['90088 09624', '93434 31551', '01-09-2016 06:57:44', '133']
    ]
    expected_dict = {
        '(04344)228249': 2329,
        '(080)43901222': 2329,
        '(080)62164823': 300,
        '74066 93594': 300,
        '(0821)6141380': 2147,
        '90366 69257': 2147,
        '98446 66723': 129,
        '83019 53227': 129,
        '90088 09624': 133,
        '93434 31551': 133
    }
    call_durations.clear()
    phone_numbers, total_time = get_longest_time_on_phone(calls)
    assert(2 == len(phone_numbers))
    assert({'(04344)228249', '(080)43901222'} == phone_numbers)
    assert (2329 == total_time)
    assert(expected_dict == call_durations)

    print('All tests are passed!')
    call_durations.clear()

call_durations = {}

main()
