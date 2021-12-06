# Project instructions at https://adventofcode.com/2021/day/5

# Gets the start and finish co-ordinates. Creates a list of start co-ordinate tuples and a list of finish co-ordinates
# tuples and returns a list comprising of both lists

def get_data(file_name) -> list:
    starting_point_tuples_list = []
    end_point_tuples_list = []
    data_list = []
    f = open(file_name, 'r')
    for line in f:
        arrays = line.strip("\n").strip(" ").split("->")
        starting_point = arrays[0].split(",")
        starting_point_tuples_list.append((int(starting_point[0]), int(starting_point[1])))
        end_point = arrays[1].split(",")
        end_point_tuples_list.append((int(end_point[0]), int(end_point[1])))
    f.close()
    data_list.append(starting_point_tuples_list)
    data_list.append(end_point_tuples_list)
    return data_list


# Returns list of (x, y) tuples

def get_journey_travelled(start_tuple, finish_tuple) -> list:
    list_of_co_ords = []
    # Same x co-ordinates, different y co-ordinates
    if start_tuple[0] == finish_tuple[0] and start_tuple[1] != finish_tuple[1]:
        lower, higher = min(start_tuple[1], finish_tuple[1]), max(start_tuple[1], finish_tuple[1])
        for y_axis in range(lower, higher + 1):
            list_of_co_ords.append((start_tuple[0], y_axis))
        return list_of_co_ords
    # Different x co-ordinates, same y co-ordinates
    if start_tuple[0] != finish_tuple[0] and start_tuple[1] == finish_tuple[1]:
        lower, higher = min(start_tuple[0], finish_tuple[0]), max(start_tuple[0], finish_tuple[0])
        for x_axis in range(lower, higher + 1):
            list_of_co_ords.append((x_axis, start_tuple[1]))
        return list_of_co_ords
    else:
        return list_of_co_ords  # returns empty list


def get_num_intersections(tuple_data) -> int:
    list_size = len(tuple_data[0])
    starting_co_ords = tuple_data[0]
    finish_co_ords = tuple_data[1]
    tuple_to_freq_dict = {}
    duplicate = set()
    for i in range(list_size):
        co_ord_list = get_journey_travelled(starting_co_ords[i], finish_co_ords[i])
        for co_ordinate_tuple in co_ord_list:
            if co_ordinate_tuple in tuple_to_freq_dict:
                duplicate.add(co_ordinate_tuple)
            else:
                tuple_to_freq_dict[co_ordinate_tuple] = 1
    return len(duplicate)


if __name__ == '__main__':
    data = get_data("CoOrds.txt")  # Two lists in 1. List of opening co-ords and a list of closing co-ords
    print("Number of intersections = " + str(get_num_intersections(data)))
