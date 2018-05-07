import journal


def write_header():
    print('-------------------')
    print('   JOURNAL APP')
    print('-------------------')


def event_loop():
    print('What do you want to do with your journal?')
    cmd = 'EMPTY'
    journal_name = 'default'
    journal_data = journal.load(journal_name)

    while cmd != 'x' and cmd:
        cmd = input('[L]ist entries, [A]dd an entry, E[x]it: ')
        cmd = cmd.lower().strip()

        if cmd == 'l':
            list_entries(journal_data)
        elif cmd == 'a':
            add_entry(journal_data)
        elif cmd != 'x' and cmd:
            print(f"Sorry, we don't understand {cmd}.")

    print('Done, goodbye.')
    journal.save(journal_name, journal_data)


def list_entries(data):
    print('Your journal entries:')
    entries = reversed(data)
    for idx, entry in enumerate(entries):
        print(f'[{idx+1}]: {entry}')


def add_entry(data):
    text = input('Type your entry, <enter> to exit: ')
    journal.add_entry(text, data)


def main():
    write_header()
    event_loop()


if __name__ == '__main__':
    main()
