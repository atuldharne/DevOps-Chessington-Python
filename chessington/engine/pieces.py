from __future__ import annotations
from abc import ABC, abstractmethod
from chessington.engine.data import Player, Square
from typing import TYPE_CHECKING, Any, List

if TYPE_CHECKING:
    from chessington.engine.board import Board

class Piece(ABC):
    """
    An abstract base class from which all pieces inherit.
    """

    def __init__(self, player: Player):
        self.player = player

    def to_json(self) -> dict[str, Any]:
        return {
            "piece": self.__class__.__name__,
            "player": self.player._name_.lower()
        }

    @abstractmethod
    def get_available_moves(self, board: Board) -> List[Square]:
        """
        Get all squares that the piece is allowed to move to.
        """
        pass

    def move_to(self, board: Board, new_square):
        """
        Move this piece to the given square on the board.
        """
        current_square = board.find_piece(self)
        board.move_piece(current_square, new_square)


class Pawn(Piece):
    """
    A class representing a chess pawn.
    """
    def __init__(self, player: Player):
        super().__init__(player)
        self.has_moved = False

    def get_available_moves(self, board) -> List[Square]:
        current_square = board.find_piece(self)
        moves = []
        
        if self.player == Player.BLACK:
            square_in_front = Square.at(current_square.row - 1, current_square.col)
            if board.is_square_empty(square_in_front):
                moves.append(square_in_front)
                # Two squares forward on first move if not moved
                if not self.has_moved:
                    two_squares_in_front = Square.at(current_square.row - 2, current_square.col)
                    if board.is_square_empty(two_squares_in_front) and board.is_square_empty(two_squares_in_front):
                        moves.append(two_squares_in_front)
        else:
            square_in_front = Square.at(current_square.row + 1, current_square.col)
            if board.is_square_empty(square_in_front):
                moves.append(square_in_front)
                # Two squares forward on first move if not moved
                if not self.has_moved:
                    two_squares_in_front = Square.at(current_square.row + 2, current_square.col)
                    if board.is_square_empty(two_squares_in_front) and board.is_square_empty(two_squares_in_front):
                        moves.append(two_squares_in_front)
        return moves
    
    def move_to(self, board: Board, new_square):
        super().move_to(board, new_square)
        self.has_moved = True

class Knight(Piece):
    """
    A class representing a chess knight.
    """

    def get_available_moves(self, board):
        return []


class Bishop(Piece):
    """
    A class representing a chess bishop.
    """

    def get_available_moves(self, board) -> List[Square]:
        current_square = board.find_piece(self)
        moves = []
        # Diagonal moves
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

        for d_row, d_col in directions:
            for distance in range(1, 8):
                new_row = current_square.row + d_row * distance
                new_col = current_square.col + d_col * distance
                if 0 <= new_row < 8 and 0 <= new_col < 8:
                    new_square = Square.at(new_row, new_col)
                    if board.is_square_empty(new_square):
                        moves.append(new_square)
                    else:
                        # Stop if we hit another piece
                        break
                else:
                    break
        return moves


class Rook(Piece):
    """
    A class representing a chess rook.
    """

    def get_available_moves(self, board) -> List[Square]:
        current_square = board.find_piece(self)
        moves = []
        # Horizontal and vertical moves
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for d_row, d_col in directions:
            for distance in range(1, 8):
                new_row = current_square.row + d_row * distance
                new_col = current_square.col + d_col * distance
                if 0 <= new_row < 8 and 0 <= new_col < 8:
                    new_square = Square.at(new_row, new_col)
                    if board.is_square_empty(new_square):
                        moves.append(new_square)
                    else:
                        # Stop if we hit another piece
                        break
                else:
                    break
        return moves


class Queen(Piece):
    """
    A class representing a chess queen.
    """
    def get_available_moves(self, board) -> List[Square]:
        # Queen moves both like a rook and a bishop
        current_square = board.find_piece(self)
        moves = []
        # Combine directions of rook and bishop
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        for d_row, d_col in directions:
            for distance in range(1, 8):
                new_row = current_square.row + d_row * distance
                new_col = current_square.col + d_col * distance
                if 0 <= new_row < 8 and 0 <= new_col < 8:
                    new_square = Square.at(new_row, new_col)
                    if board.is_square_empty(new_square):
                        moves.append(new_square)
                    else:
                        # Stop if we hit another piece
                        break
                else:
                    break
        return moves


class King(Piece):
    """
    A class representing a chess king.
    """

    def get_available_moves(self, board) -> List[Square]:
        current_square = board.find_piece(self)
        moves = []
        # King moves one square in any direction
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        for d_row, d_col in directions:
            new_row = current_square.row + d_row
            new_col = current_square.col + d_col
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                new_square = Square.at(new_row, new_col)
                if board.is_square_empty(new_square):
                    moves.append(new_square)
        return moves