import json
import enum

# Used to convert output from hazedumper to a .py file

def main():
    with open('csgo.json', 'r') as f:
        data = json.load(f)

        with open('offsets.py', 'a') as output:

            output.write('import enum\n\n')
            output.write('class Offsets(enum.IntEnum):\n')

            for k, v in data['signatures'].items():
                output.write(f'\t{k} = {hex(v)}\n')

            for k, v in data['netvars'].items():
                output.write(f'\t{k} = {hex(v)}\n')

if __name__ == '__main__':
    main()