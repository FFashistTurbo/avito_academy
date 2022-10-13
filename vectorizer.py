from typing import List
from collections import Counter


class CountVectorizer():
    def __init__(self):
        self._vocabulary = []
        self._feature_names = []

    def fit_transform(self, corpus: List[str]) -> List[List[str]]:
        self._vocabulary = corpus
        features = [text.lower().split() for text in self._vocabulary]
        feature_counters = (
            [Counter(text.lower().split()) for text in self._vocabulary]
        )
        unique_features = []
        for lst in features:
            for i in lst:
                if i not in unique_features:
                    unique_features.append(i)

        self._feature_names = (list(unique_features))
        X = []
        for counts in feature_counters:
            X.append([counts[key] for key in self._feature_names])
        return X

    def get_feature_names(self) -> List[str]:
        return self._feature_names


if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(count_matrix)
