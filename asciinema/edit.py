import json

f = open('edited.cast', 'r')

pre_typing_timing = 1
typing_timing = 0.08
line_timing = 0.5
pause_timing = 3

typing = False
output_timestamp = 0
input_timestamp = 0

for l in f.readlines():
    line = l[:-1]
    if line == '-- start typing':
        typing = True
        output_timestamp = output_timestamp + pre_typing_timing
    elif line == '-- stop typing':
        typing = False
    elif line == '-- pause':
        output_timestamp = output_timestamp + pause_timing
    elif len(line) > 0:
        o = json.loads(line)
        if isinstance(o, list):
            if typing and o[2] != '\r\n':
                for c in o[2]:
                    output_timestamp = output_timestamp + typing_timing
                    print(json.dumps([output_timestamp, 'o', c]))
            elif typing and o[2] == '\r\n':
                output_timestamp = output_timestamp + line_timing
                print(json.dumps([output_timestamp, 'o', '\r\n']))
            else:
                previous_input_timestamp = input_timestamp
                output_timestamp = output_timestamp + (o[0] - previous_input_timestamp)
                print(json.dumps([output_timestamp, o[1], o[2]]))
            input_timestamp = o[0]
        else:
            print(json.dumps(o))

f.close()
