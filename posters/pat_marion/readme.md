
Title : 3D Perception: Point cloud data processing and visualization
====================================================================

Authors :
---------

- Pat Marion, Kitware, Inc.

Abstract :
----------

The Point Cloud Library (PCL) is a popular open-source C++ library for scientists developing 3D perception algorithms and applications. The Visualization Toolkit (VTK) is a scientific visualization and data filtering library used by PCL. By leveraging VTK's well-engineered Python bindings, users of scientific Python can import the capabilities of PCL and VTK into their SciPy/NumPy programs.

This talk will introduce the basic concepts required for users to write their own scientific Python programs using PCL and VTK. Examples of point cloud processing and visualization algorithms will be demonstrated. Through these simple examples, the audience will learn about point cloud data structures, algorithms, and I/O. Users will understand the workflow that makes it possible to share point cloud data arrays between PCL and NumPy data structures. With these libraries, point clouds can make the round-trip from PCL to SciPy, and back to PCL.

PCL provides interfaces for live point cloud data acquisition from popular sensors like the Microsoft Kinect camera or the Velodyne High-Definition Lidar sensor. This talk will show how a Python program can leverage the PCL interfaces to acquire live point cloud data for processing with SciPy and Numpy.
