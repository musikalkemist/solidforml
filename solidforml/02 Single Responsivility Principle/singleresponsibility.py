class DLModel:

    def train(self, features):
        # here goes training code
        print("Model has been trained")
        return features


class Preprocessor:

    def preprocess(self, features):
        # here goes preprocessing code
        print("Features have been preprocessed")


class DlEvaluator:

    def evaluate(self, model):
        # here goes evaluation code
        print("Model has been evaluated")



if __name__ == "__main__":
    features = [
        [0, 1, 2],
        [1, 2, 3]
    ]
    model = DLModel()
    preprocessor = Preprocessor()
    evaluator = DlEvaluator()

    features = preprocessor.preprocess(features)
    model.train(features)
    evaluator.evaluate(model)