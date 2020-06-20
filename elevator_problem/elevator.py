# CONSTANTS:
UP = 'up'
DOWN = 'down'


class Elevator:
    def __init__(self, total_floors):
        self.current_floor = 1
        self.direction = None
        self.total_floors = total_floors
        self.floor_dict_up = {i: False for i in range(1, total_floors + 1)}
        self.floor_dict_down = {i: False for i in range(1, total_floors + 1)}

    def get_direction(self, floor_number):
        if floor_number > self.current_floor:
            return UP
        elif floor_number < self.current_floor:
            return DOWN
        else:
            print('Same Floor, Please Select Another Floor Number')

    def close_door(self):
        self.current_floor = None

    def floor_input(self, floor_number):
        # need to handle floor_numbers outside of range.
        input_direction = self.get_direction(floor_number=floor_number)
        self.direction = self.direction if self.direction else input_direction  # if no direction yet set
        if input_direction == UP:
            self.floor_dict_up[floor_number] = True
        elif input_direction == DOWN:
            self.floor_dict_down[floor_number] = True

    def move_to_next_floor(self):
        if self.direction == UP:
            for floor_num in range(self.current_floor, self.total_floors + 1):
                if self.floor_dict_up[floor_num]:
                    self.current_floor = floor_num
                    self.floor_dict_up[floor_num] = False
                    return f'You have arrived at floor {floor_num}'
            if any(self.floor_dict_down.values()):
                self.direction = DOWN
                return self.move_to_next_floor()
        elif self.direction == DOWN:
            for floor_num in range(1, self.current_floor)[::-1]:
                if self.floor_dict_down[floor_num]:
                    self.current_floor = floor_num
                    self.floor_dict_down[floor_num] = False
                    return f'You have arrived at floor {floor_num}'
            if any(self.floor_dict_up.values()):
                self.direction = UP
                return self.move_to_next_floor()

    def get_current_floor(self):
        """ TODO: implement this with concurrency """


if __name__ == '__main__':
    my_elevator = Elevator(50)
    my_elevator.floor_input(30)
    my_elevator.floor_input(22)
    print(my_elevator.move_to_next_floor())
    my_elevator.floor_input(10)
    my_elevator.floor_input(44)
    print(my_elevator.move_to_next_floor())
    print(my_elevator.move_to_next_floor())
    print(my_elevator.move_to_next_floor())

