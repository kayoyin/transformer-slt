"""Module defining encoders."""
from onmt.encoders.encoder import EncoderBase
from onmt.encoders.transformer import TransformerEncoder
from onmt.encoders.rnn_encoder import RNNEncoder
from onmt.encoders.mean_encoder import MeanEncoder


str2enc = {"rnn": RNNEncoder, "brnn": RNNEncoder,
           "transformer": TransformerEncoder, "mean": MeanEncoder}

__all__ = ["EncoderBase", "TransformerEncoder", "RNNEncoder",
           "MeanEncoder", "str2enc"]
