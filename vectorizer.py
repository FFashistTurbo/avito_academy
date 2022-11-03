from typing import List
from collections import Counter


class CountVectorizer():
    """class for vectorize list of strings
    """
    def __init__(self):
        self._vocabulary = []
        self._feature_names = []

    def fit_transform(self, corpus: List[str]) -> List[List[int]]:
        """transform string to vector method

        Args:
            corpus (List[str]): input list of strings to vectorize

        Returns:
            List[List[int]]: list of vectors of int
        """
        self._vocabulary = corpus
        features = [text.lower().split() for text in self._vocabulary]
        feature_counters = (
            [Counter(f) for f in features]
        )
        unique_features = []
        for lst in features:
            for i in lst:
                if i not in unique_features:
                    unique_features.append(i)

        self._feature_names = unique_features
        count_matrix = []
        for counts in feature_counters:
            count_matrix.append([counts[key] for key in self._feature_names])
        return count_matrix

    def get_feature_names(self) -> List[str]:
        """getter of feature names

        Returns:
            List[str]: list to output
        """
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
