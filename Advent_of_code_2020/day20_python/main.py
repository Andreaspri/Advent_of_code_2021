
import numpy as np
from math import sqrt
import re



class Tile:
    def __init__(self, tile) -> None:
        
        self.x = None
        self.y = None


        # Get tile id
        tile = tile.split('\n')
        self.id = int(tile[0].split(' ')[1][:-1])
        # Pop id from tile
        tile.pop(0)


        # Make a np bitmap of the tile, convert . to 0 and # to 1
        self.bitmap = np.array([np.array([1 if c == '#' else 0 for c in row]) for row in tile])
        
        # Store additional information about the tile for faster access

        # Edges
        self.top = self.bitmap[0]
        self.bottom = self.bitmap[-1]
        self.left = self.bitmap[:,0]
        self.right = self.bitmap[:,-1]


        # Store all possible edges
        self.edges = self._get_all_possible_edges()

        self.neighbors = []

    def flip_horizontal(self):
        self.bitmap = np.fliplr(self.bitmap)
        self.top = self.bitmap[0]
        self.bottom = self.bitmap[-1]
        self.left = self.bitmap[:,0]
        self.right = self.bitmap[:,-1]

        return self
    
    def flip_vertical(self):
        self.bitmap = np.flipud(self.bitmap)
        self.top = self.bitmap[0]
        self.bottom = self.bitmap[-1]
        self.left = self.bitmap[:,0]
        self.right = self.bitmap[:,-1]

        return self

    def rotate(self):
        self.bitmap = np.rot90(self.bitmap)
        self.top = self.bitmap[0]
        self.bottom = self.bitmap[-1]
        self.left = self.bitmap[:,0]
        self.right = self.bitmap[:,-1]

        return self

    
    def remove_edges(self):
        self.bitmap = self.bitmap[1:-1,1:-1]
        self.top = self.bitmap[0]
        self.bottom = self.bitmap[-1]
        self.left = self.bitmap[:,0]
        self.right = self.bitmap[:,-1]


    # Check if two tiles can be joined together
    def can_join(self, other):
        if np.array_equal(self.top, other.bottom):
            return "top"
        elif np.array_equal(self.bottom, other.top):
            return "bottom"
        elif np.array_equal(self.left, other.right):
            return "left"
        elif np.array_equal(self.right, other.left):
            return "right"
        else:
            return False
    
    def is_neighbor(self, other):
        if self.id != other.id:
            if self.edges.intersection(other.edges):
                return True
            return False

    def _get_all_possible_edges(self):
        edges = set()
        for i in range(4):
            edges.add(tuple(self.top))
            edges.add(tuple(self.bottom))
            edges.add(tuple(self.left))
            edges.add(tuple(self.right))
            self.rotate()
        self.flip_horizontal()
        for i in range(4):
            edges.add(tuple(self.top))
            edges.add(tuple(self.bottom))
            edges.add(tuple(self.left))
            edges.add(tuple(self.right))
            self.rotate()
        self.flip_horizontal()
        self.flip_vertical()
        for i in range(4):
            edges.add(tuple(self.top))
            edges.add(tuple(self.bottom))
            edges.add(tuple(self.left))
            edges.add(tuple(self.right))
            self.rotate()
        self.flip_vertical()

        return edges

    def __lt__(self, o: object) -> bool:
        return self.y < o.y or (self.y == o.y and self.x > o.x)

    def __hash__(self) -> int:
        return self.id

    def __eq__(self, o: object) -> bool:
        return self.id == o.id

    def __repr__(self) -> str:
        return f"Tile {self.id}"
    





