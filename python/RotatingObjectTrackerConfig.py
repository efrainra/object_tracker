## *********************************************************
## 
## File autogenerated for the object_tracker package 
## by the dynamic_reconfigure package.
## Please do not edit.
## 
## ********************************************************/

##**********************************************************
## Software License Agreement (BSD License)
##
##  Copyright (c) 2008, Willow Garage, Inc.
##  All rights reserved.
##
##  Redistribution and use in source and binary forms, with or without
##  modification, are permitted provided that the following conditions
##  are met:
##
##   * Redistributions of source code must retain the above copyright
##     notice, this list of conditions and the following disclaimer.
##   * Redistributions in binary form must reproduce the above
##     copyright notice, this list of conditions and the following
##     disclaimer in the documentation and/or other materials provided
##     with the distribution.
##   * Neither the name of the Willow Garage nor the names of its
##     contributors may be used to endorse or promote products derived
##     from this software without specific prior written permission.
##
##  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
##  "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
##  LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
##  FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
##  COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
##  INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
##  BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
##  LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
##  CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
##  LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
##  ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
##  POSSIBILITY OF SUCH DAMAGE.
##**********************************************************/

from dynamic_reconfigure.encoding import extract_params

inf = float('inf')

config_description = {'parameters': [{'srcline': 32, 'description': 'The fixed TF frame to use for the rotation estimation.', 'max': '', 'cconsttype': 'const char * const', 'ctype': 'std::string', 'srcfile': '/wg/stor5/tcavallari/catkin_workspace/src/object_tracker/cfg/RotatingObjectTracker.cfg', 'name': 'fixed_frame', 'edit_method': '', 'default': '/base_link', 'level': 0, 'min': '', 'type': 'str'}, {'srcline': 33, 'description': 'The TF frame used to publish the center of rotation.', 'max': '', 'cconsttype': 'const char * const', 'ctype': 'std::string', 'srcfile': '/wg/stor5/tcavallari/catkin_workspace/src/object_tracker/cfg/RotatingObjectTracker.cfg', 'name': 'rotation_center_frame', 'edit_method': '', 'default': '/rotation_center', 'level': 0, 'min': '', 'type': 'str'}, {'srcline': 34, 'description': 'The TF frame used to publish the rotating objects', 'max': '', 'cconsttype': 'const char * const', 'ctype': 'std::string', 'srcfile': '/wg/stor5/tcavallari/catkin_workspace/src/object_tracker/cfg/RotatingObjectTracker.cfg', 'name': 'rotating_frame', 'edit_method': '', 'default': '/rotating_objects', 'level': 0, 'min': '', 'type': 'str'}, {'srcline': 35, 'description': 'The minimum number of poses that need to be seen before start tracking an object.', 'max': 2147483647, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/wg/stor5/tcavallari/catkin_workspace/src/object_tracker/cfg/RotatingObjectTracker.cfg', 'name': 'min_poses_for_tracking', 'edit_method': '', 'default': 5, 'level': 0, 'min': -2147483648, 'type': 'int'}, {'srcline': 36, 'description': 'The max number of poses to keep for an object. This number influences the speed at which the model is adapted.', 'max': 2147483647, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/wg/stor5/tcavallari/catkin_workspace/src/object_tracker/cfg/RotatingObjectTracker.cfg', 'name': 'max_poses_for_object', 'edit_method': '', 'default': 50, 'level': 0, 'min': -2147483648, 'type': 'int'}, {'srcline': 37, 'description': 'The max time the node keeps track of an unseen object.', 'max': 60.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/wg/stor5/tcavallari/catkin_workspace/src/object_tracker/cfg/RotatingObjectTracker.cfg', 'name': 'max_stale_time', 'edit_method': '', 'default': 10.0, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 38, 'description': 'The maximum distance between two poses to consider them a single object.', 'max': 1.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/wg/stor5/tcavallari/catkin_workspace/src/object_tracker/cfg/RotatingObjectTracker.cfg', 'name': 'same_object_threshold', 'edit_method': '', 'default': 0.1, 'level': 0, 'min': 0.01, 'type': 'double'}, {'srcline': 39, 'description': 'Search for objects only inside a specific area (With fixed_frame coordinates).', 'max': True, 'cconsttype': 'const bool', 'ctype': 'bool', 'srcfile': '/wg/stor5/tcavallari/catkin_workspace/src/object_tracker/cfg/RotatingObjectTracker.cfg', 'name': 'use_roi', 'edit_method': '', 'default': False, 'level': 0, 'min': False, 'type': 'bool'}, {'srcline': 40, 'description': 'The minimum X coordinate for the detection ROI', 'max': 100.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/wg/stor5/tcavallari/catkin_workspace/src/object_tracker/cfg/RotatingObjectTracker.cfg', 'name': 'x_min', 'edit_method': '', 'default': -100.0, 'level': 0, 'min': -100.0, 'type': 'double'}, {'srcline': 41, 'description': 'The maximum X coordinate for the detection ROI', 'max': 100.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/wg/stor5/tcavallari/catkin_workspace/src/object_tracker/cfg/RotatingObjectTracker.cfg', 'name': 'x_max', 'edit_method': '', 'default': 100.0, 'level': 0, 'min': -100.0, 'type': 'double'}, {'srcline': 42, 'description': 'The minimum Y coordinate for the detection ROI', 'max': 100.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/wg/stor5/tcavallari/catkin_workspace/src/object_tracker/cfg/RotatingObjectTracker.cfg', 'name': 'y_min', 'edit_method': '', 'default': -100.0, 'level': 0, 'min': -100.0, 'type': 'double'}, {'srcline': 43, 'description': 'The maximum Y coordinate for the detection ROI', 'max': 100.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/wg/stor5/tcavallari/catkin_workspace/src/object_tracker/cfg/RotatingObjectTracker.cfg', 'name': 'y_max', 'edit_method': '', 'default': 100.0, 'level': 0, 'min': -100.0, 'type': 'double'}, {'srcline': 44, 'description': 'The minimum Z coordinate for the detection ROI', 'max': 100.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/wg/stor5/tcavallari/catkin_workspace/src/object_tracker/cfg/RotatingObjectTracker.cfg', 'name': 'z_min', 'edit_method': '', 'default': -100.0, 'level': 0, 'min': -100.0, 'type': 'double'}, {'srcline': 45, 'description': 'The maximum Z coordinate for the detection ROI', 'max': 100.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/wg/stor5/tcavallari/catkin_workspace/src/object_tracker/cfg/RotatingObjectTracker.cfg', 'name': 'z_max', 'edit_method': '', 'default': 100.0, 'level': 0, 'min': -100.0, 'type': 'double'}, {'srcline': 46, 'description': 'The rate in Hz at which to invoke the object detection service.', 'max': 100.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/wg/stor5/tcavallari/catkin_workspace/src/object_tracker/cfg/RotatingObjectTracker.cfg', 'name': 'detection_rate', 'edit_method': '', 'default': 2.0, 'level': 0, 'min': 0.1, 'type': 'double'}, {'srcline': 47, 'description': 'The rate in Hz at which to publish the TF data.', 'max': 1000.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/wg/stor5/tcavallari/catkin_workspace/src/object_tracker/cfg/RotatingObjectTracker.cfg', 'name': 'tf_rate', 'edit_method': '', 'default': 20.0, 'level': 0, 'min': 0.1, 'type': 'double'}], 'groups': [], 'name': '', 'id': 0, 'parent': 0, 'type': ''}

min = {}
max = {}
defaults = {}
level = {}
type = {}
all_level = 0

#def extract_params(config):
#    params = []
#    params.extend(config['parameters'])    
#    for group in config['groups']:
#        params.extend(extract_params(group))
#    return params

for param in extract_params(config_description):
    min[param['name']] = param['min']
    max[param['name']] = param['max']
    defaults[param['name']] = param['default']
    level[param['name']] = param['level']
    type[param['name']] = param['type']
    all_level = all_level | param['level']
