class CountSquares:

    def __init__(self):
        self.points = []
        
    def add(self, point: List[int]) -> None:
        self.points.append((point[0], point[1]))
        
    def count(self, point: List[int]) -> int:
        possible = 0

        y_cord_of_x_matched = []
        x_cord_of_y_matched = []

        for p in self.points:
            if p[0] == point[0]:
                y_cord_of_x_matched.append(p[1])
            if p[1] == point[1]:
                x_cord_of_y_matched.append(p[0])
        
        for x in x_cord_of_y_matched:
            for y in y_cord_of_x_matched:
                if x == point[0] or y == point[1]:
                    continue
                
                if abs(x - point[0]) != abs(y - point[1]):
                    continue

                if (x, y) in self.points:
                    possible += self.points.count((x, y))
        
        return possible