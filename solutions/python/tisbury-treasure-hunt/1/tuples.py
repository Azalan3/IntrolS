def get_coordinate(record):
    
    return record[1]
print (get_coordinate(('Scrimshawed Whale Tooth', '2A')))

def convert_coordinate(coordinate):
    return (coordinate[0], coordinate[1])
print (convert_coordinate("2A"))

def compare_records(azara_record, rui_record):
    if tuple(azara_record[1]) == rui_record[1]:
        return True
    else:
        return False
print (compare_records(('Brass Spyglass', '4B'), ('Seaside Cottages', ('1', 'C'), 'blue')))
print (compare_records(('Model Ship in Large Bottle', '8A'), ('Harbor Managers Office', ('8', 'A'), 'purple')))

def create_record(azara_record, rui_record):
    if tuple(azara_record[1]) == rui_record[1]:
        return (azara_record[0], azara_record[1],
        rui_record[0], rui_record[1], rui_record[2])
    else:
        return "not a match"
print (create_record(('Brass Spyglass', '4B'), ('Abandoned Lighthouse', ('4', 'B'), 'Blue'))) 
print (create_record(('Brass Spyglass', '4B'), ('Seaside Cottages', ('1', 'C'), 'blue')))

def clean_up(combined_record_group):
    cleaned_records = []
    
    for record in combined_record_group:
        cleaned = (record[0], record[2], record[3], record[4])
        cleaned_text = str (cleaned)
        cleaned_records.append(cleaned_text)
    report = "\n".join(cleaned_records) + "\n"
    return report


print (clean_up((('Brass Spyglass', '4B', 'Abandoned Lighthouse', ('4', 'B'), 'Blue'), ('Vintage Pirate Hat', '7E', 'Quiet Inlet (Island of Mystery)', ('7', 'E'), 'Orange'), ('Crystal Crab', '6A', 'Old Schooner', ('6', 'A'), 'Purple'))))
