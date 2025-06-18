rules = {
    #fill out rules according to the manual
    #format: "page number" : "pages needed to be updated after current page
}

def addRules(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            if '|' in line:
                x, y = map(int, line.strip().split('|'))
                if x not in rules:
                    rules[x] = {y}  
                else:
                    rules[x].add(y)

    return

def checkRules(filename):
    sum = 0
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if ',' in line:
                pages = list(map(int, line.split(',')))

                valid = True
                for page in pages:
                    if page in rules:
                        for after_page in rules[page]:
                            if after_page in pages:
                                if pages.index(after_page) < pages.index(page):
                                    valid = False
                                    break
                        if not valid:
                            break

                if valid:
                    sum += pages[len(pages) // 2]

    return print(sum)



def is_valid_order(pages):
    for x in pages:
        if x in rules:
            for y in rules[x]:
                if y in pages:
                    if pages.index(x) > pages.index(y):
                        return False
    return True

def sort_by_rules(pages):
    scores = []
    for page in pages:
        count = 0
        after_pages = rules.get(page, set())
        for other in pages:
            if other in after_pages:
                count += 1
        scores.append([page, count])

    sorted_pages = []
    while scores:
        # find index of max score
        max_index = 0
        for i in range(1, len(scores)):
            if scores[i][1] > scores[max_index][1]:
                max_index = i
        # pop the max score item and add its page to result
        max_item = scores.pop(max_index)
        sorted_pages.append(max_item[0])

    return sorted_pages



def fixBrokenQueue(filename):
    sum = 0
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if ',' in line:
                pages = list(map(int, line.split(',')))
                if not is_valid_order(pages):
                    fixed = sort_by_rules(pages)
                    sum += fixed[len(fixed) // 2]

    return print(sum)


addRules('Day 5/safetyManual.txt')
checkRules('Day 5/safetyManual.txt')
fixBrokenQueue('Day 5/safetyManual.txt')