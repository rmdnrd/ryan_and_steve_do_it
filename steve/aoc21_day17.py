"""Solves the problem Ryan Bell couldn't solve."""

def get_input(filename):
    """Read in file data."""
    with open(filename,'r',encoding='utf-8') as file:
        contents = file.read().splitlines()

    return contents

def determine_highest_accurate_trajectory(position,velocity,highest_y,grid):
    "Given a velocity pair, determine if it will land in grid."
    position_x = position[0]
    position_y = position[1]
    velocity_x = velocity[0]
    velocity_y = velocity[1]

    if position_y > highest_y:
        highest_y = position_y

    # Arrow has passed by grid
    if position_y < grid['y_max'] or (velocity_x == 0 and position_x < grid["x_min"]):
        return False

    if position_x >= grid["x_min"] and position_x <= grid["x_max"]:
        if position_y <=  grid["y_min"] and position_y >= grid["y_max"]:
            # This starting trajectory was successful
            return highest_y

    # Updating parameters to make new recursive call
    new_position = (position_x + velocity_x,position_y + velocity_y)

    # X velocity can vary
    if velocity_x == 0:
        new_x_velocity = 0
    elif velocity_x > 0:
        new_x_velocity = velocity_x - 1

    # Y will always be -'ed 1
    new_velocity = (new_x_velocity,velocity_y-1)

    # Call function with updated parameters
    return determine_highest_accurate_trajectory(new_position,new_velocity,highest_y,grid)

def solve(grid):
    """Given a target grid, find all launch trajectory combinations that will land in the grid."""

    highest_y_apex = 0
    successful_launches = 0

    for x_velocity in range(0,x_max+1,1):
        for y_velocity in range(y_max,abs(y_max)+1,1):
            result = determine_highest_accurate_trajectory(
                                                            (0,0),
                                                            (x_velocity,y_velocity),
                                                            highest_y_apex,
                                                            grid
                                                            )

            # Function returns False, or highest Y position achieved on successful launch
            if not isinstance(result,bool):
                successful_launches += 1
                if result > highest_y_apex:
                    highest_y_apex = result

    return highest_y_apex,successful_launches

if __name__ == "__main__":

    text_line = get_input("input-17.txt")
    obj = {}
    line = text_line[0]
    x,y = line.split(":")[1].split(",")
    x_min, x_max = x.split("=")[1].split("..")
    y_max, y_min = y.split("=")[1].split("..")

    obj.setdefault("x_min",int(x_min))
    obj.setdefault("x_max",int(x_max))
    obj.setdefault("y_min",int(y_min))
    obj.setdefault("y_max",int(y_max))
    max_y,count = solve(obj)
    print(f"Max-Y:{max_y},# OK Trajectories:{count}")
