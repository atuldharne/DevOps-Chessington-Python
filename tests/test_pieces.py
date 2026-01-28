from chessington.engine.board import Board
from chessington.engine.data import Player, Square
from chessington.engine.pieces import Pawn, King, Queen, Rook, Bishop, Knight

class TestPawns:

    @staticmethod
    def test_white_pawns_can_move_up_one_square():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.WHITE)
        square = Square.at(1, 4)
        board.set_piece(square, pawn)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert Square.at(2, 4) in moves

    @staticmethod
    def test_black_pawns_can_move_down_one_square():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.BLACK)
        square = Square.at(6, 4)
        board.set_piece(square, pawn)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert Square.at(5, 4) in moves

    @staticmethod
    def test_white_pawn_can_move_up_two_squares_if_not_moved():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.WHITE)
        square = Square.at(1, 4)
        board.set_piece(square, pawn)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert Square.at(3, 4) in moves

    @staticmethod
    def test_black_pawn_can_move_down_two_squares_if_not_moved():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.BLACK)
        square = Square.at(6, 4)
        board.set_piece(square, pawn)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert Square.at(4, 4) in moves

    @staticmethod
    def test_white_pawn_cannot_move_up_two_squares_if_already_moved():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.WHITE)
        starting_square = Square.at(1, 4)
        board.set_piece(starting_square, pawn)

        intermediate_square = Square.at(2, 4)
        pawn.move_to(board, intermediate_square)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert Square.at(3, 4) in moves
        assert Square.at(4, 4) not in moves

    @staticmethod
    def test_black_pawn_cannot_move_down_two_squares_if_already_moved():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.BLACK)
        starting_square = Square.at(6, 4)
        board.set_piece(starting_square, pawn)

        intermediate_square = Square.at(5, 4)
        board.current_player = Player.BLACK
        pawn.move_to(board, intermediate_square)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert Square.at(4, 4) in moves
        assert Square.at(3, 4) not in moves

class TestKings:

    @staticmethod
    def test_king_can_move_one_square_in_any_direction():

        # Arrange
        board = Board.empty()
        king = King(Player.WHITE)
        square = Square.at(3, 3)
        board.set_piece(square, king)

        # Act
        moves = king.get_available_moves(board)

        # Assert
        assert Square.at(2, 2) in moves
        assert Square.at(2, 3) in moves

class TestQueens:

    @staticmethod
    def test_queen_can_move_any_number_of_squares_in_any_direction():    
    
    # Arrange
        board = Board.empty()
        queen = Queen(Player.WHITE)
        square = Square.at(3, 3)
        board.set_piece(square, queen)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        #Horizontal and Vertical
        assert Square.at(0, 3) in moves
        #Diagonal
        assert Square.at(0, 0) in moves

class TestRooks:
    @staticmethod
    def test_rook_can_move_any_number_of_squares_horizontally_or_vertically():    
    
    # Arrange
        board = Board.empty()
        rook = Rook(Player.WHITE)
        square = Square.at(3, 3)
        board.set_piece(square, rook)

        # Act
        moves = rook.get_available_moves(board)

        # Assert
        assert Square.at(0, 3) in moves

class TestBishops:
    @staticmethod
    def test_bishop_can_move_any_number_of_squares_diagonally():    
    
    # Arrange
        board = Board.empty()
        bishop = Bishop(Player.WHITE)
        square = Square.at(3, 3)
        board.set_piece(square, bishop)

        # Act
        moves = bishop.get_available_moves(board)

        # Assert
        assert Square.at(0, 0) in moves
        assert Square.at(7, 7) in moves 