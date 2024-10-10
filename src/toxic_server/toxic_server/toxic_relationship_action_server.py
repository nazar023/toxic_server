import time
import random

import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node

from toxic_relationship.action import ToxicRelationship


class ToxicRelationshipActionServer(Node):

    def __init__(self):
        super().__init__('toxic_relationship_action_server')
        self._action_server = ActionServer(
            self,
            ToxicRelationship,
            'relationship',
            self.execute_callback)

    def execute_callback(self, goal_handle):
        self.get_logger().info(f'Recieve {goal_handle.request.toxicity_rate}% of toxicity rate from client')
        self.get_logger().info('Process...')

        feedback_msg = ToxicRelationship.Feedback()
        years_alive = 0
        living_status = True

        if goal_handle.request.toxicity_rate > 50:
            feedback_msg.feedback = "I've almost sure I got a bad news for you 💔"
            goal_handle.publish_feedback(feedback_msg)

        for i in range(1, 11):
            random_percentage_int = random.randint(1, 100)
            years_alive = i
            if goal_handle.request.toxicity_rate > random_percentage_int:
                living_status = False
                self.get_logger().info('Client died 💀')
                break
            feedback_msg.feedback = f'You survived {i} year(s)'
            goal_handle.publish_feedback(feedback_msg)
            self.get_logger().info(f'{i}-st year of relationship')
            time.sleep(1)

        goal_handle.succeed()

        result = ToxicRelationship.Result()
        result.living_status = living_status
        return result


def main(args=None):
    rclpy.init(args=args)
    toxic_relationship_action_server = ToxicRelationshipActionServer()
    rclpy.spin(toxic_relationship_action_server)


if __name__ == '__main__':
    main()
