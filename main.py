import requests;

profiles = list(['dasdafsafas', 'dasdasdas'])
N = profiles.__len__()
allPapers = list

# GET PAPERS
for profile in profiles:
    papersForProfile = requests.get('http://google-scholar.com/' + profile)
    allPapers.extend(papersForProfile)

# DISTINCT
distinctPapers = list;
for paper in allPapers:
    if not distinctPapers.__contains__(paper):
        distinctPapers.push(paper)

# GET POINTS
for distinctPaper in distinctPapers:
    distinctPaper.points = requests.get(
        'http://points.com/journalPoints?year=' + distinctPaper.year + '&journalCode' + distinctPaper.journalCode)

# SORT PAPERS
distinctPapers.sort(key=lambda paper: paper.points, reverse=True)

# CALCULATE POINTS FOR N PAPERS
score = 0
for i in range(0, N):
    score+= distinctPapers[i]

print score