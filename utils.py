from enums import Update_map


def lost_message(code: Update_map):
    print(f"Lost: {'' if code == Update_map.TAIL else 'the wall'}")
