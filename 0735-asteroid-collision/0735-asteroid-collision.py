class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        def process_asteroid(current_asteroid):
            if not stack:
                stack.append(asteroid)
                return

            last_asteriod = stack[-1]

            # check if last asteroid and current asteriod is in same direction
            if (last_asteriod < 0 and current_asteroid > 0) or (last_asteriod * current_asteroid > 0): # both are coming in opposite direction
                stack.append(current_asteroid) # they wont collide

            # they are not in same direction and last asteroid is bigger
            elif abs(last_asteriod) > abs(current_asteroid):
                return # new asteriod exploded

            # they are not in same direction and they are of same size
            elif abs(last_asteriod) == abs(current_asteroid):
                stack.pop() # remove the last asteroid which is exploded

            # current asteriod is bigger than the last asteroid
            else:
                stack.pop() # remote it process that asteroid again with the
                process_asteroid(current_asteroid)

        for asteroid in asteroids:
            # print(f'Current Stack: {stack}')
            process_asteroid(asteroid)
            
        return stack