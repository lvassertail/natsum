#!/bin/bash

/home/olab/lior/envs/miniconda3/envs/fairseq/bin/python train.py \
/home/olab/lior/code/nat_sum/data-bin \
--save-dir models/autoregressive_sum \
--keep-best-checkpoints 2 --save-interval 400 --save-interval-updates 0 \
--tensorboard-logdir models/autoregressive_sum/logs \
--share-decoder-input-output-embed --share-all-embeddings --task summarisation --criterion label_smoothed_cross_entropy --arch transformer_summarisation \
--optimizer adam --adam-betas "(0.9,0.98)" --clip-norm 0.0 --lr 0.0002 --lr-scheduler inverse_sqrt --min-lr 1e-09 \
--warmup-init-lr 1e-07 --label-smoothing 0.1 --dropout 0.3 --weight-decay 0.0001 --log-format simple --log-interval 100 --fp16 \
--max-tokens 35000 \
--max-update 50000 --warmup-updates 4000