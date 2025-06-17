rules = {
    #fill out rules according to the manual
    #format: "page number" : "pages needed to be updated after current page
}

def addRules(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            if '|' in line:
                x, y = line.strip().split('|')
                x, y = int(x), int(y)
                if x not in rules:
                    rules[x] = {y}  
                else:
                    rules[x].add(y)

    return

#gå gjennom alle linjer med komma, sjekke om alle tall oppfyller regler som gjelder (kan sjekkes på o index > index2),
#hvis ja legger til midt-tallet i en global sum

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

addRules('Day 5/safetyManual.txt')
checkRules('Day 5/safetyManual.txt')