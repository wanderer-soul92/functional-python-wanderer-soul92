BMS_allowed_range = {'temperature': {'min': 0, 'max': 45},
                'soc': {'min': 20, 'max': 80},
                'charge_rate': {'min': 0, 'max': 0.8}}



def get_out_of_range_count(BMS_input):
    out_of_range_count =0
    for c in BMS_input.items() :
        if c not in range (BMS_allowed_range.c[min], BMS_allowed_range.c[max]):
            out_of_range_count =+ 1
    return out_of_range_count

def print_out_of_range_output(BMS_input):
    out_of_range_count = get_out_of_range_count(BMS_input)
    if len(out_of_range_count) == 0: 
        return True
    else :
        return False
