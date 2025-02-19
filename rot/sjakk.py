import chess
import chess.engine

# Create a new chess board
board = chess.Board()

# Print the initial board
print(board)

# Make a move (e2e4)
move = chess.Move.from_uci("e2e4")
board.push(move)

# Print the board after the move
print(board)

# Initialize the chess engine (replace "path/to/your/engine" with the actual path to your engine)
engine = chess.engine.SimpleEngine.popen_uci("path/to/your/engine")

# Get the best move from the engine
result = engine.play(board, chess.engine.Limit(time=0.1))
print("Best move:", result.move)

# Make the engine's move
board.push(result.move)

# Print the board after the engine's move
print(board)

# Quit the engine
engine.quit()
