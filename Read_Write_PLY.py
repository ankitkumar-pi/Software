#!/usr/bin/env python
# coding: utf-8

# In[317]:


import numpy as np
import os


class Ply(object):
    """Class to represent a ply in memory, read plys, and write plys.
    """

    def __init__(self, ply_path=None, triangles=None, points=None, normals=None, colors=None):
        """Initialize the in memory ply representation.
        
        Args:
            ply_path (str, optional): Path to .ply file to read (note only
                supports text mode, not binary mode). Defaults to None.
            triangles (numpy.array [k, 3], optional): each row is a list of point indices used to
                render triangles. Defaults to None.
            points (numpy.array [n, 3], optional): each row represents a 3D point. Defaults to None.
            normals (numpy.array [n, 3], optional): each row represents the normal vector for the
                corresponding 3D point. Defaults to None.
            colors (numpy.array [n, 3], optional): each row represents the color of the
                corresponding 3D point. Defaults to None.
        """
        from plyfile import PlyData, PlyElement
        
        super().__init__()


        if ply_path is None:
            self.triangles = triangles
            self.points = points
            self.normals = normals
            self.colors = colors.astype(int)
        else:
            self.read(ply_path)
    
        
        if ply_path is not None:
            if type(triangles) is not None:
                if type(points) is not None: 
                    if type(normals) is not None:
                        if np.shape(points) is not np.shape(normals) or type(points) == None or type(normals) == None:
                            print('The number of points and normals are not equal')
                            if type(colors) is not None:
                                if np.shape(colors) == np.shape(normals) or type(colors) == None or type(normals) == None:
                                    print('The number of colors and normals are not equal')
                                    plydata = open(ply_path, 'r')
                                    
                                    
                                    
    def write(self, ply_path):

    
        b = []
        for j in range(len(triangles)):
            b.append(triangles[j])
        
        plydata = open(ply_path, 'w')

        plydata.write('ply\n')
        plydata.write('format ascii 1.0 \n')
        plydata.write(f'element vertex {np.shape(points)[0]} \n')   # number of points

        plydata.write('property float x \n')                        # first entry of a point.
        plydata.write('property float y \n')
        plydata.write('property float z \n')

        plydata.write('property float nx \n')                       # first normal component of the point.
        plydata.write('property float ny \n')
        plydata.write('property float nz \n')


        plydata.write('property uchar red \n')                      # red component of the point color.
        plydata.write('property uchar green \n')
        plydata.write('property uchar blue \n')


        plydata.write(f'element face {np.shape(triangles)[0]} \n')  # first triangle faces component of the point.
        plydata.write('property list uchar int vertex_index \n')
# need to check 

        plydata.write('end_header \n')

        plydata = open(ply_path, 'a')
        
#         print(a)
        
        for i in range(len(points)):
            x= str(points[i]) + str(normals[i]) + str(colors[i])
            
            x = x.replace("[","")
            x = x.replace("]"," ") 
            f = open(ply_path,'a')
            f.write(x + '\n')
            f.close()
            
        for i in triangles:
            b = str(i)
            b = b[1:]
            b = b[:-1]
            f = open(ply_path,'a')
            f.write(b + '\n')
                  
        pass

    def read(self, ply_path):
        """Read a ply into memory.

        Args:
            ply_path (str): ply to read in.
        """
#         print(triangles)
        # TODO: Read in ply.
        ls = []
        with open('triangle_sample.ply') as fp:
            for line in fp:
                a = line.split()
                ls.append(a)
        
        points = []
        normals = []
        colors = []
        triangles = []
        for i in range(len(ls)):
            if 'end_header' in ls[i]:
        #         print(i)
                for j in range(i+1, len(ls), 1):
                    if '.' in ls[j][0]:             # always true as points will be in floating points
                        points.append(ls[j][:3])
        #                 print(i)

                    for i in range(len(ls)):
                        if 'nx' in ls[i]:
        #                     print('yes')
                            if '.' in ls[j][0]:
                                normals.append(ls[j][3:6])

                    for i in range(len(ls)):
                        if 'red' in ls[i]:
        #                     print('yes')
                            if '.' in ls[j][0]:
                                colors.append(ls[j][6:9])

                    for i in range(len(ls)):
                        if 'face' in ls[i]:
        #                     print('yes')
                            if '.' not in ls[j][0]:
                                triangles.append(ls[j])


        points = np.array(points)    
        normals = np.array(normals) 
        colors = np.array(colors)
        triangles = np.array(triangles)
        
        self.points = points
        self.normals = normals
        self.colors = colors
        self.triangles = triangles
        
        return  points, normals, colors, triangles

