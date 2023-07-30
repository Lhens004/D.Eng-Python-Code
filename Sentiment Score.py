# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 15:43:23 2023

@author: levih
"""

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# nltk.download('vader_lexicon')  # Uncomment this line if you haven't downloaded the VADER lexicon

def analyze_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    sentiment_score = sia.polarity_scores(text)['compound']
    
    # Transform sentiment_score to a 1-5 scale
    score = (sentiment_score + 1) * 2 + 1
    
    # Custom adjustments based on specific phrases
    score += custom_adjustment(text)

    # Convert score to integer between 1 and 5
    score = max(1, min(5, int(round(score))))
    
    return score

def analyze_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    sentiment_score = sia.polarity_scores(text)['compound']
    
    # Adjust sentiment score with custom logic
    sentiment_score += custom_adjustment(text) * 0.5  # Adjust the weighting factor as needed
    
    # Transform sentiment_score to a 1-5 scale
    score = (sentiment_score + 1) * 2 + 1

    # Convert score to integer between 1 and 5
    score = max(1, min(5, int(round(score))))
    
    return score

def custom_adjustment(text):
    adjustments = 0

    # Positive phrases
    positive_phrases = [
        "technologies are mature", 
        "design is stable", 
        "production processes have been demonstrated", 
        "performing well",
        "Demonstrated all critical technologies in a relevant environment",
        "Demonstrated all critical technologies in a realistic environment",
        "Completed a system-level preliminary design review",
        "Product design is stable",
        "Design Review",
        "Released at least 90 percent of design drawings",
        "Tested a system-level integrated prototype",
        "Manufacturing processes are mature",
        "Production Started",
        "Demonstrated critical processes on a pilot production line",
        "Test a production-representative prototype in its intended environment",
        "improvement", "recommendations", "modernization", "emphasis", "aim"
    ]
    adjustments += sum([text.count(phrase) for phrase in positive_phrases])

    # Negative phrases
    negative_phrases = [
        "delayed",
        "delay"
        "performance issues", 
        "increased cost",        
        "Failed to demonstrate critical technologies in a relevant environment",
        "Failed to demonstrate critical technologies in a realistic environment",
        "Failed a system-level preliminary design review",
        "Product design is unstable",
        "Failed Design Review",
        "Released less than 90 percent of design drawings",
        "Failed to test a system-level integrated prototype",
        "Manufacturing processes are immature",
        "Production Delayed",
        "Failed to demonstrate critical processes on a pilot production line",
        "Failed to test a production-representative prototype in its intended environment",
        "Restructured",
        "replanned",
        "none of",
        "delays", "challenges", "lack", "risks", "limited", "adoption", "struggles", "threaten", "hinder",
        
        
    ]
    adjustments -= sum([text.count(phrase) for phrase in negative_phrases])

    return adjustments

# Prompt the user for an article text input
article_text = input("Please paste the article text here:\n")

score = analyze_sentiment(article_text)
print(f"The sentiment score is: {score}")
