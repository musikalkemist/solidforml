from abc import abstractmethod, ABC


################# OCP violation #############################
# class Extractor:
#
#     def extract_spectrogram(self, data):
#         print("Extracted spectrogram")
#
#     def extract_mfcc(self, data):
#         print("Extracted MFCCs")
#
#     def extract_mel_spectrogram(self, data):
#         print("Extracted mel spectrogram")
#
#
# class DLPipeline:
#
#     def __init__(self, extractor, feature_type):
#         self.extractor = extractor
#         self.feature_type = feature_type
#
#     def run(self, data):
#         print("Running DL pipeline")
#         features = self._extract(data)
#         # Implementation of DL steps go here
#
#     def _extract(self, data):
#         if self.feature_type == "spectrogram":
#             self.extractor.extract_spectrogram(data)
#         elif self.feature_type == "mfcc":
#             self.extractor.extract_mfcc(data)
#         elif self.feature_type == "melspectrogram":
#             self.extractor.extract_melspectrogram(data)
#
#
# if __name__ == "__main__":
#     data = [1, 2, 3]
#     extractor = Extractor()
#     dl_pipeline = DLPipeline(extractor, "spectrogram")
#     dl_pipeline.run(data)
################# OCP violation #############################


class Extractor(ABC):

    @abstractmethod
    def extract(self, data):
        pass


class SpectrogramExtractor(Extractor):

    def extract(self, data):
        print("Extracted spectrogram")


class MFCCExtractor(Extractor):

    def extract(self, data):
        print("Extracted MFCC")


class MelSpectrogramExtractor(Extractor):

    def extract(self, data):
        print("Extracted mel spectrogram")


class DLPipeline:

    def __init__(self, extractor):
        self.extractor = extractor

    def run(self, data):
        print("Running DL pipeline")
        features = self._extract(data)
        # Implementation of DL steps go here

    def _extract(self, data):
        self.extractor.extract(data)


if __name__ == "__main__":
    data = [1, 2, 3]
    extractor = SpectrogramExtractor()
    dl_pipeline = DLPipeline(extractor)
    dl_pipeline.run(data)
