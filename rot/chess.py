try:
    import chess
    import chess.engine
    print("python-chess is installed.")
except ImportError as e:
    print("python-chess is not installed.")
    print(e)
