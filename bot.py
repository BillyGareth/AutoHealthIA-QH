import pandas as pd
import time
import wikipedia
from sklearn import preprocessing
from sklearn.tree import DecisionTreeClassifier, _tree
import numpy as np
from sklearn import model_selection as model_selection
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_validate as cross_validation
from sklearn.tree import export_graphviz
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

print('Please wait as I get ready...')

training = pd.read_csv('Training.csv')
testing = pd.read_csv('Testing.csv')
cols = training.columns
cols = cols[:-1]
x = training[cols]
y = training['prognosis']
y1 = y

reduced_data = training.groupby(training['prognosis']).max()

#mapping strings to numbers
le = preprocessing.LabelEncoder()
le.fit(y)
y = le.transform(y)


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)
testx = testing[cols]
testy = testing['prognosis']
testy = le.transform(testy)


clf1 = DecisionTreeClassifier()
clf = clf1.fit(x_train, y_train)
#print(clf.score(x_train,y_train))
#print ("cross result========")
scores = model_selection.cross_val_score(clf, x_test, y_test, cv=3)
#print (scores)
#print (scores.mean())
#print(clf.score(testx,testy))

importances = clf.feature_importances_
indices = np.argsort(importances)[::-1]
features = cols

#feature_importances
for f in range(10):
    print("%d. feature %d - %s (%f)" % (f + 1, indices[f], features[indices[f]], importances[indices[f]]))

print("Please reply Yes or No for the following symptoms") 
def print_disease(node):
    #print(node)
    node = node[0]
    #print(len(node))
    val = node.nonzero()
    #print(val)
    disease = le.inverse_transform(val[0])
    return disease

sms = "Helloooooo.....!"
for i in sms:
    print(i, end='')
    time.sleep(0.07)
print()
sms1 = 'My name is AutoHealthIA and I like it '
for i in sms1:
    print(i, end='')
    time.sleep(0.07)
print()
yourName = str(input('What is your name? '))
sms2 = "Nice to meet you " + yourName
for i in sms2:
    print(i, end='')
    time.sleep(0.07)
print()
sms3 = 'Believe you me... I have lived through ages..days,months,years and centuries'
for i in sms3:
    print(i, end='')
    time.sleep(0.07)
print()
yourAge = input('How old are you->')
print(yourAge + '!!!')
time.sleep(2)
print('Looks like you have a lot to learn from me with ' + yourAge)
time.sleep(1)
print('This is great ' + yourName + ' !')
time.sleep(1)
num = int(input('enter 1 for health talk, 2 for diagnosis, 3 for cheerUp and 4 for coronaData ->'))

def healthtalk():
    choice = int(input('1.get a health professional contact info 2.talk to me about your situation'))
    if choice == 1:
        print(yourName + ' Text or call this number: +254741115480 or you can get a video call with billy.gareth on Skype')

    elif choice == 2:
        wati = str(input('type your concern->'))
        awati = wikipedia.summary(wati, sentences=2)
        for edr in awati:
            print(edr, end='')
            time.sleep(.08)
        print()
    else:
        return 'thanks for selecting this'

def tree_to_code(tree, feature_names):
    tree_ = tree.tree_
    #print(tree_)
    feature_name = [
        feature_names[i] if i != _tree.TREE_UNDEFINED else "undefined!"
        for i in tree_.feature
    ]
    #print("def tree({}):".format(", ".join(feature_names)))
    symptoms_present = []
    def recurse(node, depth):
        indent = "  " * depth
        if tree_.feature[node] != _tree.TREE_UNDEFINED:
            name = feature_name[node]
            threshold = tree_.threshold[node]
            print(yourName+ ' have you had any '+ name + " lately?")
            ans = input()
            ans = ans.lower()
            if ans == 'yes':
                val = 1
            else:
                val = 0
            if val <= threshold:
                recurse(tree_.children_left[node], depth + 1)
            else:
                symptoms_present.append(name)
                recurse(tree_.children_right[node], depth + 1)
        else:
            present_disease = print_disease(tree_.value[node])
            print("It could be possible that you have " + present_disease)
            time.sleep(2)
            red_cols = reduced_data.columns 
            symptoms_given = red_cols[reduced_data.loc[present_disease].values[0].nonzero()]
            print(" Well, I suggest this because of " + str(list(symptoms_present)))
            symp = "Kindly check if you also have : " + str(list(symptoms_given))
            for i in symp:
                print(i, end='')
                time.sleep(.1)
            print()
            confidence_level = (1.0*len(symptoms_present))/len(symptoms_given)
            #print("confidence level is " + str(confidence_level))
            swali = yourName + ' are you familiar with ' + present_disease
            swali1 = 'if not, just key in 1 and I will brief you, I hope that will help'
            for words in swali:
                print(words, end='')
                time.sleep(.08)
            print()
            for words in swali1:
                print(words, end='')
                time.sleep(.08)
            print()
            choice = int(input('if you have any history with '+present_disease +' enter2...' + ' if you are familiar with it enter 0'))
            if choice == 1:
                response = ''
                wiki = wikipedia.summary(present_disease, sentences=2)
                responseya = response + ' ' + wiki
                for don in responseya:
                    print(don, end='')
                    time.sleep(.08)
                print()

            if choice == 2:
                getw = input('press any key to get further medical attention and choose health officer to help you with this')
                healthtalk()

            if choice == 0:
                return 0

    recurse(0, 1)

