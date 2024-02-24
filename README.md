# ml-group45-sp2024
CS 4641 Project 


<img width="1287" alt="Screenshot 2024-02-23 at 9 24 15 PM" src="https://github.com/vinwu2/ml-group45-sp2024/assets/161073357/03102013-d2ae-4660-8e92-d79c04b277ae">

Group 45

Github repo link:
Github Page:
Video link:

[ WORD COUNT OF SECTIONS 1-4 < 500 ]

1: Introduction / Background: Provide an introduction of your topic and literature review of related work. Briefly explain your dataset and its features, and provide a link to the dataset if possible.

Literature Review
Dataset Description
Dataset Link (if applicable)

2: Problem Definition: Identify a problem and motivate the need for a solution.

Problem
Motivation

3: Methods: Present proposed solutions including specific data processing methods and machine learning algorithms, and elaborate on why you think each will be effective. It is recommended to identify specific functions/classes in existing packages and libraries (i.e. scikit-learn) rather than coding the algorithms from scratch.

3+ Data Preprocessing Methods Identified
3+ ML Algorithms/Models Identified
CS 7641: Unsupervised and Supervised Learning Methods Identified
CS 4641: Supervised Learning Methods Identified

4: Potential Results and Discussion: Identify several quantitative metrics you plan to use for the project (i.e. ML Metrics). Present goals in terms of these metrics, and state any expected results.

3+ Quantitative Metrics
Project Goals
Expected Results

5: References: Cite relevant papers and articles utilizing the IEEE format. All references in this section must have a matching in-text citation in the body of your proposal text.

3+ References (preferably peer reviewed)
1+ In-Text Citation Per Reference



Gantt Chart: https://docs.google.com/spreadsheets/d/10gW2V_CWf_yx3DgqnAJxEo57-BKHlxNomnaKp1s6kBw/edit?usp=sharing

Contribution Table:

Name
Proposal Contributions
Yolanda Li
Sections 1 and 2
Rohit George
Sections 1 and 2
Amanpreet Puri
Section 3 
Rohan Aluri
Section 4 and Video 
Vincent Wu
Github Repository


Section 1: Introduction
Several studies have experimented with using machine learning to make more accurate NBA predictions. [2] uses a probabilistic model with data on each player’s history to calculate expected points per possession. However, most studies use team-level statistics. [3] was able to achieve an overall 70% accuracy with linear regression, logistic regression, support vector machines, and artificial neural networks using team-level data, with models that combined predictions from multiple sources producing the best results. [1] combined team-level statistics with clustering analysis of players based on playing style to achieve over 70% prediction accuracy. Ensemble models were the best [2].

Dataset information:
Home vs away data, points per game, rebounds per game, shot percentage, assists, game records

Player data

Team records

NBA injuries

Section 2: Problem and Motivation
Uncertainty involved in NBA games makes betting outcomes difficult to predict. Games are influenced by many factors: player performance, injuries, location, psychological state, etc., which are often hard to reliably predict.

Our main motivation is to enhance the accuracy of NBA betting predictions. Using historical data and machine learning models, we can predict game outcomes with greater accuracy.

Section 3: Methods 
Data Preprocessing Methods:  
from sklearn.impute import SimpleImputer; 
Beneficial for historical NBA data with gaps
Approach to handle missing values in datasets
from sklearn.preprocessing import StandardScaler 
Normalize diverse statistical metrics
Ensures uniformity in feature scale
from sklearn.covariance import EllipticEnvelope 
Identify and manage outliers 
Refining dataset reliability
ML Algorithm Models:  
Multiple Bayesian Regression 
 Measures the relationship between subsets of features and a target criterion using regression.
Assesses how specific elements, like individual player contributions, influence broader outcomes such as team success.
Able to evaluate different subsets of features and combine them for multi-layered models


LinearSVC or LinearSVM 
Creates a hyperplane in an N-dimensional space to maximize the distance between different categories.
Enables mapping a set of features to another set or multiple targets, such as calculating a team's win percentage and other game outcomes.
Supervised learning method: relies on a training set with pre-known outcomes for learning and predictions.


Maximum Entropy Model 
Evaluates input data based on the weight and informativeness of selected features.
Utilizes feature functions to map inputs to classes and assesses the significance of these inputs.
Approach starts with minimal bias and progressively incorporates information from the feature data.

Section 4: Potential Results and Discussion
We can analyze individual and team efficiency indices for player and head-to-head evaluation. Statistics that our model can evaluate include: points, assists, moneyline, total over/under, etc. Our quantitative metrics and goals are as follows: 
Balanced Accuracy: accomplish our goal of determining a fair assessment of outcomes in situations with high odds (such as an underdog winning). 
Brier Score: assign probabilities compared to the observed frequencies of a team winning/losing with confidence estimates.
Mean Squared Error: analyze how well the model performs in unlikely scenarios. Errors are considered with a larger weight which can be helpful as taking risks can be costly.
Our expected result is to develop a model that accurately predicts profitable betting lines through exploiting discrepancies between bookmakers' odds and true probabilities of outcomes.

Section 5: References

[1] C. Osken and C. Onay, “Predicting the winning team in basketball: A novel approach,” Heliyon, vol. 8, no. 12, p. e12189, Dec. 2022, doi: https://doi.org/10.1016/j.heliyon.2022.e12189. 

[2] J. Kuehn, “Accounting for Complementary Skill Sets: Evaluating Individual Marginal Value to a Team in the National Basketball Association,” Economic Inquiry, vol. 55, no. 3, pp. 1556–1578, Apr. 2017, doi: https://doi.org/10.1111/ecin.12451. 

[3] M. Beckler, H. Wang, and M. Papamichael, “NBA Oracle,” 2013. Available: https://www.mbeckler.org/coursework/2008-2009/10701_report.pdf 


Link to YouTube Video: https://youtu.be/iBBLTxz9h34

