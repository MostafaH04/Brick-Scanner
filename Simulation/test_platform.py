import unittest
from Platform import Platform
import numpy as np

class PlatformUnitTesting(unittest.TestCase):

  def test_Camera2LinkInitial(self):
    newPlatform = Platform()
    
    Cam2Link_rotation = newPlatform.rot_cam2link

    Cam2Link_rotation_expected = np.matrix([[-1, 0, 0],
                                            [0, 1, 0],
                                            [0, 0, -1]])
    
    Cam2Link_position = newPlatform.pos_cam2link

    Cam2Link_position_expected = np.array([0, -0.09, 0.09])

    
    self.assertTrue(np.array_equal(Cam2Link_rotation, Cam2Link_rotation_expected)
                    and np.array_equal(Cam2Link_position, Cam2Link_position_expected))
    