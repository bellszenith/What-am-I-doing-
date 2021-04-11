def instructions():
    print(
        'Use the directions North, South, East and West to move between rooms.'
    )


def show_status(current_room):
    print('**************')
    print('Current_Location:', current_room)
    print('**************')


def main():
    rooms = {
        'Great Hall': {
            'South': 'Bedroom'
        },
        'Bedroom': {
            'North': 'Great Hall',
            'East': 'Cellar'
        },
        'Cellar': {
            'West': 'Bedroom'
        }
    }
    current_room = 'Great Hall'
    instructions()
    while (True):
        show_status(current_room)
        next_move = input('Enter the direction you would like to go\n')
        desired_room = rooms.get(current_room).get(next_move)

        if desired_room == None:
            print('You can not go that way!')
        elif next_move == 'Quit':
            exit('Thank you for exploring!!')
        else:
            print('You have entered', next_move)
            current_room = desired_room


main()
