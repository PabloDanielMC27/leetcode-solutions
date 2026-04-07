# 2069. Walking Robot Simulation II

class Robot:

    # base solution

    def __init__(self, width: int, height: int):
        # grid
        self.width = width - 1
        self.height = height - 1
        self.perimeter = 2 * (self.width + self.height)

        # robot
        self.robot_x = 0
        self.robot_y = 0
        self.robot_dir = "East"

    # def move

    def step(self, num: int) -> None:

        num %= self.perimeter
        if num == 0:
            num = self.perimeter
        
        while num > 0:
            match self.robot_dir:
                case "North":
                    if self.robot_y + 1 <= self.height:
                        self.robot_y += 1
                        num -= 1
                    else:
                        self.robot_dir = "West"

                case "West":
                    if self.robot_x - 1 >= 0:
                        self.robot_x -= 1
                        num -= 1
                    else:
                        self.robot_dir = "South"

                case "South":
                    if self.robot_y - 1 >= 0:
                        self.robot_y -= 1
                        num -= 1
                    else:
                        self.robot_dir = "East"
                
                case "East":
                    if self.robot_x + 1 <= self.width:
                        self.robot_x += 1
                        num -= 1
                    else:
                        self.robot_dir = "North"              

    def getPos(self) -> List[int]:
        return [self.robot_x, self.robot_y]        

    def getDir(self) -> str:
        return self.robot_dir


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()
