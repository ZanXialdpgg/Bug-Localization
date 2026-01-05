# Bug-Localization

This is my implementation for this paper https://ieeexplore.ieee.org/document/9719906 "An Imbalanced Deep Learning Model for Bug Localization". I've working on AspectJ, SWT and Tomcat dataset only due to limited computing resource. But the training pipeline, evaluate metric is complete for anyone to replicating the rest of the dataset.


This work proposes a deep neural network model to improve automated bug localization by tackling two major challenges: the lexical gap between natural language bug reports and source code, and the imbalance of training datasets.

The model integrates a dual-feature extraction pipeline that calculates Lexical Similarity using TF-IDF vectorization and Semantic Similarity via GloVe word embeddings and cosine similarity. 
To capture historical context, we engineered features including Code Change History (H) based on report timelines, Bug Fixing Frequency (F), and Similar Bug Report (R) scores.
The data was processed through temporal sorting and K-Fold cross-validation, and features were normalized using MinMaxScaler from Scikit-learn to ensure consistent model performance.

The system was evaluated using Mean Average Precision (MAP) and Top-k accuracy metrics to measure ranking performance

