from .libwallaby import libwallaby
from .configuration import CameraConfiguration
from .helpers import Rectangle

class Camera(object):
    '''
    Represents a USB camera connected to the robot.
    '''

    def __init__(self, color):
        '''
        Initializes the camera with a color to track.

        **Warning:** If the camera is not connected to the robot, then the
        program will crash.
        '''

        self.set_color(color)

    def set_color(self, color):
        '''
        Change the color to track, so objects of that color will be detected.
        '''

        self.color = color

        conf_name = 'detect-%s' % color

        success = libwallaby.camera_load_config(bytes(conf_name))
        assert success, 'Error loading camera configuration file "%s"' % conf_name

        self.refresh()

    def refresh(self, number_of_frames=CameraConfiguration.refresh_frames):
        '''
        Refreshes the camera by collecting the specified number of frames, to
        make object tracking more accurate. Blocks the thread until finished.

        You shouldn't normally need to call this method yourself; it is called
        automatically during initialization and when the camera's color is
        changed.
        '''

        for _ in range(number_of_frames):
            libwallaby.camera_update()

    def height(self):
        '''
        The height of the camera frame in pixels, adjusted for offset.
        '''

        return libwallaby.get_camera_height() - CameraConfiguration.height_offset

    def number_of_objects(self):
        '''
        The number of trackable objects currently in the field of view.
        '''

        return libwallaby.get_object_count(CameraConfiguration.channel)

    def object_is_present(self):
        '''
        Whether an object of the current color is present in the field of view.
        '''

        return self.number_of_objects() > 0

    def object_bounding_box(self, object_index = 0):
        '''
        Returns the bounding box for an object in the field of view, or `None`
        if there is no object.
        '''

        if object_index >= self.number_of_objects():
            return None

        bbox = libwallaby.get_object_bbox(CameraConfiguration.channel, object_index)

        return Rectangle(bbox.ulx, bbox.uly, bbox.width, bbox.height)

    def distance_to_object(self, object_height_cm, object_index = 0):
        '''
        Returns the distance to an object in the field of view, or `None` if
        there is no object. `object_height` is the height of the desired object
        in cm. This should be a known value based on the real-world measurement
        of the desired object.
        '''

        object_bounding_box = self.object_bounding_box(object_index)

        if object_bounding_box is None:
            return None

        object_height_px = float(object_bounding_box.height)

        return self.height() * object_height_cm * 10 / object_height_px

    def confidence(self, object_index = 0):
        '''
        Returns the camera's confidence that the object is in the field of view,
        or `None` if the object is not found at all.
        '''

        if object_index >= self.number_of_objects():
            return None

        return libwallaby.get_object_confidence(CameraConfiguration.channel, object_index)

    def object_is_trackable(self, object_index = 0):
        '''
        Returns whether an object is considered to be visible enough to be
        trackable by the camera, or `None` if the object is not found at all.
        '''

        confidence = self.confidence(object_index)

        if confidence is None:
            return None

        return confidence >= CameraConfiguration.confidence_threshold
