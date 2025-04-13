import trimesh as tm

class Spacecraft:
    def __init__(self, model_path):
        self.mesh = tm.load(model_path)  # Load .obj or .stl file
        
        # Add materials (specular reflection for metallic surfaces)
        self.material = tm.Material(
            metallic=0.9,
            roughness=0.1,
            color=np.array([0.3, 0.4, 0.5])  # Example: black and grey
        )
        
    def render(self):
        """
        Render the spacecraft in the scene
        """
        self.mesh.export("gateway.obj")  # Export to OpenGL-compatible format
        
        # Load into ModernGL buffers
        vertices = self.mesh.vertices.astype('f4').tobytes()
        normals = self.mesh.normals.astype('f4').tobytes()
        
        vbo_vertices = self.ctx.buffer(data=vertices)
        vbo_normals = self.ctx.buffer(data=normals)
        
        # Bind buffers to vertex attributes
        program['in_position'] = vbo_vertices
        program['in_normal'] = vbo_normals
        
        # Draw mesh
        vao = self.ctx.simple_vertex_array(program, vertices=vbo_vertices, normals=vbo_normals)
        vao.render()
