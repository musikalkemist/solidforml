from abc import ABC, abstractmethod


################# LSP violation #############################
# class Extractor(ABC):
#
#     @abstractmethod
#     def extract(self, data):
#         pass
#
#
# class MelSpectrogramExtractor(Extractor):
#
#     def extract(self, data):
#         print("Extracted spectrogram")
#
#
# class MFCCExtractor(Extractor):
#
#     def extract(self, data, num_mfccs):
#         print("Extracted MFCC")
#
#
# if __name__ == "__main__":
#     dummy_data = [1, 2, 3]
#     mfcc_extractor = MFCCExtractor()
#     mfcc_extractor.extract(dummy_data, 10)
################# LSP violation #############################


class Extractor(ABC):

    @abstractmethod
    def extract(self, data):
        pass


class MelSpectrogramExtractor(Extractor):

    def __init__(self, num_mels):
        self.num_mfccs = num_mels

    def extract(self, data):
        print("Extracted spectrogram")


class MFCCExtractor(Extractor):

    def __init__(self, num_mfccs):
        self.num_mfccs = num_mfccs

    def extract(self, data):
        print("Extracted MFCC")


if __name__ == "__main__":
    dummy_data = [1, 2, 3]
    mfcc_extractor = MFCCExtractor(13)
    mfcc_extractor.extract(dummy_data)