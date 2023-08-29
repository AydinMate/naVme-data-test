import re
import json

class VolumeFinder:
    def __init__(self, jobs):
        if isinstance(jobs, dict):
            self.jobs = [jobs]
        else:
            self.jobs = jobs
        
        for job in self.jobs:
            order_items = job['order_items']

            for item in order_items:
                # If UOM: "LM"
                if item["UOM"] == "LM":
                    description = item["Description"]
                    numbers = [int(num) for num in re.findall(r'\d+', description)]
                    numbers.sort(reverse=True)

                    if len(numbers) > 2:
                        numbers = numbers[:2]
                    
                    width = self.mm_to_m(numbers[0])
                    height = self.mm_to_m(numbers[1])
                    lineal_meters = float(item["Qty Ordered"])  # Convert to float
                    volume = width * height * lineal_meters
                    
                    item["width"] = width
                    item["height"] = height
                    item["lineal_meters"] = lineal_meters
                    item["volume"] = volume

                elif item["UOM"] == "EA" and not item["SKU"][0].isdigit() and item["SKU"] != ("DEL" or "HIT"):
                    description = item["Description"]
                    numbers = [int(num) for num in re.findall(r'\d+', description)]

                    if len(numbers) > 3:
                        concatenated_number = int(str(numbers[0]) + str(numbers[1]))*100
                        numbers = [concatenated_number] + numbers[2:]
                    

                    width = self.mm_to_m(numbers[0])
                    length = self.mm_to_m(numbers[1])
                    height = self.mm_to_m(numbers[2])
                    quantity = float(item["Qty Ordered"])
                    volume = width * length * height * quantity

                    item["width"] = width
                    item["length"] = length
                    item["height"] = height
                    item["volume"] = volume

                else:
                    item["volume"] = 0


    def get_updated_jobs(self):
        return self.jobs
    
    def mm_to_m(self, mm):
        return mm / 1000

    def save_to_file(self, output_filename="updated_jobs.json"):
        with open(output_filename, "w") as outfile:
            json.dump(self.jobs, outfile, indent=4)
        print(f"Updated jobs saved to {output_filename}")

