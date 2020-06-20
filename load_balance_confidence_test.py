from collections import Counter

from load_balance import select_server, select_server_older_python  # assuming load_balance.py is in a source folder
import sys

function_to_test = select_server


if __name__ == '__main__':
    iteration_counts = 100  # the more iterations, the closer the ratios are to what is expected
    assert len(sys.argv) > 1, 'Must provide server names and sizes seperated by a colon. E.g.: "X:5 Y:7"'
    args_dict = {x.split(':')[0]: int(x.split(':')[1]) for x in sys.argv[1:]}
    expected_ratios = {key: value/sum(list(args_dict.values())) * 100 for key, value in args_dict.items()}
    results = Counter([function_to_test(args_dict) for _ in range(iteration_counts)])
    result_ratios = {key: value/sum(list(results.values())) * 100 for key, value in results.items()}
    # print the results against expected weights:
    result_list = [(key, expected_ratios[key], result_ratios.get(key, 0)) for key in args_dict.keys()]
    report_string = 'Server:{}, Expected:{:.2f}, Actual:{:.2f}, Confidence:{:.2f}%'
    result_text = [report_string.format(*i, 100 - abs(i[2] - i[1])) for i in result_list]
    print(*result_text, sep='\n')
