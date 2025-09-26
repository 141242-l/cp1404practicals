import random

def evaluate_score(score):
    if score >= 90: return "Excellent"
    elif score >= 50: return "Passable"
    else: return "Bad"

def main():
    num_scores = int(input("Number of scores: "))