import os
from tqdm import tqdm
import json

first_bits = {}

outs = os.listdir("./outs")

for out in tqdm(outs):
    with open("./outs/" + out) as file:
        bit = ""

        for _ in range(10_000):
            bit += file.read(1)

        first_bits[out] = bit

sames = {}

for ref_key, ref_value in first_bits.items():

    for k, v in sames.items():
        if v["val"] == ref_value:
            sames[k]["sames"].append(ref_key)

    else:
        sames[ref_key] = {"val": ref_value, "sames": []}

new_out = {}

for k, v in sames.items():
    if len(v["sames"]) > 0:
        new_out[k] = v["sames"]

with open("sames_out.json", "w") as file:
    json_object = json.dumps(new_out, indent=4)
    file.write(json_object)
