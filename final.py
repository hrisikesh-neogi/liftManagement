import os

import pandas as pd
import time



class lift_assign:

    def __init__(self, from_floor, to_floor):

        self.floor = to_floor
        self.from_floor = from_floor

    

    def near_by_lift(self):

        data = pd.read_csv('floordata.csv')
        data = data.tail(1)
        data = data.to_dict(orient='records')[0]
        lengths_of_rope = {}
        distance_from_user = {}
        for key in data.keys():
            
                
            value = data[key]
            length_of_rope = 220 - value
            lengths_of_rope[key] = length_of_rope
            
        
        user_position = 220-self.from_floor
        
        for key in lengths_of_rope.keys():
            value = lengths_of_rope[key]
            if value < user_position:
                distance_from_user[key] = user_position - value
            else:
                distance_from_user[key] = value - user_position
    

        minimum_distance = min(distance_from_user.values())
        for key in distance_from_user.keys():
            value = distance_from_user[key]
            if value == minimum_distance:
                return key

    def get_direction(self):
        if self.from_floor > self.floor:
            return 'down'
        else:
            return 'up'

    

    def validation(self):
        if type(self.floor) == int and type(self.from_floor) == int:
            num_list = [num for num in range(0,23)]
            if self.floor in num_list and self.from_floor in num_list:



                return True
            else:
                return False
        else:
            num_list = [str(num) for num in range(0,23)]
            if type(self.floor) == str or type(self.from_floor) == str:
                if self.floor in num_list or self.from_floor in num_list:
                    self.floor = int(self.floor)
                    self.from_floor = int(self.from_floor)
                    return True
                else:
                    return False
            else:
                return False

    def get_lift(self):

        
        
        if self.validation():
            lift = self.near_by_lift()
            direction_ = self.get_direction()

            
        
            data = pd.read_csv('floordata.csv')
            data = data.tail(1)
            data = data.to_dict(orient='records')[0]
            print(f'your lift is lift no - {lift}')
            if data[lift] == self.from_floor:
                print('lift is already at your position')
                time.sleep(2)
                print('lift is opening...')

            else:

                print('lift is coming...')
                time.sleep(1)
                if direction_ == 'up':
                    lift_is_in = data[lift]
                    if self.from_floor > int(lift_is_in):

                        print('lift is at {}'.format(lift_is_in))
                        print('lift is going up...')
                        for i in range (lift_is_in, self.from_floor):
                            print(f'lift is at {i} floor')
                            time.sleep(1)
                    else:
                        print('lift is at {}'.format(lift_is_in))
                        print('lift is going down...')
                        for i in range (lift_is_in, self.from_floor, -1):
                            print(f'lift is at {i} floor')
                            time.sleep(1)
                    print('lift has arrived at your destination')
                    
                    
                else:
                    print('lift is going down...')
                    lift_is_in = data[lift]
                    if self.from_floor < lift_is_in:
                        print('lift is at {}'.format(lift_is_in))
                        for i in range (lift_is_in, self.from_floor, -1):
                            print(f'lift is at {i} floor')
                            time.sleep(1)
                    else:
                        print('lift is at {}'.format(lift_is_in))
                        for i in range (lift_is_in, self.from_floor):
                            print(f'lift is at {i} floor')
                            time.sleep(1)
                        print('lift has arrived at your destination')

            
            if os.path.exists('floordata.csv'):



                existing_data = pd.read_csv('floordata.csv')
                df = existing_data.tail(1).to_dict(orient='records')[0]
                if direction_ == 'up':
                    df[lift] = self.floor
                else:
                    df[lift] = self.from_floor
                existing_data = existing_data.append(df, ignore_index=True)
                existing_data.to_csv('floordata.csv', index=False)
            
        else:
            print('invalid floor')
            print('check if you give the inputs as numbers or not')


               
                
            
        



    

    


        
    
                
                
            




        
                


        
        


                    
        

        
        
        



        

