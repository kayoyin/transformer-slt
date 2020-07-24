# transformer-slt
This repository gathers data and code supporting the experiments in the paper [Sign Language Translation with Transformers](https://arxiv.org/abs/2004.00588).

## Installation
This code is based on [OpenNMT](https://github.com/OpenNMT/OpenNMT-py) and requires all of its dependencies. Additional requirements are [NLTK](https://www.nltk.org/) for NMT evaluation metrics.

The recommended way to install is shown below:
```
# create a new virtual environment
virtualenv --python=python3 venv
source venv/bin/activate

# clone the repo
git clone https://github.com/kayoyin/transformer-slt.git
cd transformer-slt

# install python dependencies
pip install -r requirements.txt

# install OpenNMT-py
python setup.py install

```

## Sample Usage

### Data processing

```
onmt_preprocess -train_src data/phoenix2014T.train.gloss -train_tgt data/phoenix2014T.train.de -valid_src data/phoenix2014T.dev.gloss -valid_tgt data/phoenix2014T.dev.de -save_data data/dgs -lower 
```

### Training
```
python  train.py -data data/dgs -save_model model -keep_checkpoint 1 \
          -layers 2 -rnn_size 512 -word_vec_size 512 -transformer_ff 2048 -heads 8  \
          -encoder_type transformer -decoder_type transformer -position_encoding \
          -max_generator_batches 2 -dropout 0.1 \
          -early_stopping 3 -early_stopping_criteria accuracy ppl \
          -batch_size 2048 -accum_count 3 -batch_type tokens -normalization tokens \
          -optim adam -adam_beta2 0.998 -decay_method noam -warmup_steps 3000 -learning_rate 0.5 \
          -max_grad_norm 0 -param_init 0  -param_init_glorot \
          -label_smoothing 0.1 -valid_steps 100 -save_checkpoint_steps 100 \
          -world_size 1 -gpu_ranks 0
```

### Inference
```
python translate.py -model model [model2 model3 ...] -src data/phoenix2014T.test.gloss -output pred.txt -gpu 0 -replace_unk -beam_size 4
```

### Scoring
```
# BLEU-1,2,3,4
python tools/bleu.py 1 pred.txt data/phoenix2014T.test.de
python tools/bleu.py 2 pred.txt data/phoenix2014T.test.de
python tools/bleu.py 3 pred.txt data/phoenix2014T.test.de
python tools/bleu.py 4 pred.txt data/phoenix2014T.test.de

# ROUGE
python tools/rouge.py pred.txt data/phoenix2014T.test.de

# METEOR
python tools/meteor.py pred.txt data/phoenix2014T.test.de
```

# To dos:
* Add configurations & steps to recreate paper results

# Reference
Please cite the paper below if you found the resources in this repository useful:
```
@article{yin2020sign,
  title={Sign Language Translation with Transformers},
  author={Kayo Yin},
  journal={arXiv preprint arXiv:2004.00588},
  year={2020}
} 
```