def cheerUp():
    namb = int(input('1.I get to ask you a question'
                     '2.You ask me a question and I never fail!'))
    if namb == 1:
        print('I got lucky so I will ask you a question first ')
        namba = 'Here it comes...get ready!'
        for z in namba:
            print(z, end='')
            time.sleep(0.09)
        print()
        xy = np.random.randint(1, 5, 1)
        if xy == 1:
            mes = 'Who is Albert Einstein?'
            for c in mes:
                print(c, end='')
                time.sleep(.08)
            print()
            anwsero = str(input('enter a description ->'))
            conf = input('key in any value to confirm this ')
            jibu = wikipedia.summary(mes, sentences=2)
            yesy = jibu + '.'
            for ywq in yesy:
                print(ywq, end='')
                time.sleep(.07)
            print()

        elif xy == 2:
            mes1 = 'Who is the largest tech company in terms of market coverage?'
            for c in mes1:
                print(c, end='')
                time.sleep(.08)
            print()
            anwsero1 = str(input('enter a description ->'))
            confa = input('key in any value to confirm this ')
            jibu1 = wikipedia.summary(mes1, sentences=2)
            yesy1 = jibu1 + '.'
            for ywq in yesy1:
                print(ywq, end='')
                time.sleep(.07)
            print()

        elif xy == 3:
            mes2 = 'What is the greatest principle of getting rich?'
            for c in mes2:
                print(c, end='')
                time.sleep(.08)
            print()
            anwsero2 = str(input('enter a description ->'))
            confam = input('key in any value to confirm this ')
            jibu2 = wikipedia.summary(mes2, sentences=2)
            yesy2 = jibu2 + '.'
            for ywq in yesy2:
                print(ywq, end='')
                time.sleep(.07)
            print()

        elif xy == 4:
            mes3 = 'Does planet Mercury have a moon?'
            for c in mes3:
                print(c, end='')
                time.sleep(.08)
            print()
            anwsero3 = str(input('enter a description ->'))
            conf3 = input('key in any value to confirm this ')
            jibu3 = wikipedia.summary(mes3, sentences=2)
            yesy3 = jibu3 + '.'
            for yzsx in yesy3:
                print(yzsx, end='')
                time.sleep(.07)
            print()

        elif xy == 5:
            mes4 = 'Who is the billionaire who has experienced great failure?'
            for c in mes4:
                print(c, end='')
                time.sleep(.08)
            print()
            anwsero4 = str(input('enter a description ->'))
            conf4 = input('key in any value to confirm this ')
            jibu4 = wikipedia.summary(mes4, sentences=2)
            yesy4 = jibu4 + '.'
            for qwy in yesy4:
                print(qwy, end='')
                time.sleep(.07)
            print()

        else:
            return 0



    elif namb == 2:
        print('Ask any questions here...could be out of scope')
        swae = 'I think I am smart enough to answer any questions'
        for se in swae:
            print(se, end='')
            time.sleep(.08)
        print()
        quiz = input('type->')
        val = input('how many sentences should I use to answer your questions e.g 1,2  ')
        response = ''
        wiki = wikipedia.summary(quiz, sentences=val)
        responsep = response + ' ' + wiki
        for ddj in responsep:
            print(ddj, end='')
            time.sleep(.07)
        print()

    else:
        return 0

# here I'll need to scrap data from the web directly, I'll need to develop a cool website using flask framework
def covidData():
    print('This isnt ready yet I will need to scrap data from the official websites')
    state = 'how many people are affected by corona virus'
    gts = wikipedia.summary(state, sentences=4)
    for nult in gts:
        print(nult, end='')
        time.sleep(.05)
    print()

inaload = 'loading...'
for i in inaload:
    print(i, end='')
    time.sleep(.03)
print()
time.sleep(1)
if num == 1:
    healthtalk()
elif num == 2:
    tree_to_code(clf, cols)
elif num == 3:
    cheerUp()
elif num == 4:
    covidData()
else:
    print('wrong entry ' + yourName)

