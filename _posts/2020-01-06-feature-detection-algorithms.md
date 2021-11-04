---
layout: post
title: "Feature Detection"
category: mobile
description: 常见的特征提取算法
thumb: /images/2019-03-28-annual-review.jpg
---

参考资料：
- [AR & Video Streaming Services Emerging Technologies - Coursera](https://www.coursera.org/learn/ar-technologies-video-streaming)
- [Feature Detection and Description - OpenCV-Python Tutorials](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_feature2d/py_table_of_contents_feature2d/py_table_of_contents_feature2d.html)


| | SIFT | SURF | FAST | BRIEF | ORB | BRISK |
| -- | -- | -- | -- | -- | -- | -- |
| Year | 1999 | 2006 | 2006 | 2010 | 2011 | 2011 |
| Feature Detector | Difference of Gaussian | Fast Hessian | Binary comparison | N/A | FAST | FAST or AGAST |
| Spectra | Local gradient magnitude | Integral box filter | N/A | Local binary | Local binary | Local binary |
| Orientation | Yes | Yes | N/A | No | Yes | Yes |
| Feature Shape | Square | HAAR rectangles | N/A | Square | Square | Square |
| Feature Pattern | Square | Dense | N/A | Random point-pair pixel compares | Trained point-pair pixel compares | Trained point-pair pixel compares |

