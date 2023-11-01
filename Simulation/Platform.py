import numpy as np

class Platform:
  def __init__(self, base_radius = 0.09):
    self.base_radius = base_radius
    self.base_angle = 0
    self.link_angle = 0

    self.rot_cam2link = np.matrix([[-1,0,0],
                                   [0,1,0],
                                   [0,0,-1]])
    
    self.pos_cam2link = np.array([0,-self.base_radius,self.base_radius]).T
    self.pos_link = np.array([0, self.base_radius, 0]).T

    self.update(0,0)
    

  def update(self, linkAngle, baseAngle):
    self.link_angle = linkAngle
    self.base_angle = baseAngle

    cos_beta = np.cos(self.link_angle)
    sin_beta = np.sin(self.link_angle)
    self.rot_link = np.matrix([[cos_beta,0,sin_beta],
                               [0,1,0],
                               [-sin_beta,0,cos_beta]])
    

    self.rot_cam = np.matmul(self.rot_link, self.rot_cam2link)
    self.pos_cam = self.pos_link + np.matmul(self.rot_link,self.pos_cam2link)

    cos_theta = np.cos(self.base_angle)
    sin_theta = np.sin(self.base_angle)
    self.rot_obj = np.matrix([[cos_theta, -sin_theta, 0],
                              [sin_theta, cos_theta, 0],
                              [0,0,1]])

    self.pos_cam2obj = np.matmul(self.rot_obj.T, self.pos_cam.T)
    self.rot_cam2obj = np.matmul(self.rot_obj.T, self.rot_cam.T)
