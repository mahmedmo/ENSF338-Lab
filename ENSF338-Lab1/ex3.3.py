import json
import timeit
import numpy as np
import matplotlib.pyplot as plt

# update_all_sizes generated with ChatGPT
def update_all_sizes(obj):
    if isinstance(obj, dict):
        for key, value in obj.items():
            if key == 'size':
                obj[key] = 35
            else:
                update_all_sizes(value)
    elif isinstance(obj, list):
        for item in obj:
            update_all_sizes(item)

def test_update_all_sizes(json_data,run_no):
    elapsed_time = timeit.timeit(lambda: update_all_sizes(json_data), number=run_no)
    print(f'Average elapsed time: {elapsed_time/run_no} seconds')

def update_json(file_in, file_out):
    with open(file_in, 'r') as j_file:
        json_data = json.load(j_file)
    json_data.reverse()
    with open(file_out, 'w') as j_file:
        json.dump(json_data, j_file,indent = 4)

    print("Exercise 3.3 Histogram...")
    sliced_data = json_data[:1000]

    times = timeit.repeat(lambda: update_all_sizes(sliced_data), repeat=1000, number=1)

    # histogram plotted via ChatGPT
    plt.hist(times, bins=50, color='green', alpha=0.5)
    plt.xlabel('Time (seconds)')
    plt.ylabel('Frequency')
    plt.title('Distribution of Processing Times for 1000 Records')
    plt.savefig('ENSF338-Lab1/output.3.3.png')
    plt.close()
    print("Histogram complete! Saved to output.3.3.png")


file_in = 'ENSF338-Lab1/large-file.json'
file_out = 'ENSF338-Lab1/output.2.3.json'

update_json(file_in, file_out)
