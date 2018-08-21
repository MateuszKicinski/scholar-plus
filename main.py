import requests;

profiles = list(['dasdafsafas', 'dasdasdas'])
fromYear = 2010
toYear = 2018
N = profiles.__len__()
allPapers = list

# GET PAPERS
for profile in profiles:
    papersForProfile = requests.get('http://google-scholar.com/' + profile + '?from=' + fromYear + '&to=' + toYear)
    allPapers.extend(papersForProfile)

# DISTINCT
distinctPapers = list;
for paper in allPapers:
    if not distinctPapers.__contains__(key=lambda paper: paper.name):
        distinctPapers.push(paper)

# GET POINTS
for distinctPaper in distinctPapers:
    distinctPaper.points = requests.get(
        'http://points.com/journalPoints?year=' + distinctPaper.year + '&journalCode' + distinctPaper.journalCode)

# SORT PAPERS
distinctPapers.sort(key=lambda paper: paper.points, reverse=True)

# CALCULATE POINTS FOR N PAPERS
score = 0
displayPapers = list
for i in range(0, N):
    displayPapers[i] = distinctPapers[i]
    score += distinctPapers[i]

print score, displayPapers
