from csgo.engine import Engine
from csgo.features import Features
import time

def main():
    engine = Engine()
    features = Features(engine, multiprocess=False)
    loops = 1

    while 1:

        if engine.game_state == 6:
            features.recoil_control()
            features.aimbot()
            features.wallhack()

        #print(f'Loop: {loops}')
        loops += 1
        #time.sleep(1)

if __name__ == '__main__':
    main()