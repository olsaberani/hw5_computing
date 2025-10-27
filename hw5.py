###########################################

#
# 1. In this exercise we will make a "Patient" class
#
# The Patient class should store the state of
# a patient in our hospital system.
#
#
# 1.1)
# Create a class called "Patient".
# The constructor should have two parameters
# (in addition to self, of course):
#
# 1. name (str)
# 2. symptoms (list of str)
#
# the parameters should be stored as attributes
# called "name" and "symptoms" respectively

class Patient:
    def __init__(self, name: str, symptoms: list[str]):
        self.name = name
        self.symptoms = symptoms
        
p1 = Patient("Olta Recica", ["fever", "cough"])
print(p1.name)        
print(p1.symptoms)    


#
# 1.2)
# Create a method called "add_test"
# which takes two paramters:
# 1. the name of the test (str)
# 2. the results of the test (bool)
#
# This information should be stored somehow.

class Patient:
    def __init__(self, name: str, symptoms: list[str]):
        self.name = name
        self.symptoms = symptoms
        self.tests = {}  # store test name -> result (True/False)

    def add_test(self, test_name: str, result: bool):
        self.tests[test_name] = result

p1 = Patient("Olta Recica", ["fever", "cough"])
p1.add_test("COVID", True)
p1.add_test("Flu", False)

print(p1.tests)

#
# 1.3)
# Create a method called has_covid()
# which takes no parameters.
#
# "has_covid" returns a float, between 0.0
# and 1.0, which represents the probability
# of the patient to have Covid-19
#
# The probability should work as follows:
#
# 1. If the user has had the test "covid"
#    then it should return .99 if the test
#    is True and 0.01 if the test is False
# 2. Otherwise, probability starts at 0.05
#    and ncreases by 0.1 for each of the
#    following symptoms:
#    ['fever', 'cough', 'anosmia']

class Patient:
    def __init__(self, name: str, symptoms: list[str]):
        self.name = name
        self.symptoms = symptoms
        self.tests = {}

    def add_test(self, test_name: str, result: bool):
        self.tests[test_name.lower()] = result

    def has_covid(self) -> float:
        
        if "covid" in self.tests:
            return 0.99 if self.tests["covid"] else 0.01
       
        probability = 0.05
        covid_symptoms = ['fever', 'cough', 'anosmia']
        for symptom in covid_symptoms:
            if symptom in self.symptoms:
                probability += 0.1
        
    
        return min(probability, 1.0)

p1 = Patient("Olta Recica", ["fever", "cough"])
p1.add_test("COVID", True)
print(p1.has_covid())  # 0.99

p2 = Patient("Olsa Berani", ["fever", "anosmia"])
print(p2.has_covid())  # 0.25  (0.05 + 0.1 + 0.1)

######################

# 2. In this exercise you will make an English Deck class made of Card classes
# 
# the Card class should represent each of the cards
#
# the Deck class should represent the collection of cards and actions on them

# 2.1) Create a Card class called "Card".
# The constructor (__init__ ) should have two parameters the "suit" and the "value" and the suit of the card.
# The class should store both as attributes.

class Card:
    def __init__(self, suit: str, value: str):
        self.suit = suit
        self.value = value

c1 = Card("Hearts", "Ace")
print(c1.suit)   
print(c1.value) 

# 2.2) Create a Deck class called "Deck".
# The constructor will create an English Deck (suits: Hearts, Diamonds, Clubs, Spades and values: A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K). It will create a list of cards that contain each of the existing cards in an English Deck.
# Create a method called "shuffle" that shuffles the cards randomly. 
# Create a method called "draw" that will draw a single card and print the suit and value. When a card is drawn, the card should be removed from the deck.

import random

class Card:
    def __init__(self, suit: str, value: str):
        self.suit = suit
        self.value = value


