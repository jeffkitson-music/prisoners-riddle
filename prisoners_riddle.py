import random
import argparse

class PrisonersRiddle:
    def __init__(self):
        self.success = None

        # Set-Up
        self.boxes = None
        self.prisoners = None

        self.successful_prisoners = []

    def run(self):
        self.boxes, self.prisoners = self.order_boxes_and_prisoners()
        self.simulate_prisoners_riddle()
        return self.success

    @staticmethod
    def order_boxes_and_prisoners():
        boxes = []
        prisoners = []
        b_p = [boxes, prisoners]
        for l in b_p:
            while len(l) < 100:
                n = random.randint(1, 100)
                if n not in l:
                    l.append(n)
        #print(boxes)
        #print(prisoners)
        return boxes, prisoners

    def simulate_prisoners_riddle(self):
        for p in self.prisoners:
            box_to_look_in = p - 1
            for i in range(50):
                if self.boxes[box_to_look_in] == p:
                    #print(f"Prisoner {self.prisoners.index(p) + 1} found their number!")
                    self.successful_prisoners.append(p)
                    break
                else:
                    box_to_look_in = self.boxes[box_to_look_in] - 1
        if len(self.successful_prisoners) == 100:
            #print("Prisoners win!")
            self.success = True
        else:
            #print("Prisoners lose!")
            self.success = False
        self.successful_prisoners.sort()
        #print(self.successful_prisoners)
        #print(f"Success Rate of Prisoners Finding Their Number: {int((len(self.successful_prisoners) / 100) * 100)}%")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Prisoner's Riddle Simulator"
    )

    parser.add_argument(
        '-g', '--games',
        type=int,
        default=1000,
        help="Number of rounds to run (default: 1000)"
    )
    args = parser.parse_args()

    print(f"Running simulation {args.games} times...")


    # Variables
    wins = 0
    losses = 0

    for g in range(args.games):
        pr = PrisonersRiddle()
        success = pr.run()
        if pr.success:
            wins += 1
            print(f"Prisoners win game {g}!")
        else:
            losses += 1
            #print(f"Prisoners lose game {g}!")

    print(f"Win rate: {((wins / args.games) * 100)}%")
    print(f"Loss rate: {((losses / args.games) * 100)}%")
