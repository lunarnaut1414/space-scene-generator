generator = SpaceSceneGenerator()
frame = generator.generate()

# Visualize the generated frame
import matplotlib.pyplot as plt

plt.imshow(frame.astype(np.uint8), cmap='viridis')
plt.show()