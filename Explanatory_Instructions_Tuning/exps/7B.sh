#!/bin/bash

lr=2e-5
min_lr=2e-6
wd=0.1
dropout=0.05
z_loss_weight=1e-5

data_config=configs/data/sample.yaml

exp_name=7B_task_A_to_B_lr${lr}_min_lr${min_lr}
mkdir -p output/"$exp_name"


# python -u finetune_solver.py \
# python finetune_solver.py
torchrun --nproc_per_node=8 --master_port=25641 finetune_solver.py \
--model_size 7B \
--batch_size 4 \
--accum_iter 1 \
--epochs 3 \
--warmup_epochs 0.01 \
--lr ${lr} \
--min_lr ${min_lr} \
--wd ${wd} \
--clip_grad 4 \
--data_config $data_config \
--cache_ann_on_disk \
--num_workers 8 \
--output_dir output/"$exp_name" \
--save_iteration_interval 4000 \
--checkpointing \
--max_seq_len 2048 \
--unmask_image_logits \
--dropout ${dropout} \
--z_loss_weight ${z_loss_weight} \
2>&1 | tee -a output/"$exp_name"/output.log

echo "exp name: $exp_name"
