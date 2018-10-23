from bs4 import BeautifulSoup
from requests import get
from json import loads
from re import findall

def getLists(deptnum):

    # Loads json from Rutgers API endpoint
    url = f'http://sis.rutgers.edu/soc/courses.json?campus=NB&semester=92018&level=U&subject={deptnum}'
    text = get(url).text
    soup = BeautifulSoup(text, 'lxml')
    classes = loads(soup.get_text())

    # Parses for the class id number and name
    courses = [f'{class_["offeringUnitCode"]}:{deptnum}:{class_["courseNumber"]}' for class_ in classes] 
    names = [class_['title'] for class_ in classes]
    
    # Gathers prereqs for each class and flattens the list
    prereqs = [[[p, f'{class_["offeringUnitCode"]}:{deptnum}:{class_["courseNumber"]}'] for p in 
        set(findall('\\d{{2}}:{}:\\d{{3}}'.format(deptnum), str(class_['preReqNotes'])))] for class_ in classes]
    prereqs = [item for class_ in prereqs for tup in class_ for item in tup]
    
    return (courses, names, prereqs)
