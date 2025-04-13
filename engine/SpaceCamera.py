import numpy as np

class SpaceCamera:
    def __init__(self, resolution=(1024, 1024), pixel_size=10e-6, exposure_time=1):
        self.resolution = resolution
        self.pixel_size = pixel_size          # meters per pixel
        self.exposure_time = exposure_time   # seconds
        
        # Sensor noise parameters
        self.dark_current = 50                # e-/s
        self.read_noise = 25                  # e-
        
    def simulate(self, scene_radiance):
        """
        Simulate sensor response to radiance (W/m²·sr)
        """
        flux = scene_radiance * self.pixel_size**2 * np.pi  # W/s per pixel
        charge = flux * self.exposure_time + self.dark_current * self.exposure_time
        
        # Add noise sources
        shot_noise = np.random.poisson(lam=charge / 10)
        readout_noise = np.random.normal(0, self.read_noise, size=self.resolution)
        
        signal = (charge + shot_noise) * np.exp(-self.exposure_time/2)  # Simplified decay model
        return signal + readout_noise