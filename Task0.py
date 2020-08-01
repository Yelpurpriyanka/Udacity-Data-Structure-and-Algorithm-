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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

def main():
    print("First record of texts, {} texts {} at time {}".format(*texts[0]))

    print("Last record of calls, {} calls {} at time {}, lasting {} seconds".format(*calls[-1]))

def test_case_run():

    import io
    from contextlib import redirect_stdout

    actual = None

    with io.StringIO() as obuffer, redirect_stdout(obuffer):
        main()
        actual = obuffer.getvalue()

    assert("First record of texts, 97424 22395 texts 90365 06212 at time 01-09-2016 06:03:22" in actual)
    assert ("Last record of calls, 98447 62998 calls (080)46304537 at time 30-09-2016 23:57:15" in actual)

    print('All test cases are passed!')

main()

