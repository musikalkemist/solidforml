##################### Dependency Inversion Violation ####################
# class TensorFlowEvaluator:
#
#     def evaluate(self):
#         print("Evaluating with TensorFlow.")
#
#
# class MLPipeline:
#
#     def __init__(self):
#         self.evaluator = TensorFlowEvaluator()
#
#     def evaluate(self):
#         self.evaluator.evaluate()
#
#
# if __name__ == "__main__":
#     ml_pipeline = MLPipeline()
#     ml_pipeline.evaluate()
##################### Dependency Inversion Violation ####################


from abc import ABC, abstractmethod


class Evaluator(ABC):

    @abstractmethod
    def evaluate(self):
        pass


class TensorFlowEvaluator(Evaluator):

    def evaluate(self):
        print("Evaluating with TensorFlow.")


class PyTorchEvaluator(Evaluator):

    def evaluate(self):
        print("Evaluating with PyTorch.")


class MLPipeline:

    def __init__(self, evaluator: Evaluator):
        self.evaluator = evaluator

    def evaluate(self):
        self.evaluator.evaluate()


if __name__ == "__main__":
    evaluator = PyTorchEvaluator()
    ml_pipeline = MLPipeline(evaluator)
    ml_pipeline.evaluate()