class SpaceSceneGenerator:
    def __init__(self):
        self.camera = SpaceCamera(resolution=(1024, 1024))
        self.scene = Scene()
        self.spacecraft = Spacecraft("spacecraft.obj")
        
    def generate(self):
        # Simulate camera exposure
        radiance = self.scene.render()  # Get scene radiance map
        
        # Apply sensor noise and response
        image_data = self.camera.simulate(radiance)
        
        # Add spacecraft to the scene
        self.spacecraft.position = (0.5, 0.5, 1.0)  # Position in frame buffer space
        
        return image_data