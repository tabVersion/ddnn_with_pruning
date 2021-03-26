import time
import logging


def edge_compute(track_id, image):
    """
    computing part
    """
    time.sleep(1)
    feature_map = [0.0] * 16
    return [1.0] + [0.0] * 9, feature_map


def aggregate(res):
    logging.info(f"[aggregate] get edge results: {res}")
    return False
