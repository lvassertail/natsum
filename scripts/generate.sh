#!/bin/bash

/home/olab/lior/envs/miniconda3/envs/fairseq/bin/python /home/olab/lior/code/nat_sum/fairseq_cli/generate.py \
/home/olab/lior/code/nat_sum/data-bin \
--gen-subset test --path /home/olab/lior/code/nat_sum/models/autoregressive_sum/checkpoint_best.pt \
--results-path /home/olab/lior/code/nat_sum/models/autoregressive_sum \
--task summarisation --beam 5 --remove-bpe --max-tokens 15000 --calc-rouge
