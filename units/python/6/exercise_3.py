
import math


def parse_line(equation):
    """
    Parses the given equation of line in y = mx + c, and returns
    the values of m and c.
    """

    # Split the equation with '=' into LHS and RHS.
    rhs = equation.split('=')[1]

    # Split the RHS into two parts 'mx' and 'c' with '+' operator.
    parts = rhs.split('+')

    # Get the value of 'm' from the first part, 'mx'.
    m = parts[0].replace('x', '').strip()

    # Get the value of 'c' from the second part.
    c = parts[1].strip()

    return (float(m), float(c))


def get_intersection(line1, line2):
    """
    Calculates the intersection point of two lines given by their 
    parsed tuples each containing slope & y-intercept. 
    """
    (m1, c1) = line1
    (m2, c2) = line2

    # Get the point of intersection
    x = (c1 - c2) / (m2 - m1)
    y = m1 * x + c1             # As we have y = mx + c

    return (x, y)


def get_angle(line1, line2):
    """
    Calculates the angle between two lines (in Degrees) using their
    parsed tuples each containing slope & y-intercept
    """

    (m1, c1) = line1
    (m2, c2) = line2

    denominator = 1.0 + m1 * m2

    # If this part of the expression results to zero
    # then it implies the angle between the lines is 90 degrees.
    if denominator == 0:
        return 90.0

    angle_radian = math.atan((m1 - m2) / denominator)

    return angle_radian * (180 / math.pi)


def get_lines_relation(angle):
    if angle == 0:
        return 'parallel'
    elif angle == 90:
        return 'perpendicular'


def main():
    """
    The main function that actually executes the program.
    """

    print('Enter equations of lines in y = mx + c form:\n')

    # Get the equations of two lines from the user.
    equation1 = input('Line 1: ')
    equation2 = input('Line 2: ')

    # Parse the two equations of two lines.
    line1 = parse_line(equation1)
    line2 = parse_line(equation2)

    # Print the intersection point.
    point = get_intersection(line1, line2)
    print('\nIntersection Point (x, y) = ({}, {})'.format(*point))

    # Angle between lines.
    angle = get_angle(line1, line2)
    print('Angle between lines = {} Degrees'.format(angle))

    # Relation in between lines i.e parallel or perpendicular.
    relation = get_lines_relation(angle)
    if not relation is None:
        print('The lines are {}'.format(relation))


# Run the program
main()
