import os
import sys

sys.path.append(os.path.abspath(__file__).rsplit("/", 2)[0])

from argparse import ArgumentParser
import json
import math
import pickle
import random

from data.convertsation import Conversation
from data.item_processor import FlexARItemProcessor


class ItemProcessor(FlexARItemProcessor):
    def __init__(
        self,
        tokenizer="../Lumina-mGPT-7B-768-tokenizer",
        conv_template=Conversation,
        target_size=512,
    ):
        super().__init__(tokenizer, conv_template, target_size)
        print(self.crop_size_list)
        self.data_root = "/Dataset/SEED/multi_turn_editing/data"  #Path to SEED Dataset

    def process_item(self, raw_item, training_mode=False, out_flatten=True):
        def ensure_period_at_end(text):
            if not text.endswith('.'):
                return text + '.'
            return text

        Image_Paths = [os.path.join(self.data_root, raw_item[f"edit_image_{i+1}"]) for i in range((len(raw_item) - 1)//3)]
        Image_Paths.insert(0, os.path.join(self.data_root, raw_item["source_image"]))

        instructions = [ensure_period_at_end(raw_item[f"instruction_{i+1}"]) for i in range((len(raw_item) - 1) // 3)]
        inverse_instructions = [ensure_period_at_end(raw_item[f"inverse_instruction_{i+1}"]) for i in range((len(raw_item) - 1) // 3)]
        
        edit_tasks = []

        for i in range(len(instructions)):
            for j in range(i, len(instructions)):
                combined_instruction = ' '.join(instructions[i:j+1])
                source_image = Image_Paths[i]
                target_image = Image_Paths[j+1]
                edit_task = {
                    "conversations": [
                        {"from": "human", "value": "<|image|>" + combined_instruction},
                        {"from": "gpt", "value": "<|image|>"}
                    ],
                    "image": [source_image, target_image]
                }
                edit_tasks.append(edit_task)

        for i in range(len(inverse_instructions)):
            for j in range(i, len(inverse_instructions)):
                combined_inverse_instruction = ' '.join(inverse_instructions[j:i-1:-1] if i > 0 else inverse_instructions[j::-1])
                source_image = Image_Paths[-(j+2)]
                target_image = Image_Paths[-(i+1)]
                edit_task = {
                    "conversations": [
                        {"from": "human", "value": "<|image|>" + combined_inverse_instruction},
                        {"from": "gpt", "value": "<|image|>"}
                    ],
                    "image": [source_image, target_image]
                }
                edit_tasks.append(edit_task)

        task_list = []
        for task in edit_tasks:
            # print(task)
            result = super(ItemProcessor, self).process_item(task, training_mode, out_flatten)
            task_list.append(result)

        return task_list

if __name__ == "__main__":

    parser = ArgumentParser()
    parser.add_argument(
        "--splits",
        type=int,
        default=8,
    )
    parser.add_argument(
        "--rank",
        type=int,
        default=0,
    )
    parser.add_argument(
        "--in_filename",
        type=str,
    )
    parser.add_argument(
        "--out_dir",
        type=str,
    )
    parser.add_argument("--target_size", type=int, default=512)
    args = parser.parse_args()

    item_processor = ItemProcessor(target_size=args.target_size)

    with open(args.in_filename) as f:
        ori_contents = json.load(f)

    per_max_len = 0
    for i in range(len(ori_contents)):
        per_max_len = max(per_max_len, (len(ori_contents[i]) - 1) // 3)
    print(per_max_len)
    per_max_len = (per_max_len + 1) * per_max_len
    print(per_max_len)

    num = len(ori_contents)

    splits = args.splits
    rank = args.rank
    output_dir = args.out_dir
    save_dir = os.path.join(output_dir, "files")
    os.makedirs(save_dir, exist_ok=True)

    num_per_rank = math.ceil(num / splits)

    try:
        with open(os.path.join(output_dir, f"{rank}-of-{splits}-progress.txt"), "r") as f:
            start_idx = int(f.read()) + 1
        print(f"resume from {start_idx}")
    except:
        start_idx = num_per_rank * rank
        print(f"start from {start_idx}")

    end_idx = min(num_per_rank * (rank + 1), len(ori_contents))
    for i in range(start_idx, end_idx):
        if i % 10 == 0:
            print(f"{i}/{end_idx}")

        records = []
        try:
            processed_items = item_processor.process_item(ori_contents[i], training_mode=True)

            for j, (tokens, labels) in enumerate(processed_items):
                pkl_path = os.path.join(save_dir, f"{i}_{j}.pkl")
                new_item = {"token": tokens, "label": labels, "id": i * per_max_len + j}
                with open(pkl_path, "wb") as f:
                    pickle.dump(new_item, f)
                record = {"file": pkl_path, "len": len(tokens), "id": i * per_max_len + j}
                records.append(record)

        except Exception as e:
            from traceback import format_exc

            print(f"item {i} error: \n{ori_contents[i]}")
            print(format_exc())

        if records:
            with open(os.path.join(output_dir, f"{rank}-of-{splits}-record.jsonl"), "a") as f:
                for record in records:
                    f.write(json.dumps(record) + "\n")

        with open(os.path.join(output_dir, f"{rank}-of-{splits}-progress.txt"), "w") as f:
            if i == end_idx - 1:
                f.write("finished")
            else:
                f.write(f"{i}")


'''
for i in {0..7}
do
  export CUDA_VISIBLE_DEVICES=${i}
  python -u pre_tokenize/seed_multi_turn_pre_tokenize.py \
  --splits=8 \
  --rank=${i} \
  --in_filename /Dataset/seed_multi_turn_editing_data.json \
  --out_dir ./json/edit_resolution_448/SEED/Multi_Turn \
  --target_size 448 &> ${i}.log &
done

python -u pre_tokenize/concat_record.py --sub_record_dir ./json/edit_resolution_448/SEED/Multi_Turn/ --save_path ./json/edit_resolution_448/SEED/Multi_Turn/record.json
'''

