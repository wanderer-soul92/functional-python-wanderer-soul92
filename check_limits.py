import EV_test

if __name__ == '__main__':
    #assert(EV_test.battery_is_ok(25, 70, 0.7) is True)
    #assert(EV_test.battery_is_ok(50, 85, 0) is False)
    assert(EV.test.print_out_of_range_output({
       'temperature' : 25,
       'state_of_charge' : 70,
       'charge_rate' : 0.9
          }) is true) 