class Deck:
    def __init__(self):
        suits = ["hearts", "diamonds", "clubs", "spades"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = [Card(suit, value) for suit in suits for value in values]

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        if len(self.cards) == 0:
            print("no cards left in the deck")
            return None
        card = self.cards.pop()
        print(f"{card.value} of {card.suit}")
        return card

deck = Deck()
deck.shuffle()
deck.draw()  
print(len(deck.cards))  


###################

# 3. In this exercise you will create an interface that will serve as template 
# for different figures to compute their perimeter and surface. 

# 3.1Create an abstract class (interface) called "PlaneFigure" with two abstract methods:
# compute_perimeter() that will implement the formula to compute the perimiter of the plane figure.
# compute_surface() that will implement the formula to compute the surface of the plane figure.

from abc import ABC, abstractmethod

class PlaneFigure(ABC):
    
    @abstractmethod
    def compute_perimeter(self):
        pass

    @abstractmethod
    def compute_surface(self):
        pass

# 3.2 Create a child class called "Triangle" that inherits from "PlaneFigure" and has as parameters in the constructor "base", "c1", "c2", "h". ("base" being the base, "c1" and "c2" the other two sides of the triangle and "h" the height). Implement the abstract methods with the formula of the triangle.

import math

class Triangle(PlaneFigure):
    def __init__(self, base: float, c1: float, c2: float, h: float):
        self.base = base
        self.c1 = c1
        self.c2 = c2
        self.h = h

    def compute_perimeter(self) -> float:
        return self.base + self.c1 + self.c2

    def compute_surface(self) -> float:
        return 0.5 * self.base * self.h

t = Triangle(base=5, c1=4, c2=3, h=2.5)
print("Perimeter:", t.compute_perimeter())  
print("Surface:", t.compute_surface())      

# 3.3 Create a child class called "Rectangle" that inherits from "PlaneFigure" and has as parameters in the constructor "a", "b" (sides of the rectangle). Implement the abstract methods with the formula of the rectangle.

class Rectangle(PlaneFigure):
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def compute_perimeter(self) -> float:
        return 2 * (self.a + self.b)

    def compute_surface(self) -> float:
        return self.a * self.b

r = Rectangle(4, 6)
print("Perimeter:", r.compute_perimeter())  
print("Surface:", r.compute_surface())      

# 3.3 Create a child class called "Circle" that inherits from "PlaneFigure" and has as parameters in the constructor "radius" (radius of the circle). Implement the abstract methods with the formula of the circle.

import math

class Circle(PlaneFigure):
    def __init__(self, radius: float):
        self.radius = radius

    def compute_perimeter(self) -> float:
        return 2 * math.pi * self.radius

    def compute_surface(self) -> float:
        return math.pi * (self.radius ** 2)

c = Circle(3)
print("Perimeter:", c.compute_perimeter())  
print("Surface:", c.compute_surface())      

###########################################
#Question 6: Data Analysis

#a) test 
from src.data_loader import DataLoader

loader = DataLoader("data/sample_diabetes_mellitus_data.csv")
train_df, test_df = loader.split_data()

print("Train shape:", train_df.shape)
print("Test shape:", test_df.shape)

#b) test 
from src.data_loader import DataLoader
from src.preprocessor_dropna import DropNaPreprocessor

loader = DataLoader("data/sample_diabetes_mellitus_data.csv")
train_df, test_df = loader.split_data()

dropper = DropNaPreprocessor()
train_clean = dropper.process(train_df)
test_clean = dropper.process(test_df)

print("Original train shape:", train_df.shape)
print("Cleaned train shape:", train_clean.shape)


#c) test
from src.preprocessor_fillmean import FillMeanPreprocessor

filler = FillMeanPreprocessor()
train_final = filler.process(train_clean)
test_final = filler.process(test_clean)

print("before filling:", train_clean.isna().sum()[["height", "weight"]])
print("after filling:", train_final.isna().sum()[["height", "weight"]])

#d) test 
from src.features import BMIFeature, AgeGroupFeature

bmi_feature = BMIFeature()
age_feature = AgeGroupFeature()

train_features = bmi_feature.transform(train_final)
train_features = age_feature.transform(train_features)

print(train_features[["height", "weight", "BMI", "age", "age_group"]].head())

#e) and f) model class test
from src.model import Model

feature_cols = ["BMI", "age"]
target_col = "diabetes"

model = Model(feature_cols=feature_cols, target_col=target_col, max_iter=1000)
model.train(train_features)

test_final["predictions"] = model.predict(test_final)
print(test_final[["BMI", "age", "predictions"]].head())
