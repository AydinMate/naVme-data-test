import json

data = {
                "SKU": "CWED19018",
                "Description": "EDWARDIAN CRAFTWOOD PRIMED 190 X 18",
                "UOM": "LM",
                "Special Order": "N",
                "Qty Ordered": "145.8",
                "Qty This Invoice": "145.8"
            }

stringified_data = json.dumps(data)

print(stringified_data)