def make_board(tiles):

    board = np.array([Tile(tile) for tile in tiles], dtype=object)

    for tile in board:
        for tile2 in board:
            if tile.id != tile2.id:
                if tile.is_neighbor(tile2):
                    tile.neighbors.append(tile2)
    

    # Get one corner tile and start building the board from there
    corner = None
    for tile in board:
        if len(tile.neighbors) == 2:
            corner = tile
            break

    tiles_left = set([corner])
    placed_tiles = set()
    # Assume that the corner is in the top left corner and is correctly oriented
    corner.x = 0
    corner.y = 0

    while tiles_left:
        # Pop one tile from the set
        tile = tiles_left.pop()
        placed_tiles.add(tile)

        for neighbor in tile.neighbors:
            if neighbor not in placed_tiles:
                for flip in [neighbor.flip_horizontal, neighbor.flip_vertical]:
                    for rotate in [neighbor.rotate] * 4:
                        if tile.can_join(neighbor):
                            break
                        rotate()
                    if tile.can_join(neighbor):
                        break
                    flip()
                direction = tile.can_join(neighbor)
                if direction == "top":
                    neighbor.x = tile.x
                    neighbor.y = tile.y - 1
                elif direction == "bottom":
                    neighbor.x = tile.x
                    neighbor.y = tile.y + 1
                elif direction == "left":
                    neighbor.x = tile.x - 1
                    neighbor.y = tile.y
                elif direction == "right":
                    neighbor.x = tile.x + 1
                    neighbor.y = tile.y

                tiles_left.add(neighbor)




    
                    
    return board


def concatenate_tiles(board):
    # Remove edges from all tiles
    for tile in board:
        tile.remove_edges()

    # Get the size of the board
    size = int(sqrt(len(board)))

    # Sort the tiles
    board = sorted(board, reverse=True)

    # Get the bitmaps of all tiles
    for i in range(len(board)):
        board[i] = board[i].bitmap
    
    # Concatenate the tiles into one bitmap
    bitmap = np.concatenate([np.concatenate([board[i*size + j] for j in range(size)], axis=1) for i in range(size-1, -1, -1)], axis=0)
    

    return bitmap





def find_monsters(bitmap):
    str_map = [''.join([str(c) for c in row]) for row in bitmap]
    
    # Regex for the monster, the (?=) is a lookahead assertion. It handles the overlapping monsters
    middle = "(?=(1[0-1]{4}11[0-1]{4}11[0-1]{4}111))"
    bottom = "(?=(1[0-1]{2}1[0-1]{2}1[0-1]{2}1[0-1]{2}1))"
    monsters = set()
    for i in range(len(str_map)-2):
        middle_matches = re.finditer(middle, str_map[i+1])
        bottom_matches = re.finditer(bottom, str_map[i+2])

        
        # Get all the middle matches with the index of the match
        middle_matches = [int(match.start()) for match in middle_matches]
        # Get all the bottom matches with the index of the match
        bottom_matches = [int(match.start()) for match in bottom_matches]

        if middle_matches and bottom_matches:
            for mid_match in middle_matches:
                for bot_match in bottom_matches:
                    if (mid_match + 1) == bot_match and mid_match+18 < len(str_map[0]) and str_map[i][mid_match+18] == "1":
                        # Store all the positions of the monster and return them as a set
                        monsters |= set([(i, mid_match+18),
                                        (i+1, mid_match),
                                        (i+1, mid_match+5),
                                        (i+1, mid_match+6),
                                        (i+1, mid_match+11),
                                        (i+1, mid_match+12),
                                        (i+1, mid_match+17),
                                        (i+1, mid_match+18),
                                        (i+1, mid_match+19),
                                        (i+2, bot_match),
                                        (i+2, bot_match+3),
                                        (i+2, bot_match+6),
                                        (i+2, bot_match+9),
                                        (i+2, bot_match+12),
                                        (i+2, bot_match+15)]
                                        )
                        
    if monsters:
        return monsters
    else:
        return set()
                        

                                                
                                    


def part_1(board):
    total = 1
    for tile in board:
        if len(tile.neighbors) == 2:
            total *= tile.id

    return total




def part_2(bitmap):
    monsters = set()
    for flip in [np.fliplr, np.flipud]:
        for rotate in [np.rot90] * 4:
            monsters |= find_monsters(bitmap)
            if len(monsters) > 0:
                break
            bitmap = rotate(bitmap)
        monsters |= find_monsters(bitmap)
        if len(monsters) > 0:
            break
        bitmap = flip(bitmap)
    
    
    return np.sum(bitmap) - len(monsters)
    
    



if __name__ == "__main__":

    with open('data.txt') as f:
        tiles = f.read().split('\n\n')

        board = make_board(tiles)
        print("Part 1:", part_1(board))
        

        bitmap = concatenate_tiles(board)
        
        print("Part 2:", part_2(bitmap))

