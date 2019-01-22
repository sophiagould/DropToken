# Author: Sophia Gould - 01/22/2019
# Written & Tested in Python 3.4


class DropTokenGame:
    def __init__(self):
        self.BOARD_DIMENSION = 4
        self._player_1 = True
        self._columns = []
        self.board = [[] for _ in range(self.BOARD_DIMENSION)]

    def put_token(self, col=None, *args):
        """Drop token into column, perform game status check, alternate player"""

        try:
            col = int(col)
        except ValueError:
            print('ERROR')
            return

        if col > self.BOARD_DIMENSION or len(self.board[col-1]) == self.BOARD_DIMENSION:
            print('ERROR')
        else:
            self._columns.append(col)
            self.board[col-1].append('1' if self._player_1 else '2')
            self._check_board(col-1, len(self.board[col-1])-1)
            self._player_1 = not self._player_1
        return

    def get_columns(self, *args):
        [print(x) for x in self._columns]
        return

    def _get_board_at(self, i, j):
        """Return '0', '1', or '2' depending on board content"""

        return '0' if len(self.board[i]) <= j else self.board[i][j]

    def print_board(self, *args):
        """Print contents of board to spec"""

        for j in range(self.BOARD_DIMENSION-1, -1, -1):
            print('| ', end='')
            [print(self._get_board_at(i, j), end=' ') for i in range(self.BOARD_DIMENSION)]
            print()
        print('+' + '--' * self.BOARD_DIMENSION)
        print('  ' + ' '.join(map(str, range(1, self.BOARD_DIMENSION+1))))
        return

    def _check_board(self, col, row):
        """Check board state for 4-in-a-row.
        The check is a bit cryptic but effectively runs through row, column, and diagonals
        of the newly-inserted value and tries to find '1 1 1 1' or '2 2 2 2'."""

        rows = ' '.join([self._get_board_at(i, row) for i in range(self.BOARD_DIMENSION)])
        cols = ' '.join(self.board[col])

        # Traverse matrix diagonally by calculating an offset to the edge and walking forwards through row,col
        diag_up = ' '.join([self._get_board_at(col+i, row+i)
                            for i in range(-min(row, col), self.BOARD_DIMENSION - max(row, col))])
        diag_down = ' '.join([self._get_board_at(col + i, row - i)
                            for i in range(-min(self.BOARD_DIMENSION - row - 1, col),
                                self.BOARD_DIMENSION - max(self.BOARD_DIMENSION - row - 1, col))])

        if ('1 1 1 1' if self._player_1 else '2 2 2 2') in rows + ':'+cols + ':' + diag_up + ':' + diag_down:
            print('WIN')
        elif all([len(x) == self.BOARD_DIMENSION for x in self.board]):
            print('DRAW')
        else:
            print('OK')
        return

    def play(self):
        """Play the game"""

        funcs = {'PUT': self.put_token, 'GET': self.get_columns, 'BOARD': self.print_board}
        while True:
            com = input('> ').split()

            if com[0] == 'EXIT':
                break
            if com[0] not in funcs:
                print('ERROR')
            else:
                funcs[com[0]](*com[1:])


if __name__ == '__main__':
    game = DropTokenGame()
    game.play()
