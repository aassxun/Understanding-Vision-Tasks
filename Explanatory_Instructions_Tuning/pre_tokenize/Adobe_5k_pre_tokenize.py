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
        self.data_root = "/Dataset/Adobe_5k"  #Path to Adobe_5k Daraset

    def process_item(self, raw_item, training_mode=False, out_flatten=True):
        edit_tasks = []
        Image_A = os.path.join(self.data_root, raw_item["input_img_A"])
        Image_B = os.path.join(self.data_root, raw_item["output_img_B"])
        Image_C = os.path.join(self.data_root, raw_item["output_img_C"])
        Image_D = os.path.join(self.data_root, raw_item["output_img_D"])
        Image_E = os.path.join(self.data_root, raw_item["output_img_E"])
        Image_F = os.path.join(self.data_root, raw_item["output_img_F"])

        edit_task_1 = {
            "conversations": [
                {"from": "human", "value": "<|image|>" + raw_item['Task_Descriptions_from_A_to_B']},
                {"from": "gpt", "value": "<|image|>"}
            ],
            "image": [Image_A, Image_B]
        }
        edit_tasks.append(edit_task_1)

        edit_task_2 = {
            "conversations": [
                {"from": "human", "value": "<|image|>" + raw_item['Task_Descriptions_from_B_to_A']},
                {"from": "gpt", "value": "<|image|>"}
            ],
            "image": [Image_B, Image_A]
        }
        edit_tasks.append(edit_task_2)

        edit_task_3 = {
            "conversations": [
                {"from": "human", "value": "<|image|>" + raw_item['Task_Descriptions_from_A_to_C']},
                {"from": "gpt", "value": "<|image|>"}
            ],
            "image": [Image_A, Image_C]
        }
        edit_tasks.append(edit_task_3)

        edit_task_4 = {
            "conversations": [
                {"from": "human", "value": "<|image|>" + raw_item['Task_Descriptions_from_C_to_A']},
                {"from": "gpt", "value": "<|image|>"}
            ],
            "image": [Image_C, Image_A]
        }
        edit_tasks.append(edit_task_4)

        edit_task_5 = {
            "conversations": [
                {"from": "human", "value": "<|image|>" + raw_item['Task_Descriptions_from_A_to_D']},
                {"from": "gpt", "value": "<|image|>"}
            ],
            "image": [Image_A, Image_D]
        }
        edit_tasks.append(edit_task_5)

        edit_task_6 = {
            "conversations": [
                {"from": "human", "value": "<|image|>" + raw_item['Task_Descriptions_from_D_to_A']},
                {"from": "gpt", "value": "<|image|>"}
            ],
            "image": [Image_D, Image_A]
        }
        edit_tasks.append(edit_task_6)

        edit_task_7 = {
            "conversations": [
                {"from": "human", "value": "<|image|>" + raw_item['Task_Descriptions_from_A_to_E']},
                {"from": "gpt", "value": "<|image|>"}
            ],
            "image": [Image_A, Image_E]
        }
        edit_tasks.append(edit_task_7)

        edit_task_8 = {
            "conversations": [
                {"from": "human", "value": "<|image|>" + raw_item['Task_Descriptions_from_E_to_A']},
                {"from": "gpt", "value": "<|image|>"}
            ],
            "image": [Image_E, Image_A]
        }
        edit_tasks.append(edit_task_8)

        edit_task_9 = {
            "conversations": [
                {"from": "human", "value": "<|image|>" + raw_item['Task_Descriptions_from_A_to_F']},
                {"from": "gpt", "value": "<|image|>"}
            ],
            "image": [Image_A, Image_F]
        }
        edit_tasks.append(edit_task_9)

        edit_task_10 = {
            "conversations": [
                {"from": "human", "value": "<|image|>" + raw_item['Task_Descriptions_from_F_to_A']},
                {"from": "gpt", "value": "<|image|>"}
            ],
            "image": [Image_F, Image_A]
        }
        edit_tasks.append(edit_task_10)

        task_list = []
        for task in edit_tasks:
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

    per_max_len = 10

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
  python -u pre_tokenize/Adobe_5k_pre_tokenize.py \
  --splits=8 \
  --rank=${i} \
  --in_filename /Dataset/Adobe_5k/Adobe_5k_data.json \
  --out_dir ./json/edit_resolution_448/Adobe_5k/ \
  --target_size 448 &> ${i}.log &
done

python -u pre_tokenize/concat_record.py --sub_record_dir ./json/edit_resolution_448/Adobe_5k/ --save_path ./json/edit_resolution_448/Adobe_5k/record.json
'''