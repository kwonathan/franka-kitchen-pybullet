import pybullet as p
import time
import config
from kitchen_assets.load_franka_kitchen import loadFrankaKitchen, updateFrankaKitchen

class Environment:

    def __init__(self):
        self.value = None

    def load(self):
        p.resetDebugVisualizerCamera(cameraDistance=config.cameraDistance,
                                     cameraYaw=config.cameraYaw,
                                     cameraPitch=config.cameraPitch,
                                     cameraTargetPosition=config.cameraTargetPosition)
        kitchen, kettle = loadFrankaKitchen()
        self.value = kitchen
        p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)

    def update(self):
        updateFrankaKitchen(self.value)
        p.stepSimulation()
        time.sleep(config.control_dt)
