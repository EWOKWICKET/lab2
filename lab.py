dictionary = {}
lines = []
scores = [12, 10, 8, 7, 6, 5, 4, 3, 2, 1]
results = {}
with open('data1.csv', 'r', encoding='utf-8') as d1, open('data2.csv', 'r', encoding='utf-8') as d2, open('result.csv', 'w', encoding='utf-8') as out:
    lines_1 = d1.readlines()[1:]
    lines_2 = d2.readlines()[1:]
    for i in range(len(lines_1)):
        lines.extend(lines_1[i].strip().split(','))
    for i in range(len(lines_2)):
        lines.extend(lines_2[i].strip().split(','))
    
    for i in range(1, 21):
        dictionary[i] = {lines[j]: int(lines[j + i]) for j in range(0, len(lines), 21)}
        dictionary[i] = dict(sorted(dictionary[i].items(), key=lambda x: x[1], reverse=True)[:10])
        for j in range(len(dictionary[i])):
            dictionary[i][list(dictionary[i].keys())[j]] = scores[j]
        for k in dictionary[i].keys():
            results[k] = results.get(k, 0) + dictionary[i][k]
    results = dict(sorted(results.items(), key=lambda x: x[1], reverse=True)[:10])
    for k, v in results.items():
        out.write(f'{k} - {v}\n')           